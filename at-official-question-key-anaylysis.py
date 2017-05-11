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
AAABNA0ODAoPeNqtkcFLwzAUxu/5KwJe9NCyVp1uEFC6HoS1UzvFg5dneK2BNK0vSdn+e1M3dXgcH
gLhe8nv+z7eydojL7uBpzM+uZin03lyybNqzdNJMmULtJJU71RnxINHO14srzviWWdq7dFI5KcV0
oB09jrn+QDaw/iKlb59Q1rVTxbJiihhGeHXZAEOxUiPkiRKZ0x2bQxOg7UKTCx/uHGvfaOMPZCij
+8MMUinBhSOPB5JqByQQxI1aIss9HGBmRegtGjRNBsVUMptb5o2SAHRst92O1+tJBqLz6HgqKUsf
DYODQSjfNMr2h50TY/vutz5rLc9ltCiyFZFkT9md7dLtqIGjLK7UC/K8CJEZ1VeinCi5fVsklydX
7E94T9DYWhKPSm7X8K9J/kOFv+u9xObW9f8MCwCFGHz+Oc52N08Huo0IxNCxwcYSmuRAhQOiTCSY
5jV5M51I4JbD2sVuUZXhA==X02ff
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
