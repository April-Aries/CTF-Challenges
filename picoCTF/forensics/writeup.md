# Writeups

> Writeup for forensics in picoCTF

# Blast from the past

> Difficulty: Medium

## Problem Description

The judge for these pictures is a real fan of antiques. Can you age this photo to the specifications? Set the timestamps on this picture to `1970:01:01 00:00:00.001+00:00` with as much precision as possible for each timestamp. In this example, `+00:00` is a timezone adjustment. Any timezone is acceptable as long as the time is equivalent. As an example, this timestamp is acceptable as well: `1969:12:31 19:00:00.001-05:00`. For timestamps without a timezone adjustment, put them in GMT time (`+00:00`). The checker program provides the timestamp needed for each. Use this picture (`./BlastFromThePast/original.jpg`)

- Submit your modified picture here: `nc -w 2 mimas.picoctf.net 51429 < modified.jpg`
- Check your modified picture here: `nc mimas.picoctf.net 50644`

> Hint: **Exiftool** is really good at reading metadata, but you might want to use something else to modify it.

## Solution

First, I use **Exiftool** to get some information about the picture. `exiftool -s -g original.jpg` shows the information in short and categrized in groups. Additionally, I use `exiftool -s -g original.jpg | grep "Time"` and `exiftool -s -g riginal.jpg | grep "Date"` to spot the time information.

Result I get is as below.

```sh
# `exiftool -s -g original.jpg | grep "Date"`
FileModifyDate                  : 2025:01:22 05:29:42-05:00
FileAccessDate                  : 2025:01:22 05:29:35-05:00
FileInodeChangeDate             : 2025:01:22 05:30:01-05:00
ModifyDate                      : 2023:11:20 15:46:23
DateTimeOriginal                : 2023:11:20 15:46:23
CreateDate                      : 2023:11:20 15:46:23
SubSecCreateDate                : 2023:11:20 15:46:23.703
SubSecDateTimeOriginal          : 2023:11:20 15:46:23.703
SubSecModifyDate                : 2023:11:20 15:46:23.703

# `exiftool -s -g original.jpg | grep "Time"`
ExposureTime                    : 1/24
DateTimeOriginal                : 2023:11:20 15:46:23
SubSecTime                      : 703
SubSecTimeOriginal              : 703
SubSecTimeDigitized             : 703
TimeStamp                       : 2023:11:20 15:46:21.420-05:00
SubSecDateTimeOriginal          : 2023:11:20 15:46:23.703
```

After combining both results while removing away unnecessary information. I write a shell script `./BlastFromThePast/exp.sh` to modify `original.jpg`. A warning raised after execution, "Warning: Not an integer for XMP-apple-fi:TimeStamp". This points out the issue when modifying the "TimeStamp" field. This is sue to a propietary format used by samsung and it seems no tools are able to change it. Exiftool documentation also states that this property cannot be modified. Well... It's time to take out the ancient tool **ghex**! Yes. I try to modify the timestamp directly through a hex editor.

To find where the time stamp is, we can use tool like [Unix Time Stamp Converter](https://www.unixtimestamp.com/). The given time stamp is `2023:11:20 20:46:21.420+00:00`, which is equal to `1700513181420` in millisecond. Such string appears near the bottom of the whole file. Changing those 13 bytes leads me to the flag. The last problem is, what is the millisecond time stamp of `1970:00:00 00:00:00.001+00:00`. Actually it is `0000000000001`. Submit the modified image `./BlastFromThePast/modified.jpg` and get the flag after passing the check.

The flag is : `picoCTF{71m3_7r4v311ng_p1c7ur3_ed953b57}`

## Note

The checker checks 7 fields of the image time information, `ModifyDate`, `DateTimeOriginal`, `CreateDate`, `SubSecCreateDate`, `SubSecDateTimeOriginal`, `SubSecModifyDate`, and `TimeStamp`.

## Reference

- [PicoCTF 2024: Forensics Writeup](https://fireynacho.medium.com/picoctf-2024-forensics-writeup-8ef6265a049b)
