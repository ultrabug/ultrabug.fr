---
title: "Convert special characters to ASCII in python"
date: "2014-04-04"
categories: 
  - "linux"
tags: 
  - "python"
---

I came across a recurrent problem at work which was to convert special characters such as the French-Latin accentuated letter **"é"** to ASCII **"e"** (this is called transliteration).

I wanted to avoid having to use an external library such as [Unidecode](https://pypi.python.org/pypi/Unidecode/) (which is great obviously) so I ended up wandering around the **unicodedata** built-in library. Before I had to get too deep in the matter I found this [StackOverflow topic](http://stackoverflow.com/questions/517923/what-is-the-best-way-to-remove-accents-in-a-python-unicode-string) which gives an interesting method to do so and works fine for me.

def strip\_accents(s):
    """
    Sanitarize the given unicode string and remove all special/localized
    characters from it.

    Category "Mn" stands for Nonspacing\_Mark
    """
    try:
        return ''.join(
            c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
        )
    except:
        return s

_PS : thanks to @Flameeyes for his good remark on wording_
