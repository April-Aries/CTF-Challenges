# HideToSee

| Information | Description |
| :-- | :-- |
| Category | Crypto |
| Difficulty | Medium |

# Problem Description

How about some hide and seek heh?
Look at this image [here](https://artifacts.picoctf.net/c/237/atbash.jpg).

> Hint: Download the image and try to extract it.

# Solution

I learn a new tool **steghide** in this problem! To learn more about this tool, I push a [post](https://april-aries.github.io/zh_TW/blog/steghide/) about it.

To get more information about this image, I use `steghide --info atbash.jpg`

```bash=
$ steghide --info atbash.jpg
"atbash.jpg":
  format: jpeg
  capacity: 2.4 KB
Try to get information about embedded data ? (y/n) y
Enter passphrase: 
  embedded file "encrypted.txt":
    size: 31.0 Byte
    encrypted: rijndael-128, cbc
    compressed: yes
```

It seems there is an embedded file *encrypted.txt*. After extracting it, I could get the ciphertext. Use command `steghide extract -sf atbash.jpg`. `steghide` will write the extracted data to a file.

```bash=
$ steghide extract -sf atbash.jpg
Enter passphrase: 
wrote extracted data to "encrypted.txt".
```

Well... I reckon it's tricky to guess the passphrase is nothing. Simply press enter and it pass.

The ciphertext is "krxlXGU{zgyzhs_xizxp_05y2z65z}". Perhaps it's time to use **asbash**. Atbash cipher, or mirror code, is a encode method that swap the first k letter with the last k letter. For instance, `a` is `z`, `b` is `y`, etc. Simply use an online decoder is efficient to find the flag.

:triangular_flag_on_post:: `picoCTF{atbash_crack_05b2a65a}`
