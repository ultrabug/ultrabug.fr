---
title: "nginx : conditional uWSGI error handling"
date: "2012-02-27"
categories: 
  - "linux"
tags: 
  - "conditional"
  - "error"
  - "nginx"
  - "uwsgi"
---

To ensure the best possible quality of service we want to make sure that we catch our **uWSGI** application failures on the **nginx** side and react accordingly. Our goal is to never serve a HTTP 500 error to visitors. I'll show you how you can **adapt nginx error handling behavior based on the URI called by the visitor**.

# nginx + uWSGI base configuration (nginx.conf)

Suppose we have the following configuration to handle our uWSGI apps. We have set our gateway timeouts to 10 seconds to make sure no request will take more than that time to be answered, no matter what our application do.

upstream uwsgi_app1  {
	server 127.0.0.1:1000;
}

location / {
	uwsgi_pass uwsgi_app1;
	include uwsgi_params;
	uwsgi_ignore_client_abort on;
	uwsgi_connect_timeout 10;
	uwsgi_read_timeout 10;
	uwsgi_send_timeout 10;
}

# Static uWSGI error handling

Now  we don't want nginx to reply to clients with errors such as 500 (our app crashed) and 504 (timeout has been triggered). At first, we'll serve a simple 1x1 GIF pixel instead.

location = /px.gif {
	empty_gif;
}

upstream uwsgid  {
	server 127.0.0.1:1000;
}

location / {
	uwsgi_pass uwsgi_app1;
	include uwsgi_params;
	uwsgi_ignore_client_abort on;
	uwsgi_connect_timeout 10;
	uwsgi_read_timeout 10;
	uwsgi_send_timeout 10;

	uwsgi_intercept_errors on;
	error_page 500 504 /px.gif;
}

The **uwsgi_intercept_errors** directive tells nginx to handle errors from uWSGI. Then we just have to use the usual nginx error handling using the **error_page** directive which in our case calls for /px.gif, returning our 1x1 GIF pixel using the **empty_gif** nginx module.

# Dynamic uWSGI error handling

Let's go conditional, suppose we have two types or URLS :

1. http://www.mysite.com/APP1?query=bar
2. http://www.mysite.com/APP1?query=foo&**redir=http://www.ultrabug.fr**&word=bar

For URL #1, we want to serve the 1x1 pixel whereas for URL #2, when we receive the **redir** parameter, we want to redirect the visitor to exactly that URI.

It's standard [error_page](http://wiki.nginx.org/HttpCoreModule#error_page "error_page") handling remember ? Let's use the **named location** feature to process the request.

location @uwsgi_errors {
	rewrite_log on;
	if ($arg_redir ~\* (.+)) {
		set $redir $1;
		rewrite ^ $redir? redirect;
	}
	rewrite ^ /px.gif? redirect;
}

location / {
	uwsgi_pass uwsgi_app1;
	include uwsgi_params;
	uwsgi_ignore_client_abort on;
	uwsgi_connect_timeout 10;
	uwsgi_read_timeout 10;
	uwsgi_send_timeout 10;

	uwsgi_intercept_errors on;
	error_page 500 504 @uwsgi_errors;
}

Upon HTTP 500/504 error, the **@uwsgi_errors** location is called by nginx internals. Let's detail its processing :

- **rewrite_log on** : turn the rewriting logging on for debugging / monitoring reasons
- **$arg_redir ~\* (.+)** : [$arg_PARAMETER](http://wiki.nginx.org/HttpCoreModule#Variables "nginx variables") is a neat way to get the value of the given GET parameter (**redir** in our case). The condition here means that if the parameter is present, we'll use it and enter the condition.
- **rewrite ^ $redir? redirect** : we call the [rewrite module](http://wiki.nginx.org/HttpRewriteModule "nginx rewrite") using the redirect method to send a HTTP 302 to the client with the value of the previously defined **$redir** variable which contains the URI of the redir parameter. **The important part here is the question mark after the $redir variable which makes sure that the original URI parameters are stripped from the redirection URI.**
- **rewrite ^ /px.gif? redirect** : if no redir parameter was received, we redirect to the the px.gif as usual. The question mark has the same meaning as above.

That's it, we managed to handle our uWSGI errors based on certain conditions. Of course we could go further and use more named locations for different types of HTTP errors and use more nginx variables and conditions but that's up to you now !
