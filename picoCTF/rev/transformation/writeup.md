# Transformation

| Information | Description |
| :-- | :-- |
| Category | Reverse |
| Difficulty | Easy |

# Problem Description

I wonder what this really is... `enc`
`''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])`

# Solution

I wrote a python script `exp.py` to decode the encoded flag.
