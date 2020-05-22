from conans import tools
import os
from conanfile_base import BaseHeaderOnly

class utilmacrosConan(BaseHeaderOnly):
    basename = "util-macros"
    name = basename.lower()
    version = "1.19.2"
    tags = ("conan", "util-macros")
    description = 'GNU autoconf macros shared across X.Org projects'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    

    def source(self):
        url = "https://www.x.org/archive/individual/util/util-macros-1.19.2.tar.gz"
        tools.get(url, sha256="9225c45c3de60faf971979a55a5536f3562baa4b6f02246c23e98ac0c09a75b7")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "util-macros-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(utilmacrosConan, self).package_info()
        
        
