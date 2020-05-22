from conans import tools
import os
from conanfile_base import BaseLib

class xcbutilwmConan(BaseLib):
    basename = "xcb-util-wm"
    name = basename.lower()
    version = "0.4.0"
    tags = ("conan", "xcb-util-wm")
    description = ' XCB ICCCM and EWMH bindings'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("libxcb/1.13.1@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/xcb/xcb-util-wm-0.4.0.tar.gz"
        tools.get(url, sha256="48c9b2a8c5697e0fde189706a6fa4b09b7b65762d88a495308e646eaf891f42a")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "xcb-util-wm-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(xcbutilwmConan, self).package_info()
        self.cpp_info.libs.extend(["xcb-ewmh", "xcb-icccm"])
        
