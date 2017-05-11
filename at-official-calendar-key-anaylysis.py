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
AAABJg0ODAoPeNptkMFKxDAQhu95ioAXPXTZ1GV1CwGl24Ow7Yqt4kGQMU5roE3LJC3btzdrV5Syh
7nM5P/mm1wUPfKsHXi44ctVFK6ja8HjvODhUqzZFq0i3TndGlkgNDyGGs0nkOVlSzxuTVn3aBTyy
xxpQLp6i3gyQN3DMcOyvvlA2pfPFsnKQDDnIe/qF7JA45A60halox5ZTPgT3IJDeTQIhAjCzTwGy
unhFJmNcgfkmbKE2npea5x/nKSga9mgqQ7aLJR2413V+NZCtQ37052AtVZoLL5442MvZD7sNQ34M
5NDp2n8ZxeesdtNgGLsMIMGZbxP0+QpfrjfsT1VYLSdtr1qw1PvxPIkk76C3e1mKW5Wgp0I57c99
qS+wOL8j74BhDub1jAsAhR0M9yXHbJQZB2AybfumJc32bJO4wIUNJHzx01QaZmuRHCj7WwA1Hz77
Is=X02eq
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
