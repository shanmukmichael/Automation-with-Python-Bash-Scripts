#!/usr/bin/env python3
import shutil
import psutil


def check_disk_usage(disk):
    do = shutil.disk_usage(disk)
    free = do.free / do.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_disk_usage("/") or not check_cpu_usage():
    print("E R R O R !!!")
print("Every thing OK!")
