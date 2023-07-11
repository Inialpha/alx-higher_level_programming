#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics"""


import sys
status_codes = {'200': 0, '301': 0,
                '400': 0, '401': 0,
                '403': 0, '404': 0,
                '405': 0, '500': 0}
i = 0
f_size = 0
try:
    for line in sys.stdin:
        token = line.split()
        if len(token) >= 2:
            a = i
            if token[-2] in status_codes:
                status_codes[token[-2]] += 1
                i += 1
            try:
                f_size += int(token[-1])
                if a == i:
                    i += 1
            except FileNotFoundError:
                if a == i:
                    continue
            if i % 10 == 0:
                print("file size: {:d}".format(f_size))
                for key, value in sorted(status_codes.items()):
                    if value:
                        print("{:s}: {:d}".format(key, value))
    print("file size: {:d}".format(f_size))
    for key, value in sorted(status_codes.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("file size: {:d}".format(f_size), flush=True)
    for key, value in sorted(status_codes.items()):
        if value:
            print("{:s}: {:d}".format(key, value), flush=True)
