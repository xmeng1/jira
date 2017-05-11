#!/usr/bin/env python
# -*- coding: utf-8 -*-
import M2Crypto
import base64
import hashlib
import struct
import zlib
# Some constants
ENCODED_LICENSE_LENGTH_BASE = 31
LICENSE_PREFIX = ''.join(map(chr, [13, 14, 12, 10, 15]))
SEPARATOR = 'X'
ATLASSIAN_PUBLIC_KEY = './atlassian_pub.pem'
# Confluence eveluation license_key
license_key = '''
AAABKw0ODAoPeNptkF9LwzAUxd/zKQK+6EPK0ulwhYDadlDWP2K74YMvMdzNQJuWJC3rtzddRaf4E
Aj3nnPu796rqgectwP213ixDOhdsKQ4LCvsL+gKRWCElp2VrWJhqw51D0oAvi5BD6Bv3gIcD7zu+
SRAoYbzJ+IW2GQnlBJ/jYQzelxYOQCzuoe5UFquLWh24LUB5MKtk8QZlzVrQB1PUnlC2vHh2LiSJ
9oG/Yy6iEmlAGWgGjvIeQMsLLIsfgmTxxTVc2sP2kweH7lwZUFxt0J86qQeL0j9ibTQR66kmWe8S
oUzR4LmZZOIPVVJRPa7eEs221VBNrfZHpVxztwj6f16QZeUoi8gJ0+T6FfnzJv3zTvo4rAzDouRb
/3/QM+9Fh/cwN+TfgKaHo4uMCwCFB0UqWEpl08fexR7ZlOkoAdCI1kIAhQvuD3uPv5cJnOD23pk7
XF/M+gxmg==X02f3
'''
# Remove any white spaces and return in the key
license_content = license_key.replace("\r", "").replace("\n", "").replace("\t", "").replace(" ", "")
# Check Version
x_position = license_content.rfind(SEPARATOR)
if license_content[x_position + 1:x_position + 3] != "02":
    print "Invalid license version, only license version 2 is supported!"
    exit()
# Get the base64 encoded license
license_length = int(license_content[x_position + 3:], ENCODED_LICENSE_LENGTH_BASE)
encoded_bytes = license_content[:license_length]
# Base64 decode
decoded_bytes = base64.b64decode(encoded_bytes)
text_length, = struct.unpack(">I", decoded_bytes[:4])
license_bytes = decoded_bytes[4:4 + text_length]
# Magic 13, 14, 12, 10, 15 for license header
if license_bytes[:5] != LICENSE_PREFIX:
    print "Invalid license version 2 file"
    exit()
# Get license original text and signature
license_text = zlib.decompress(license_bytes[5:])
license_hash = decoded_bytes[4 + text_length:]
print license_text
# Verify whether it is official key
public_key = M2Crypto.DSA.load_pub_key(ATLASSIAN_PUBLIC_KEY)
official = public_key.verify_asn1(hashlib.sha1(license_bytes).digest(), license_hash)
if official:
    print "This license is official signed."
else:
    print "This license is not official signed."
