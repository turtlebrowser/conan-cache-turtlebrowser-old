from conans import tools
import os
from conanfile_base import BaseHeaderOnly

class xprotoConan(BaseHeaderOnly):
    basename = "xproto"
    name = basename.lower()
    version = "7.0.31"
    tags = ("conan", "xproto")
    description = 'X Window System Core Protocol'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ()

    def source(self):
        url = "https://www.x.org/archive/individual/proto/xproto-7.0.31.tar.gz"
        tools.get(url, sha256="6d755eaae27b45c5cc75529a12855fed5de5969b367ed05003944cf901ed43c7")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "xproto-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(xprotoConan, self).package_info()
        
        
