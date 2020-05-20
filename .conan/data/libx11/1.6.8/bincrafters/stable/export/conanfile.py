from conans import tools
import os
from conanfile_base import BaseLib

class libX11Conan(BaseLib):
    basename = "libX11"
    name = basename.lower()
    version = "1.6.8"
    tags = ("conan", "libX11")
    description = 'Core X11 protocol client library (aka "Xlib")'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = ['libx11.patch']

    requires = ("xorgproto/2019.1@bincrafters/stable", "xtrans/1.4.0@bincrafters/stable", "libxcb/1.13.1@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libX11-1.6.8.tar.gz"
        tools.get(url, sha256="69d1a27cba722dca897198a23fa8d3cad3ec0c715e00205ea4398ec68a4258a5")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libX11-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libX11Conan, self).package_info()
        self.cpp_info.libs.extend(["X11"])
        self.cpp_info.system_libs.extend(["dl"])
