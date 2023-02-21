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
    if os.path.exists("out/mac_intel/libskia.a"):
        print("------------------------------ Mac Intel Build Success ------------------------------")
        print(root_dir + "/skia/out/mac_intel")
    else:
        print("------------------------------ Mac Intel Build Failed ------------------------------")
