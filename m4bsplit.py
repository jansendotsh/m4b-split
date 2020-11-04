#!/usr/bin/python3

import sys, re, ffmpeg

try:
    filename = sys.argv[1]
    bookFile = ffmpeg.input(filename)
    metaDict = ffmpeg.probe(filename,show_chapters=None)
except IndexError:
    print("File name missing, must have file name passed as argument")
    sys.exit(1)

for i in range(0,len(metaDict['chapters']),1):
    chapTitle = metaDict['chapters'][i]['tags']['title']
    chapTitle = re.sub("['-]", "", chapTitle)
    startTime = metaDict['chapters'][i]['start_time']
    endTime = metaDict['chapters'][i]['end_time']
    chapNum = metaDict['chapters'][i]['id'] + 1

    trackName = "{} {}.mp3".format(chapNum, chapTitle)

    outbound = ffmpeg.output(bookFile,trackName,ss=startTime,to=endTime,map_chapters="-1")
    ffmpeg.run(outbound)
