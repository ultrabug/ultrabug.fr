# Scylla Webinar May 2022

![scylla rust webinar](../images/scylla_rust_webinar.jpeg)

The ScyllaDB folks and I hosted a webinar on May 5th 2022 that allowed me to update my Scylla Summit 2022 talk and share [my experience of learning Rust the hard way in the migration of Python pipelines to Rust](https://ultrabug.fr/Tech%20Blog/2022/2022-02-21-learning-rust-the-hard-way/).

!!! abstract
    Numberly operates business-critical data pipelines and applications where failure and latency means "lost money" in the best-case scenario. Most of their data pipelines and applications are deployed on Kubernetes and rely on Kafka and ScyllaDB, with Kafka acting as the message bus and ScyllaDB as the source of data for enrichment. The availability and latency of both systems are thus very important for data pipelines. While most of Numberly’s applications are developed using Python, they found a need to move high-performance applications to Rust in order to benefit from a lower-level programming language.

    Learn the lessons from Numberly’s experience, including:

    - Rationale in selecting a lower-level language
    - Developing using a lower-level Rust code base
    - Observability and analyzing latency impacts with Rust
    - Tuning everything from Apache Avro to driver client settings
    - How to build a mission-critical system combining Apache Kafka and ScyllaDB
    - Half a year Rust in production feedback

