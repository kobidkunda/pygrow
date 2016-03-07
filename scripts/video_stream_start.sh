#!/bin/sh

# nohup raspivid -t -0 -w 1280 -h 720 -fps 25 -b 2000000 -o - | ffmpeg -i - -vcodec copy -an -f flv -metadata streamName=PyGrowStream tcp://0.0.0.0:7777

raspivid -t -0 -w 1280 -h 720 -fps 25 -b 2000000 -o - | ffmpeg -i - -vcodec copy -an -f flv -metadata streamName=PyGrowStream tcp://0.0.0.0:7777
