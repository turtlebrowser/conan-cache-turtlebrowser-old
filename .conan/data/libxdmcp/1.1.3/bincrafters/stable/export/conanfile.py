from conans import tools
import os
from conanfile_base import BaseLib

class libXdmcpConan(BaseLib):
    basename = "libXdmcp"
    name = basename.lower()
    version = "1.1.3"
    tags = ("conan", "libXdmcp")
    description = 'X Display Manager Control Protocol library'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("xproto/7.0.31@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libXdmcp-1.1.3.tar.gz"
        tools.get(url, sha256="2ef9653d32e09d1bf1b837d0e0311024979653fe755ad3aaada8db1aa6ea180c")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libXdmcp-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libXdmcpConan, self).package_info()
        self.cpp_info.libs.extend(["Xdmcp"])
        
