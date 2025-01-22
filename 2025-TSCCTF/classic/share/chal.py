import os
import string
import secrets

flag = os.getenv("FLAG") or "TSC{test_flag}"

charset = string.digits + string.ascii_letters + string.punctuation
A, B = secrets.randbelow(2**32), secrets.randbelow(2**32)
assert len(set((A * x + B) % len(charset) for x in range(len(charset)))) == len(charset)

enc = "".join(charset[(charset.find(c) * A + B) % len(charset)] for c in flag)
print(enc)
