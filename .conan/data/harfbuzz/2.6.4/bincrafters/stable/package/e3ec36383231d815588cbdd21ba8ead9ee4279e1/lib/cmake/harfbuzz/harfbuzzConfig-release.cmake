#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "harfbuzz::harfbuzz" for configuration "Release"
set_property(TARGET harfbuzz::harfbuzz APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(harfbuzz::harfbuzz PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "freetype;gio-2.0;gmodule-2.0;gobject-2.0;gthread-2.0;glib-2.0;png16;m;ffi;pcreposix;pcre;elf;mount;blkid;selinux;sepol;pcre2-posix;pcre2-8;pcre2-16;pcre2-32;z;bz2;pthread;resolv;dl;/home/conan/.conan/data/freetype/2.10.1/_/_/package/3cdd93cd46fc07735d1b0d7f2860a82fac7a3053/lib/libfreetype.a;/home/conan/.conan/data/glib/2.64.0/bincrafters/stable/package/f328e8721181dbb381ed842e289123010efd816c/lib/libglib-2.0.so"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libharfbuzz.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS harfbuzz::harfbuzz )
list(APPEND _IMPORT_CHECK_FILES_FOR_harfbuzz::harfbuzz "${_IMPORT_PREFIX}/lib/libharfbuzz.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
