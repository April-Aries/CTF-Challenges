# st3g0

| Information | Description |
| :-- | :-- |
| Category | Forensics |
| Difficulty | Medium |

## Problem Description

Download this [image](https://artifacts.picoctf.net/c/217/pico.flag.png) and find the flag.

> Hint: We know the end sequence of the message will be `$t3g0`.

## Solution

It's a steganography problem that hides the flag in the picture `pico.flag.png`. In this problem, I will use a tool to find the hidden message.

`zsteg` is a tool developed by Ruby. It is able to detect hidden messages in PNG or BMP file.  If you want to learn more about this tool, you may refer to [this post](https://april-aries.github.io/zh_TW/blog/zsteg).

To install `zsteg`, run the following commands.

```bash=
$ sudo apt install ruby
$ sudo gem install zsteg
```

Then you have the tool to use. To extract the hidden message inside the image file, simply run the following command.

```bash=
$ zsteg pico.flag.png 
b1,r,lsb,xy         .. text: "~__B>VG?G@"
b1,rgb,lsb,xy       .. text: "picoCTF{7h3r3_15_n0_5p00n_a9a181eb}$t3g0"
b1,abgr,lsb,xy      .. text: "E2A5q4E%uSA"
b2,b,lsb,xy         .. text: "AAPAAQTAAA"
b2,b,msb,xy         .. text: "HWUUUUUU"
b3,r,lsb,xy         .. file: gfxboot compiled html help file
b4,r,lsb,xy         .. file: Targa image data (16-273) 65536 x 4097 x 1 +4352 +4369 - 1-bit alpha - right "\021\020\001\001\021\021\001\001\021\021\001"
b4,g,lsb,xy         .. file: 0420 Alliant virtual executable not stripped
b4,b,lsb,xy         .. file: Targa image data - Map 272 x 17 x 16 +257 +272 - 1-bit alpha "\020\001\021\001\021\020\020\001\020\001\020\001"
b4,bgr,lsb,xy       .. file: Targa image data - Map 273 x 272 x 16 +1 +4113 - 1-bit alpha "\020\001\001\001"
b4,rgba,msb,xy      .. file: Applesoft BASIC program data, first line number 8
```

:triangular_flag_on_post:: `picoCTF{7h3r3_15_n0_5p00n_a9a181eb}`

## Reference

- [Day20 Forensics 工欲善其事，必先利其器](https://ithelp.ithome.com.tw/articles/10224456)
