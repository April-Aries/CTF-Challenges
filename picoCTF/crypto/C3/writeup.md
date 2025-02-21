# C3

| Information | Description |
| :-- | :-- |
| Category | Crypto |
| Difficulty | Medium |

# Problem Description

This is the Custom Cyclical Cipher!
Download the ciphertext [here](https://artifacts.picoctf.net/c_titan/47/ciphertext).
Download the encoder [here](https://artifacts.picoctf.net/c_titan/47/convert.py).
Enclose the flag in our wrapper for submission. If the flag was "example" you would submit "picoCTF{example}".

> Hint: Modern crypto schemes don't depend on the encoder to be secret, but this one does.

# Solution

*converter.py* is the encoder that encode the flag to ciphertext. To recover the flag, I design a decoder *exp.py*. Let's dive into the mechanism of the encoder first.

For each character in flag, the encoder will first look up the index of such character and store it as `cur`. Then it looks up the element of `lookup2` with index `(cur - prev) % 40`. The purpose of `%40` is to limit the range of the index from 0 to 39, which fits the array `lookup2`. Such element is the corresponding ciphertext of flag. Finally, it sets `cur` as new `prev`.

To decode such ciphertext, I begin from the first character since I know the first convertion is under situation that `prev` is `0`. I iterate through all characters in `ciphertext`, getting the value of `out` in *converter.py* as `tmp` in *exp.py*. `cur` should be `tmp + prev` and thus I know the corresponding plaintext is `lookup1[cur]`. To keep the next round, setting `prev` to `cur` is important.

Eveything goes good and I execute the decoder with given ciphertext. Guess what! I saw a python script as output. I was so stupid that I consider the script as what I wrote and wondering "Why the python script cannot be executed and viewed as pure ASCII text file for my Kali". Well... I get hint from others' writeups. The output is indeed another python2 script (`hidden.py`). Don't give up and the flag is reachable.

Ultimately, I slightly modify the python2 script into python3 script, execute the script with input itself, and get the flag `adlib` in the end.

Remember to encapsulate the flag with "picoCTF{}".

:triangular_flag_on_post:: `picoCTF{adlib}`
