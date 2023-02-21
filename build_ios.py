#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import os
import initiingizer

if __name__ == "__main__":
    initiingizer.do_init()
    root_dir = os.path.dirname(__file__)
    os.chdir("skia")
    # intel
    os.system("bin/gn gen out/mac_intel")
    os.system("ninja -C out/mac_intel")
