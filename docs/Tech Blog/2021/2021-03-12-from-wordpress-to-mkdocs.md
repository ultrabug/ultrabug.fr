# From Wordpress to MkDocs

The idea of a statically built website has been in my mind for a while but I
never found a satisfying stack to make it happen until I discovered and got
intimate with [MkDocs](https://www.mkdocs.org/).

Building a static website out of any kind of formatted text file neither new
nor hard to do. But when I was interested in the subject a while ago, the
ecosystem to support it and make it useful was not as mature as it is today.

## My website stack wish list

What I wanted was the ability to:

- build a responsive website out of simple text formatted files
- have a versioned, historized and Open Source view of my website sources on git
- work on different kind of content, from simple pages to blog posts to tutorials
- test it locally
- deploy and host it seamlessly (and at no cost if possible)
- have everything automated (except the actual writing, ok!)

Bonus was to be able to:

- have the possibility to add dynamic content in the build process

## MkDocs?

Yep that means that I got the crazy idea of using a project initially designed
to ease the creation of technical documentation of projects for my website.

!!! quote
    MkDocs is a fast, simple and downright gorgeous static site generator that's geared towards building project documentation. Documentation source files are written in Markdown, and configured with a single YAML configuration file. Start by reading the introduction below, then check the User Guide for more info.

After you swallow the possible shock or fear, let's reconsider my stack wish
list above... After all, a git based website made out of text files that is
built by a CI and hosted through CD looks exactly the same to me as a technical
documentation build and hosting process!

All it needs is some nice sugar to accomodate with specific needs.

## Converting my Wordpress content to Markdown

I used the nice [wordpress export to markdown](https://github.com/lonekorean/wordpress-export-to-markdown)
project which did the work perfectly for me as I could run the export to output
a file structure fitting my mkdocs file hierarchy needs.

## The ultrabug.fr stack

### Git

Let's start with the obvious **git** to get revision control over the sources
of the website. Be it text files, media files and configuration files:
everything is on git!

### MkDocs

Now MkDocs comes into play as it offers a straightforward way to structurate
and configure the resulting website.

By itself it does not offer all the features I needed. For example, a blog
section needs to sort articles by the "most recent" first while some other
sections of the website simply need alphabetical ordering. Wait, what if this
particular sub-section you wanted first? What about emojis or nice thumbnails?

Here is a list of what I'm using to enrich MkDocs and accomodate my needs:

- [X] [mkdocs-material](https://github.com/squidfunk/mkdocs-material): this is
a responsive and good looking theme for MkDocs that offers some nice features
to present your content in a lean way.
- [X] [mkdocs-redirects](https://github.com/datarobot/mkdocs-redirects): I did
not want to break my old links so I'm using this mkdocs plugin to make sure that
my old Wordpress content is still redirected to the new mkdocs structure URLs
of this website.
- [X] [python markdown extensions](https://github.com/facelessuser/pymdown-extensions): to have nice markdown extensions like these checkboxes and of course emojis :cat:
- [X] [mkdocs-awesome-pages-plugin](https://github.com/lukasgeiter/mkdocs-awesome-pages-plugin): this one is the ultimate plugin if like me you need to control the ordering of your navigation!

### Multi-language support

MkDocs does not support language localization and I wanted to be able to propose
some of my website sections and content in my mother tongue (French) and in English.

My first attempt was to simply add a :gb: and :fr: flag followed by the localized
version of my content on a single page. It was okay, not great but okay enough
so I could live with it at start.

It did not last long since my friend @Lujeni immediately told me that it would
be better without all these flags flying around a same page...

So I ended up writing a [mkdocs plugin to support pages localization](https://github.com/ultrabug/mkdocs-static-i18n) easily!

This work took me a bit (too much?) further and I am now also working on
[adding theme localization support to the whole mkdocs project](https://github.com/mkdocs/mkdocs/pull/2299)!

### Github

Last but not least, I use [Github workflow Actions + Pages](https://github.com/ultrabug/ultrabug.fr) to build and host my website now!

## Take a leap, go static!

I hope this article inspires you to try and use these cool projects :thumbsup:
