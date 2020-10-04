#!/usr/bin/env python3
import os, binascii, hashlib, base58, random

def shex(x):
    return binascii.hexlify(x).decode()

priv_key = os.urandom(32)

full_key = b'\x80' + priv_key
sha256a = hashlib.sha256(full_key).digest()
sha256b = hashlib.sha256(sha256a).digest()
WIF = base58.b58encode(full_key+sha256b[:4])
print('WIF', WIF)
print('shex(full_key)', shex(full_key))