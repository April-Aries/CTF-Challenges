# Mob Psycho 

| Information | Description |
| :-- | :-- |
| Category | Forensics |
| Difficulty | Medium |

## Problem Description

Can you handle APKs? Download the android apk [here](https://artifacts.picoctf.net/c_titan/52/mobpsycho.apk).

> Hint 1: Did you know you can `unzip` APK files?
> Hint 2: Now you have the whole host of shell tools for searching these files.

## Solution

The problem gives a APK file, which is a middleware used by Android operating system. An APK file is also a ZIP archive. Command `unzip` is available to decompress thus whole host of shell tools for searching these files.

Use command `file` to check its file type. It indicates that an APK is basically a zip archive data.
```bash=
$ file mobpsycho.apk
mobpsycho.apk: Zip archive data, at least v1.0 to extract, compression method=store
```

As always, I use `strings` to see if flag is searchable through this method.

```bash=
$ strings mobpsycho.apk| grep pico

$ strings mobpsycho.apk| grep flag
res/color/flag.txtUT
res/color/flag.txtUT
```

It seems there is a file called *flag.txt* under *res/color*. Let's decompress the APK file and try to get the *flag.txt*

```bash=
$ unzip -d mobpsycho mobpsycho.apk 
Archive:  mobpsycho.apk
   creating: mobpsycho/res/
   creating: mobpsycho/res/anim/
  inflating: mobpsycho/res/anim/abc_fade_in.xml  
  ...

$ cd ./mobpsycho/res/color
$ cat flag.txt
7069636f4354467b6178386d433052553676655f4e5838356c346178386d436c5f38356462643231357d
```

Yes I do get the flag, but I need more operations on it. The flag is encoded as hexadecimal in ASCII. I use `xxd` commands to transform them back to ASCII.

```bash=
$ cat flag.txt | xxd -r -p
picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_85dbd215}
```

`xxd` command makes a hexdump or do the reverse. In this task, I'm attempting to do the reverse (from hex to ASCII). `-r` argument tells `xxd` to "do the reverse". `-p` argument tells `xxd` to print the outcome in plaintext.

:triangular_flag_on_post:: `picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_85dbd215}`

## Reference

- [APK wiki](https://zh.wikipedia.org/zh-tw/APK)
