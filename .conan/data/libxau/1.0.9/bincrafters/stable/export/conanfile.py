from conans import tools
import os
from conanfile_base import BaseLib

class libXauConan(BaseLib):
    basename = "libXau"
    name = basename.lower()
    version = "1.0.9"
    tags = ("conan", "libXau")
    description = 'Functions for handling Xauthority files and entries.'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("xorgproto/2019.1@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libXau-1.0.9.tar.gz"
        tools.get(url, sha256="1f123d8304b082ad63a9e89376400a3b1d4c29e67e3ea07b3f659cccca690eea")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libXau-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libXauConan, self).package_info()
        self.cpp_info.libs.extend(["Xau"])
        
