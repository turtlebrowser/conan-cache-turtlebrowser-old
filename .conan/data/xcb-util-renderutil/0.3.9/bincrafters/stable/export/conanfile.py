from conans import tools
import os
from conanfile_base import BaseLib

class xcbutilrenderutilConan(BaseLib):
    basename = "xcb-util-renderutil"
    name = basename.lower()
    version = "0.3.9"
    tags = ("conan", "xcb-util-renderutil")
    description = 'convenience functions for the Render extension'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("libxcb/1.13.1@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/xcb/xcb-util-renderutil-0.3.9.tar.gz"
        tools.get(url, sha256="55eee797e3214fe39d0f3f4d9448cc53cffe06706d108824ea37bb79fcedcad5")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "xcb-util-renderutil-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(xcbutilrenderutilConan, self).package_info()
        self.cpp_info.libs.extend(["xcb-render-util"])
        
