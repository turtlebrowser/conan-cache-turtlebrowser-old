from conans import tools
import os
from conanfile_base import BaseHeaderOnly

class xtransConan(BaseHeaderOnly):
    basename = "xtrans"
    name = basename.lower()
    version = "1.4.0"
    tags = ("conan", "xtrans")
    description = 'X Window System Protocols Transport layer shared code'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    

    def source(self):
        url = "https://www.x.org/archive/individual/lib/xtrans-1.4.0.tar.gz"
        tools.get(url, sha256="48ed850ce772fef1b44ca23639b0a57e38884045ed2cbb18ab137ef33ec713f9")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "xtrans-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(xtransConan, self).package_info()
        
        
