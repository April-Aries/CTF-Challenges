#!/bin/sh

exiftool \
    -DateTimeOriginal="1970:01:01 00:00:00" \
    -TimeStamp="1970:01:01 00:00:00.001+00:00" \
    -SubSecDateTimeOriginal="1970:01:01 00:00:00.001" \
    -ModifyDate="1970:01:01 00:00:00" \
    -CreateDate="1970:01:01 00:00:00" \
    -SubSecCreateDate="1970:01:01 00:00:00.001" \
    -SubSecModifyDate="1970:01:01 00:00:00.001" \
    original.jpg
