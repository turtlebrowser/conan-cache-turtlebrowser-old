from conans import tools
import os
from conanfile_base import BaseLib

class xcbutilimageConan(BaseLib):
    basename = "xcb-util-image"
    name = basename.lower()
    version = "0.4.0"
    tags = ("conan", "xcb-util-image")
    description = 'XCB image convenience library'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = ['clang.patch', 'xcb-util-image.patch']

    requires = ("xcb-util/0.4.0@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/xcb/xcb-util-image-0.4.0.tar.gz"
        tools.get(url, sha256="cb2c86190cf6216260b7357a57d9100811bb6f78c24576a3a5bfef6ad3740a42")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "xcb-util-image-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(xcbutilimageConan, self).package_info()
        self.cpp_info.libs.extend(["xcb-image"])
        
