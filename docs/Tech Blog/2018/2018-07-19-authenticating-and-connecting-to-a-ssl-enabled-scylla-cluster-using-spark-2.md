---
title: "Authenticating and connecting to a SSL enabled Scylla cluster using Spark 2"
date: "2018-07-19"
categories: 
  - "linux"
tags: 
  - "gentoo"
  - "scylla"
---

This quick article is a wrap up for reference on how to **connect to ScyllaDB using Spark 2** when authentication and SSL are enforced for the clients on the Scylla cluster.

We encountered multiple problems, even more since we distribute our workload using a YARN cluster so that our worker nodes should have everything they need to connect properly to Scylla.

We found very little help online so I hope it will serve anyone facing similar issues (that's also why I copy/pasted them here).

The [authentication part](http://docs.scylladb.com/operating-scylla/security/) is easy going by itself and was not the source of our problems, SSL on the client side was.

# Environment

- (py)spark: 2.1.0.cloudera2
- spark-cassandra-connector: datastax:spark-cassandra-connector: 2.0.1-s\_2.11
- python: 3.5.5
- java: 1.8.0\_144
- scylladb: 2.1.5

# SSL cipher setup

The Datastax spark cassandra driver uses default the **TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA** cipher that the JVM does not support by default. This raises the following error when connecting to Scylla:

18/07/18 13:13:41 WARN channel.ChannelInitializer: Failed to initialize a channel. Closing: \[id: 0x8d6f78a7\]
java.lang.IllegalArgumentException: Cannot support TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA with currently installed providers

According to the [ssl documentation](https://github.com/datastax/spark-cassandra-connector/blob/master/doc/reference.md#cassandra-ssl-connection-options) we have two ciphers available:

1. TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA
2. TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA

We can get get rid of the error by lowering the cipher to **TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA** using the following configuration:

.config("spark.cassandra.connection.ssl.enabledAlgorithms", "TLS\_RSA\_WITH\_AES\_128\_CBC\_SHA")\\

However, this is not really a good solution and instead we'd be inclined to **use the TLS\_RSA\_WITH\_AES\_256\_CBC\_SHA** version. For this we need to follow this [Datastax's procedure](https://support.datastax.com/hc/en-us/articles/204226129-Receiving-error-Caused-by-java-lang-IllegalArgumentException-Cannot-support-TLS-RSA-WITH-AES-256-CBC-SHA-with-currently-installed-providers-on-DSE-startup-after-setting-up-client-to-node-encryption).

Then we need to deploy the JCE security jars **on our all client nodes**, if using YARN like us this means that you have to deploy these jars to all your NodeManager nodes.

For example by hand:

\# unzip jce\_policy-8.zip
# cp UnlimitedJCEPolicyJDK8/\*.jar /opt/oracle-jdk-bin-1.8.0.144/jre/lib/security/

# Java trust store

When connecting, the clients need to be able to validate the Scylla cluster's self-signed CA. This is done by setting up a **trustStore JKS file** and providing it to the spark connector configuration (note that you protect this file with a password).

## keyStore vs trustStore

In SSL handshake purpose of **trustStore is to verify credentials** and purpose of **keyStore is to provide credentials**. keyStore in Java stores private key and certificates corresponding to the public keys and is required if you are a SSL Server or SSL requires client authentication. TrustStore stores certificates from third parties or your own self-signed certificates, your application identify and validates them using this trustStore.

The [spark-cassandra-connector documentation](https://github.com/datastax/spark-cassandra-connector/blob/master/doc/reference.md#cassandra-ssl-connection-options) has two options to handle keyStore and trustStore.

When we did not use the **trustStore** option, we would get some obscure error when connecting to Scylla:

com.datastax.driver.core.exceptions.TransportException: \[node/1.1.1.1:9042\] Channel has been closed

When enabling DEBUG logging, we get a clearer error which indicated a failure in validating the SSL certificate provided by the Scylla server node:

Caused by: sun.security.validator.ValidatorException: PKIX path building failed: sun.security.provider.certpath.SunCertPathBuilderException: unable to find valid certification path to requested target

## setting up the trustStore JKS

You need to have the self-signed CA public certificate file, then issue the following command:

\# keytool -importcert -file /usr/local/share/ca-certificates/MY\_SELF\_SIGNED\_CA.crt -keystore COMPANY\_TRUSTSTORE.jks -noprompt
Enter keystore password:  
Re-enter new password: 
Certificate was added to keystore

## using the trustStore

Now you need to configure spark to use the trustStore like this:

.config("spark.cassandra.connection.ssl.trustStore.password", "PASSWORD")\\
.config("spark.cassandra.connection.ssl.trustStore.path", "COMPANY\_TRUSTSTORE.jks")\\

# Spark SSL configuration example

This wraps up the SSL connection configuration used for spark.

This example uses pyspark2 and reads a table in Scylla from a YARN cluster:

$ pyspark2 --packages datastax:spark-cassandra-connector:2.0.1-s\_2.11 --files COMPANY\_TRUSTSTORE.jks

>>> spark = SparkSession.builder.appName("scylla\_app")\\
.config("spark.cassandra.auth.password", "test")\\
.config("spark.cassandra.auth.username", "test")\\
.config("spark.cassandra.connection.host", "node1,node2,node3")\\
.config("spark.cassandra.connection.ssl.clientAuth.enabled", True)\\
.config("spark.cassandra.connection.ssl.enabled", True)\\
.config("spark.cassandra.connection.ssl.trustStore.password", "PASSWORD")\\
.config("spark.cassandra.connection.ssl.trustStore.path", "COMPANY\_TRUSTSTORE.jks")\\
.config("spark.cassandra.input.split.size\_in\_mb", 1)\\
.config("spark.yarn.queue", "scylla\_queue").getOrCreate()

>>> df = spark.read.format("org.apache.spark.sql.cassandra").options(table="my\_table", keyspace="test").load()
>>> df.show()
