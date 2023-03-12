#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import os
import initiingizer
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("use correct command: python3 build_android NDK_PATH")
    else:
        ndk_path = sys.argv[1]
        if not os.path.exists(ndk_path):
            print(ndk_path + " is not correct NDK_PATH.")
        else:
            initiingizer.do_init()
            root_dir = os.path.dirname(__file__)
            os.chdir("skia")
            print("--------------------ARM START--------------------")
            os.system("bin/gn gen out/arm --args=\'ndk=\"" + ndk_path + "\" target_cpu=\"arm\"\'")
            os.system("ninja -C out/arm")
            print("--------------------ARM END--------------------")
            print("--------------------ARM64 START--------------------")
            os.system("bin/gn gen out/arm64 --args=\'ndk=\"" + ndk_path + "\" target_cpu=\"arm64\"\'")
            os.system("ninja -C out/arm64")
            print("--------------------ARM64 END--------------------")
            print("--------------------x64 START--------------------")
            os.system("bin/gn gen out/x64 --args=\'ndk=\"" + ndk_path + "\" target_cpu=\"x64\"\'")
            os.system("ninja -C out/x64")
            print("--------------------x64 END--------------------")
            print("--------------------x86 START--------------------")
            os.system("bin/gn gen out/x86 --args=\'ndk=\"" + ndk_path + "\" target_cpu=\"x86\"\'")
            os.system("ninja -C out/x86")
            print("--------------------x86 END--------------------")
