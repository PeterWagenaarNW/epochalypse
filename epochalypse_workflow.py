#!/usr/bin/env python2
# encoding: utf-8

import os
import sys

# Workflow3 supports Alfred 3's new features. The `Workflow` class
# is also compatible with Alfred 2.
from workflow import Workflow3

from datetime import datetime

# The number of seconds between January 1, 1904 and Jan 1, 1970.
HFS_OFFSET = 2082844800

# The number of seconds between January 1, 1970 and January 1, 2001.
# Apple Safari also uses Cocoa timestamp
COCOA_OFFSET = 978307200

# The difference between Jan 1, 1601 and Jan 1, 1970 in micro seconds
# WebKit timestamp is used by Google Chrome and Opera
WEBKIT_OFFSET = 11644473600 * 1000000

# The difference between Jan 1, 1601 and Jan 1, 1970 in 100 nano seconds
NTFS_OFFSET = 11644473600 * 10000000

# The difference between Jan 1, 1980 and Jan 1, 1970 in seconds.
FAT_OFFSET = 315532800

# No offset calculation needed for APFS, as represent the number of nano
# second since January 1, 1970 (same as standard Unix epoch)

# No offset calculation needed for FireFox timestamp, as represent the number
# of microseconds since January 1, 1970 (same as standard Unix epoch)

def from_epoch(epoch):
    results = []
    try:
        results.append(('Unix', datetime.utcfromtimestamp(epoch).isoformat(" ") + ' UTC'))
    except:
        results.append(('Unix', '-'))

    try:
        results.append(('COCOA', datetime.utcfromtimestamp(epoch + COCOA_OFFSET).isoformat(" ") + ' UTC'))
    except:
        results.append(('COCOA', '-'))

    try:
        results.append(('FAT', datetime.utcfromtimestamp(epoch + FAT_OFFSET).isoformat(" ") + ' UTC'))
    except:
        results.append(('FAT', '-'))

    try:
        results.append(('HFS+', datetime.utcfromtimestamp(epoch - HFS_OFFSET).isoformat(" ") + ' UTC'))
    except:
        results.append(('HFS+', '-'))

    try:
        # Webkit timestamp calculation
        wk = datetime.utcfromtimestamp(float(epoch - WEBKIT_OFFSET) / 1000000)
        results.append(('WebKit', wk.isoformat(" ") + ' UTC'))
    except:
        results.append(('WebKit', '-'))

    try:
        # ntfs time calculation
        ntfs = datetime.utcfromtimestamp(float(epoch - NTFS_OFFSET) / 10000000)
        results.append(('NTFS', ntfs.isoformat(" ") + ' UTC'))
    except:
        results.append(('NTFS'))
    try:
        # new APFS time calculation
        apfs = datetime.utcfromtimestamp(float(epoch) / 1000000000)
        results.append(('APFS', apfs.isoformat(" ") + ' UTC'))
    except:
        results.append(('APFS'))
    try:
        # Firefox timestamp, number of microseconds since January 1, 1970 UTC
        ff = datetime.utcfromtimestamp(float(epoch) / 1000000)
        results.append(('FireFox', ff.isoformat(" ") + ' UTC'))
    except:
        results.append(('FireFox'))
    return results

def main(wf):
    # The Workflow3 instance will be passed to the function
    # you call from `Workflow3.run`.
    # Not super useful, as the `wf` object created in
    # the `if __name__ ...` clause below is global...
    #
    # Your imports go here if you want to catch import errors, which
    # is not a bad idea, or if the modules/packages are in a directory
    # added via `Workflow3(libraries=...)`

    # Get args from Workflow3, already in normalized Unicode.
    # This is also necessary for "magic" arguments to work.

    icon = os.path.join(os.path.dirname(__file__), 'clock.png')
    args = wf.args
    for a in args:
        try:
            epoch = float(a)
            r = from_epoch(epoch)
            for t, ts in r:
                # def add_item(self, title, subtitle='', arg=None, autocomplete=None,
                #              valid=False, uid=None, icon=None, icontype=None, type=None,
                #              largetext=None, copytext=None, quicklookurl=None, match=None):
                wf.add_item(title=t, subtitle=ts, arg=ts, valid=True, icon=icon)
        except ValueError:
            pass
        

    # Send output to Alfred. You can only call this once.
    # Well, you *can* call it multiple times, but subsequent calls
    # are ignored (otherwise the JSON sent to Alfred would be invalid).
    wf.send_feedback()


if __name__ == '__main__':
    # Create a global `Workflow3` object
    wf = Workflow3()
    # Call your entry function via `Workflow3.run()` to enable its
    # helper functions, like exception catching, ARGV normalization,
    # magic arguments etc.
    sys.exit(wf.run(main))

