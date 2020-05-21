#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "harfbuzz::harfbuzz" for configuration "Release"
set_property(TARGET harfbuzz::harfbuzz APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(harfbuzz::harfbuzz PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "freetype;gio-2.0;gmodule-2.0;gobject-2.0;gthread-2.0;glib-2.0;png16;ffi;pcreposix;pcre;elf;gnuintl;z;bz2;iconv;iconv;resolv;/Applications/Xcode-11.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk/System/Library/Frameworks/Foundation.framework;/Applications/Xcode-11.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk/System/Library/Frameworks/CoreServices.framework;/Applications/Xcode-11.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk/System/Library/Frameworks/CoreFoundation.framework;/Users/travis/.conan/data/freetype/2.10.1/_/_/package/9fbc622fdb9d2462147cf446a56b1688bf016d05/lib/libfreetype.a;/Users/travis/.conan/data/glib/2.64.0/bincrafters/stable/package/2f35ff713084d1b9a9452ef9ed236a58748ab45c/lib/libglib-2.0.dylib;/Applications/Xcode-11.4.app/Contents/Developer/Platforms/MacOSX.platform/Developer/SDKs/MacOSX10.15.sdk/System/Library/Frameworks/ApplicationServices.framework"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libharfbuzz.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS harfbuzz::harfbuzz )
list(APPEND _IMPORT_CHECK_FILES_FOR_harfbuzz::harfbuzz "${_IMPORT_PREFIX}/lib/libharfbuzz.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
