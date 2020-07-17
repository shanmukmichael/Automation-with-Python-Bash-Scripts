#!/usr/bin/env python3
import os
import subprocess
import sys

logfile = sys.argv[1]
usernames = {}
if os.path.isfile(logfile) or os.path.exists(logfile):
    with open(logfile) as f:
        for line in f:
            if "shanmuk" not in line:
                continue
            pattern = r"USER \((\w+)\)$"
            result = re.search(pattern, line)
            if result is None:
                continue
            name = result[1]
            usernames[name] = usernames.get(name, 0) + 1
    print(usernames)
else:
    print("File not Found....")
