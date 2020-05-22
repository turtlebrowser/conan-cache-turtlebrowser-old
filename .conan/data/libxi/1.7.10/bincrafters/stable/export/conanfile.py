from conans import tools
import os
from conanfile_base import BaseLib

class libXiConan(BaseLib):
    basename = "libXi"
    name = basename.lower()
    version = "1.7.10"
    tags = ("conan", "libXi")
    description = 'Xlib library for the X Input Extension'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("libxext/1.3.4@bincrafters/stable", "libxfixes/5.0.3@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libXi-1.7.10.tar.gz"
        tools.get(url, sha256="b51e106c445a49409f3da877aa2f9129839001b24697d75a54e5c60507e9a5e3")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libXi-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libXiConan, self).package_info()
        self.cpp_info.libs.extend(["Xi"])
        
