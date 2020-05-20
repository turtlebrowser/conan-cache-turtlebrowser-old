from conans import tools
import os
from conanfile_base import BaseLib

class libXfixesConan(BaseLib):
    basename = "libXfixes"
    name = basename.lower()
    version = "5.0.3"
    tags = ("conan", "libXfixes")
    description = 'Xlib-based library for the XFIXES Extension'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("libx11/1.6.8@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libXfixes-5.0.3.tar.gz"
        tools.get(url, sha256="9ab6c13590658501ce4bd965a8a5d32ba4d8b3bb39a5a5bc9901edffc5666570")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libXfixes-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libXfixesConan, self).package_info()
        self.cpp_info.libs.extend(["Xfixes"])
        
