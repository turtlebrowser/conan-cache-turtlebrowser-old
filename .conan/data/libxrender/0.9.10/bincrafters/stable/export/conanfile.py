from conans import tools
import os
from conanfile_base import BaseLib

class libXrenderConan(BaseLib):
    basename = "libXrender"
    name = basename.lower()
    version = "0.9.10"
    tags = ("conan", "libXrender")
    description = 'Xlib library for the Render Extension to the X11 protocol'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("libx11/1.6.8@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libXrender-0.9.10.tar.gz"
        tools.get(url, sha256="770527cce42500790433df84ec3521e8bf095dfe5079454a92236494ab296adf")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libXrender-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libXrenderConan, self).package_info()
        self.cpp_info.libs.extend(["Xrender"])
        
