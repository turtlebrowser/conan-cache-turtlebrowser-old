from conans import tools
import os
from conanfile_base import BaseLib

class libXcursorConan(BaseLib):
    basename = "libXcursor"
    name = basename.lower()
    version = "1.2.0"
    tags = ("conan", "libXcursor")
    description = 'Xlib-based Cursor management library'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("libxfixes/5.0.3@bincrafters/stable", "libxrender/0.9.10@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libXcursor-1.2.0.tar.gz"
        tools.get(url, sha256="ad5b2574fccaa4c3fa67b9874fbed863d29ad230c784e9a08b20692418f6a1f8")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libXcursor-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libXcursorConan, self).package_info()
        self.cpp_info.libs.extend(["Xcursor"])
        
