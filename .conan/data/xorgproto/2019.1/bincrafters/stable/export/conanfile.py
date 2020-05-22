from conans import tools
import os
from conanfile_base import BaseHeaderOnly

class xorgprotoConan(BaseHeaderOnly):
    basename = "xorgproto"
    name = basename.lower()
    version = "2019.1"
    tags = ("conan", "xorgproto")
    description = 'X Window System unified protocol definitions'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    

    def source(self):
        url = "https://www.x.org/archive/individual/proto/xorgproto-2019.1.tar.gz"
        tools.get(url, sha256="38ad1d8316515785d53c5162b4b7022918e03c11d72a5bd9df0a176607f42bca")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "xorgproto-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(xorgprotoConan, self).package_info()
        
        
