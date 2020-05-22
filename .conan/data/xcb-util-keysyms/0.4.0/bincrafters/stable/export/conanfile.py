from conans import tools
import os
from conanfile_base import BaseLib

class xcbutilkeysymsConan(BaseLib):
    basename = "xcb-util-keysyms"
    name = basename.lower()
    version = "0.4.0"
    tags = ("conan", "xcb-util-keysyms")
    description = 'Library for handling standard X key constants and conversion to/from keycodes.'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("libxcb/1.13.1@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/xcb/xcb-util-keysyms-0.4.0.tar.gz"
        tools.get(url, sha256="0807cf078fbe38489a41d755095c58239e1b67299f14460dec2ec811e96caa96")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "xcb-util-keysyms-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(xcbutilkeysymsConan, self).package_info()
        self.cpp_info.libs.extend(["xcb-keysyms"])
        
