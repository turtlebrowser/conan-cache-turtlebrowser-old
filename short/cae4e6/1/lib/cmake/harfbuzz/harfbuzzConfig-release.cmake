#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "harfbuzz::harfbuzz" for configuration "Release"
set_property(TARGET harfbuzz::harfbuzz APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(harfbuzz::harfbuzz PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LINK_INTERFACE_LIBRARIES_RELEASE "freetype;gio-2.0;gmodule-2.0;gobject-2.0;gthread-2.0;glib-2.0;libpng16;libffi;pcreposix;pcre;elf;gnuintl;zlib;bz2;iconv;ws2_32;ole32;shell32;user32;advapi32;C:/Users/appveyor/.conan/data/freetype/2.10.1/_/_/package/2eda287fd36b7b010dea069857045000246077e3/lib/freetype.lib;C:/.conan/d2f401/1/lib/glib-2.0.lib;gdi32;usp10;gdi32;rpcrt4"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/harfbuzz.lib"
  )

list(APPEND _IMPORT_CHECK_TARGETS harfbuzz::harfbuzz )
list(APPEND _IMPORT_CHECK_FILES_FOR_harfbuzz::harfbuzz "${_IMPORT_PREFIX}/lib/harfbuzz.lib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
