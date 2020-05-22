from conans import tools
import os
from conanfile_base import BaseLib

class libxcbConan(BaseLib):
    basename = "libxcb"
    name = basename.lower()
    version = "1.13.1"
    tags = ("conan", "libxcb")
    description = 'C interface to the X Window System protocol, which replaces the traditional Xlib interface'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("xcb-proto/1.13@bincrafters/stable", "util-macros/1.19.2@bincrafters/stable", "libxau/1.0.9@bincrafters/stable", "libpthread-stubs/0.1@bincrafters/stable", "libxdmcp/1.1.3@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/xcb/libxcb-1.13.1.tar.gz"
        tools.get(url, sha256="f09a76971437780a602303170fd51b5f7474051722bc39d566a272d2c4bde1b5")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libxcb-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libxcbConan, self).package_info()
        self.cpp_info.libs.extend(["xcb"])
        
