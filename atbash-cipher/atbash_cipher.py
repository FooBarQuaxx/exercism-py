#!/usr/bin/env python2

# TODO: make it work on py3
import string
from string import maketrans

ENCODE_TRANSLATION = maketrans(string.ascii_uppercase + string.ascii_lowercase,
                               2 * string.ascii_lowercase[::-1])

DECODE_TRANSLATION = maketrans(2 * string.ascii_lowercase[::-1],
                               string.ascii_uppercase + string.ascii_lowercase)


def encode(s):
    trans = s.translate(ENCODE_TRANSLATION, string.punctuation + ' ')
    return ' '.join([trans[i: i + 5] for i in xrange(0, len(trans), 5)])


def decode(s):
    return s.translate(DECODE_TRANSLATION, string.punctuation + ' ')
