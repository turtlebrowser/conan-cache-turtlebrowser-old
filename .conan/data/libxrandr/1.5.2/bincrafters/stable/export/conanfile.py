from conans import tools
import os
from conanfile_base import BaseLib

class libXrandrConan(BaseLib):
    basename = "libXrandr"
    name = basename.lower()
    version = "1.5.2"
    tags = ("conan", "libXrandr")
    description = 'Xlib Resize, Rotate and Reflection (RandR) extension library'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("libxrender/0.9.10@bincrafters/stable", "libxext/1.3.4@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libXrandr-1.5.2.tar.gz"
        tools.get(url, sha256="3f10813ab355e7a09f17e147d61b0ce090d898a5ea5b5519acd0ef68675dcf8e")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libXrandr-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libXrandrConan, self).package_info()
        self.cpp_info.libs.extend(["Xrandr"])
        
