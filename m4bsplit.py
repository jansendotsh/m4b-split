#!/usr/bin/python3

import sys, ffmpeg

filename = sys.argv[1]
bookFile = ffmpeg.input(filename)

metaDict = ffmpeg.probe(filename,show_chapters=None)

for i in range(0,len(metaDict['chapters']),1):
    chapTitle = metaDict['chapters'][i]['tags']['title']
    startTime = metaDict['chapters'][i]['start_time']
    endTime = metaDict['chapters'][i]['end_time']
    chapNum = metaDict['chapters'][i]['id'] + 1

    trackName = "{} {}.mp3".format(chapNum, chapTitle)

    outbound = ffmpeg.output(bookFile,trackName,ss=startTime,to=endTime)
    ffmpeg.run(outbound)
