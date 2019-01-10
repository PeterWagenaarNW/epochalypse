# Epochalypse
There is the standard, official Epoch time (the Unix/POSIX one, seconds elapsed since 1 Jan 1970), and there are "other epoch" type of time (because, why not?). Epochalypse is a python script that receives a generic timestamp as input and converts it in several known common formats. In the latest version it supports also timestamps in hexadecimal value as input.
Sample output and currently supported formats below:
```
$ python3 epochalypse.py --help
usage: epochalypse.py [-h] [-e] [-x]

optional arguments:
  -h, --help     show this help message and exit
  -e , --epoch   Epoch time to be converted
  -x , --hex     Hexadecimal timemstamp value to be converted


$ python3 epochalypse.py -e 547120509.243697

Epoch Time input to be converted: 547120509.243697
Unix:    1987-05-04 09:55:09.243697 UTC
COCOA:   2018-05-04 09:55:09.243697 UTC
FAT:     1997-05-03 09:55:09.243697 UTC
HFS+:    1921-05-03 09:55:09.243697 UTC
WebKit:  1601-01-01 00:09:07.120510 UTC
NTFS:    1601-01-01 00:00:54.712051 UTC
APFS:    1970-01-01 00:00:00.547121 UTC
FireFox: 1970-01-01 00:09:07.120509 UTC
```

This repository contains the original script created by pstirparo and an adaptation created by yours truly for use in Alfred App for OSX. The workflow requires https://github.com/deanishe/alfred-workflow/tree/master/workflow to be available, for instance by symlinking this directory directly in the directory containing the workflow.
