#!/usr/local/bin/python3
# -*- coding:utf-8 -*-
import os
import initiingizer

if __name__ == "__main__":
    initiingizer.do_init()
    root_dir = os.path.dirname(__file__)
    os.chdir("skia")

    IS_OFFICIAL_BUILD="true"
    IS_DEBUG="false"
    FORCE_TRACING="false"
    PROFILE_BUILD="false"
    ENABLE_GPU="true"
    ENABLE_WEBGL="true"
    ENABLE_WEBGPU="false"
    SERIALIZE_SKP="false"
    DESERIALIZE_EFFECTS="true"
    ENABLE_SKOTTIE="false"
    INCLUDE_VIEWER="false"
    USE_EXPAT="false"
    ENABLE_PARTICLES="false"
    ENABLE_PATHOPS="true"
    ENABLE_RT_SHADER="true"
    ENABLE_SKSL_TRACE="false"
    ENABLE_MATRIX="true"
    ENABLE_CANVAS="true"
    GN_FONT="skia_enable_fontmgr_custom_directory=false "
    WOFF2_FONT="skia_use_freetype_woff2=true"
    ENABLE_FONT="true"
    ENABLE_EMBEDDED_FONT="true"
    TO_GENERATE_EMBEDDED_FONT = True
    # if ENABLE_EMBEDDED_FONT you need to compile your project with generated cpp file: skia/src/fonts/NotoMono-Regular.ttf.cpp
    if TO_GENERATE_EMBEDDED_FONT:
        if not os.path.exists("src/fonts/NotoMono-Regular.ttf.cpp"):
            os.system("python tools/embed_resources.py --name SK_EMBEDDED_FONTS --input modules/canvaskit/fonts/NotoMono-Regular.ttf --output src/fonts/NotoMono-Regular.ttf.cpp")
    else:
        if os.path.exists("src/fonts/NotoMono-Regular.ttf.cpp"):
            os.remove("src/fonts/NotoMono-Regular.ttf.cpp")
    ###### no_font + no_embedded_font
    # GN_FONT+="skia_enable_fontmgr_custom_embedded=false skia_enable_fontmgr_custom_empty=false "
    # GN_FONT+="skia_fontmgr_factory=\":fontmgr_empty_factory\""
    ##### no_embedded_font
    # GN_FONT+="skia_enable_fontmgr_custom_embedded=false skia_enable_fontmgr_custom_empty=false "
    # GN_FONT+="skia_fontmgr_factory=\":fontmgr_empty_factory\""
    ###### font + embedded_font
    GN_FONT+="skia_enable_fontmgr_custom_embedded=true skia_enable_fontmgr_custom_empty=false "
    GN_FONT+="skia_fontmgr_factory=\":fontmgr_custom_embedded_factory\""
    ENABLE_ALIAS_FONT="true"
    LEGACY_DRAW_VERTICES="false"
    DEBUGGER_ENABLED="false"
    GN_SHAPER="skia_use_icu=true skia_use_client_icu=false skia_use_system_icu=false skia_use_harfbuzz=true skia_use_system_harfbuzz=false"
    ENABLE_PARAGRAPH="true"
    DO_DECODE="false"
    ENCODE_PNG="false"
    ENCODE_JPEG="false"
    ENCODE_WEBP="false"

    command_list = "bin/gn gen out/web --args=\'";
    command_list += ("is_official_build=" + IS_OFFICIAL_BUILD)
    command_list += (" is_debug=" + IS_DEBUG)
    command_list += " is_component_build=false"
    command_list += " werror=true"
    command_list += " target_cpu=\"wasm\""
    command_list += " skia_use_angle=false"
    command_list += " skia_use_dng_sdk=false"
    command_list += (" skia_use_dawn=" + ENABLE_WEBGPU)
    command_list += (" skia_use_webgl=" + ENABLE_WEBGL)
    command_list += (" skia_use_webgpu=" + ENABLE_WEBGPU)
    command_list += (" skia_use_expat=" + USE_EXPAT)
    command_list += " skia_use_fontconfig=false"
    command_list += " skia_use_freetype=true"
    command_list += " skia_use_libheif=false"
    command_list += (" skia_use_libjpeg_turbo_decode=" + DO_DECODE)
    command_list += (" skia_use_libjpeg_turbo_encode=" + ENCODE_JPEG)
    command_list += (" skia_use_libpng_decode=" + DO_DECODE)
    command_list += (" skia_use_libpng_encode=" + ENCODE_PNG)
    command_list += (" skia_use_libwebp_decode=" + DO_DECODE)
    command_list += (" skia_use_libwebp_encode=" + ENCODE_WEBP)
    command_list += " skia_use_lua=false"
    command_list += " skia_use_piex=false"
    command_list += " skia_use_system_freetype2=false"
    command_list += " skia_use_system_libjpeg_turbo=false"
    command_list += " skia_use_system_libpng=false"
    command_list += " skia_use_system_libwebp=false"
    command_list += " skia_use_system_zlib=false"
    command_list += " skia_use_vulkan=false"
    command_list += " skia_use_wuffs=true"
    command_list += " skia_use_zlib=true"
    command_list += (" skia_enable_gpu=" + ENABLE_GPU)
    command_list += (" skia_build_for_debugger=" + DEBUGGER_ENABLED)
    command_list += (" skia_enable_sksl_tracing=" + ENABLE_SKSL_TRACE)
    command_list += (" " + GN_SHAPER)
    command_list += (" " + GN_FONT)
    command_list += (" " + WOFF2_FONT)
    command_list += " skia_enable_skshaper=true"
    command_list += " skia_enable_skparagraph=true"
    command_list += " skia_enable_pdf=false"
    command_list += (" skia_canvaskit_force_tracing=" + FORCE_TRACING)
    command_list += (" skia_canvaskit_profile_build=" + PROFILE_BUILD)
    command_list += (" skia_canvaskit_enable_skp_serialization=" + SERIALIZE_SKP)
    command_list += (" skia_canvaskit_enable_effects_deserialization=" + DESERIALIZE_EFFECTS)
    command_list += (" skia_canvaskit_enable_skottie=" + ENABLE_SKOTTIE)
    command_list += (" skia_canvaskit_include_viewer=" + INCLUDE_VIEWER)
    command_list += (" skia_canvaskit_enable_particles=" + ENABLE_PARTICLES)
    command_list += (" skia_canvaskit_enable_pathops=" + ENABLE_PATHOPS)
    command_list += (" skia_canvaskit_enable_rt_shader=" + ENABLE_RT_SHADER)
    command_list += (" skia_canvaskit_enable_matrix_helper=" + ENABLE_MATRIX)
    command_list += (" skia_canvaskit_enable_canvas_bindings=" + ENABLE_CANVAS)
    command_list += (" skia_canvaskit_enable_font=" + ENABLE_FONT)
    command_list += (" skia_canvaskit_enable_embedded_font=" + ENABLE_EMBEDDED_FONT)
    command_list += (" skia_canvaskit_enable_alias_font=" + ENABLE_ALIAS_FONT)
    command_list += (" skia_canvaskit_legacy_draw_vertices_blend_mode=" + LEGACY_DRAW_VERTICES)
    command_list += (" skia_canvaskit_enable_debugger=" + DEBUGGER_ENABLED)
    command_list += (" skia_canvaskit_enable_paragraph=" + ENABLE_PARAGRAPH)
    command_list += (" skia_canvaskit_enable_webgl=" + ENABLE_WEBGL)
    command_list += (" skia_canvaskit_enable_webgpu=" + ENABLE_WEBGPU)
    command_list += "\'"
    os.system(command_list)
    os.system("ninja -C out/web")
    if os.path.exists("out/web/libskia.a"):
        print("------------------------------ Web Build Success ------------------------------")
        print(root_dir + "/skia/out/web")
    else:
        print("------------------------------ Web Build Failed ------------------------------")
