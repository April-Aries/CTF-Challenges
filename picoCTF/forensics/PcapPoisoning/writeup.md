# PcapPoisoning

| Information | Description |
| :-- | :-- |
| Category | Forensics |
| Difficulty | Medium |

## Problem Description

How about some hide and seek heh? Download this [file](https://artifacts.picoctf.net/c/377/trace.pcap) and find the flag.

## Solution

### Approach 1: `strings`

Using `strings` is able to find the flag.

```bash=
$ strings trace.pcap | grep pico
```

### Approach 2: wireshark filter

The other approach is using wireshark to open the pcap file. Instead of manually searching for the flag, I use the filter to achieve the result. Type `tcp contains "pico"` in the filter bar and I get the flag.

:triangular_flag_on_post:: `picoCTF{P64P_4N4L7S1S_SU55355FUL_31010c46}`
