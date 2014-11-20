# -*- coding: utf-8 -*-
"""
    𝔣𝔯𝔞𝔨𝔱𝔲𝔯.𝔣𝔯𝔞𝔨𝔱𝔲𝔯
    ~~~~~~~~~~~~~~~
    𝔠𝔬𝔫𝔳𝔢𝔯𝔱 𝔱𝔥𝔢 𝔩𝔞𝔱𝔦𝔫 𝔞𝔩𝔭𝔥𝔞𝔟𝔢𝔱 𝔱𝔬 𝔣𝔯𝔞𝔨𝔱𝔲𝔯 𝔲𝔫𝔦𝔠𝔬𝔡𝔢 𝔠𝔥𝔞𝔯𝔞𝔠𝔱𝔢𝔯𝔰

    :license: 𝔐𝕴𝔗, 𝔰𝔢𝔢 𝔏𝕴𝕮𝔈𝔑𝔖𝔈 𝔣𝔬𝔯 𝔪𝔬𝔯𝔢 𝔡𝔢𝔱𝔞𝔦𝔩𝔰.
"""
from .code import encodeCode, decodeCode

def encode(text):
    if isinstance(text, unicode):
        return text.translate(encodeCode)
    else:
        return text.decode('utf8').translate(encodeCode).encode('utf8')

def decode(text):
    if isinstance(text, unicode):
        return text.translate(decodeCode)
    else:
        return text.decode('utf8').translate(decodeCode).encode('utf8')
