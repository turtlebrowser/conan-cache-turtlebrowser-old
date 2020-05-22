from conans import tools
import os
from conanfile_base import BaseLib

class libpciaccessConan(BaseLib):
    basename = "libpciaccess"
    name = basename.lower()
    version = "0.16"
    tags = ("conan", "libpciaccess")
    description = 'Generic PCI access library'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libpciaccess-0.16.tar.gz"
        tools.get(url, sha256="84413553994aef0070cf420050aa5c0a51b1956b404920e21b81e96db6a61a27")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libpciaccess-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libpciaccessConan, self).package_info()
        self.cpp_info.libs.extend(["pciaccess"])
        
