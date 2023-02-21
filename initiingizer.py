#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import os
import sys

def do_init():
    print("--------------------INIT DEPS START--------------------")
    root_dir = os.path.dirname(__file__)
    os.system("git submodule init")
    os.system("git submodule update --progress")
    os.environ["PATH"] += (os.pathsep + root_dir + "/depot_tools")
    print(os.environ["PATH"])
    os.system("brew install bazelisk")
    os.chdir("skia")
    os.system("python3 tools/git-sync-deps")
    os.system("bin/fetch-ninja")
    # emsdk 3.1.15
    os.chdir(root_dir)
    print("--------------------INIT DEPS END--------------------")
