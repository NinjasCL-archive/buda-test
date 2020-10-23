#!/usr/bin/env python3

from hashlib import sha256
from uuid import uuid4

needle = "b00da"

found = False
while not found:
    candidate = str(uuid4()).encode()
    haystack = sha256(candidate).hexdigest()
    found = needle in haystack

print(candidate, haystack)
