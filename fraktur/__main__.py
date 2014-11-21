# This code was suggested from this comment.
# http://www.reddit.com/r/Python/comments/2mv0n7/convert_the_latin_alphabet_to_fraktur_unicode/cm89aqv
import sys
from .fraktur import encode

for line in sys.stdin:
    sys.stdout.write(encode(line))
