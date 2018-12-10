#!/usr/bin/env python3

from c.storage import Storage as StorageC
from python.src.storage import Storage as StoragePy

from hashlib import sha256


def hash(data):
    return sha256(data).hexdigest()[:16]


sc = StorageC()
sp = StoragePy()
a = []

# Strings for testing ChaCha20 encryption.
test_strings = [b"Short string.", b"", b"Although ChaCha20 is a stream cipher, it operates on blocks of 64 bytes. This string is over 152 bytes in length so that we test multi-block encryption.", b"This string is exactly 64 bytes long, that is exactly one block."]

# Unique device ID for testing.
uid = b"\x67\xce\x6a\xe8\xf7\x9b\x73\x96\x83\x88\x21\x5e"

for s in [sc, sp]:
    print(s.__class__)
    s.init(uid)
    s.unlock(1)
    s.set(0xbeef, b"hello")
    s.set(0x03fe, b"world!")
    s.set(0xbeef, b"ahojj")
    d = s._dump()
    print(d[0][:512].hex())
    h = [hash(x) for x in d]
    print(h)
    a.append(h[0])
    a.append(h[1])
    print()

print("-------------")
print("Equals:", a[0] == a[2] and a[1] == a[3])
