#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import os
import sys
import platform

def do_init():
    print("--------------------INIT DEPS START--------------------")
    root_dir = os.path.dirname(__file__)
    os.system("git submodule init")
    os.system("git submodule update --progress")
    os.environ["PATH"] += (os.pathsep + root_dir + "/depot_tools")
    print(os.environ["PATH"])
    if platform.system().lower() == 'darwin':
        os.system("brew install bazelisk")
    os.chdir("skia")
    os.system("python3 tools/git-sync-deps")
    os.system("bin/fetch-ninja")
    # emsdk 3.1.15
    os.environ["PATH"] += (os.pathsep + root_dir + "/skia/third_party/externals/emsdk")
    os.environ["PATH"] += (os.pathsep + root_dir + "/skia/third_party/externals/emsdk/upstream/emscripten")
    os.environ["PATH"] += (os.pathsep + root_dir + "/skia/third_party/externals/emsdk/node/14.18.2_64bit/bin")
    os.environ["EMSDK"] = root_dir + "/skia/third_party/externals/emsdk"
    os.environ["EM_CONFIG"] = root_dir + "/skia/third_party/externals/emsdk/.emscripten"
    os.environ["EMSDK_NODE"] = root_dir + "/skia/third_party/externals/emsdk/node/14.18.2_64bit/bin/node"
    os.environ["EMSDK_PYTHON"] = root_dir + "/skia/third_party/externals/emsdk/python/3.9.2_64bit/bin/python3"
    os.environ["SSL_CERT_FILE"] = root_dir + "/skia/third_party/externals/emsdk/python/3.9.2_64bit/lib/python3.9/site-packages/certifi/cacert.pem"
    # NDK
    # print(platform.system())
    # if not os.path.exists(root_dir + "/ndk"):
    #     os.system("./bin/fetch-sk")
    #     if platform.system().lower() == 'windows':
    #         os.system("./bin/sk.exe asset download android_ndk_windows " + root_dir + "/ndk");
    #     elif platform.system().lower() == 'linux':
    #         os.system("./bin/sk asset download android_ndk_linux " + root_dir + "/ndk");
    #     else:
    #         os.system("./bin/sk asset download android_ndk_darwin " + root_dir + "/ndk");
    os.chdir(root_dir)
    print("--------------------INIT DEPS END--------------------")
