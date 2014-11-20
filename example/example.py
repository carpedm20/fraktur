#!/usr/bin/python
import fraktur

quote = """So avoid using the word 'very' because it's lazy.
A man is not very tired, he is exhausted.
Don't use very sad, use morose.
Language was invented for one reason,
boys - to woo women - and, in that endeavor,
laziness will not do. It also won't do in your essays."""

print fraktur.encode(quote)
print
print fraktur.decode(fraktur.encode(quote))
