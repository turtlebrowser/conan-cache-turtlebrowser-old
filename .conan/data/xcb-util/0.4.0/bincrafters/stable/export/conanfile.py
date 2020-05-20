from conans import tools
import os
from conanfile_base import BaseLib

class xcbutilConan(BaseLib):
    basename = "xcb-util"
    name = basename.lower()
    version = "0.4.0"
    tags = ("conan", "xcb-util")
    description = 'utility functions for other XCB utilities.'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("libxcb/1.13.1@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/xcb/xcb-util-0.4.0.tar.gz"
        tools.get(url, sha256="0ed0934e2ef4ddff53fcc70fc64fb16fe766cd41ee00330312e20a985fd927a7")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "xcb-util-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(xcbutilConan, self).package_info()
        self.cpp_info.libs.extend(["xcb-util"])
        
