from conans import tools
import os
from conanfile_base import BaseHeaderOnly

class libpthreadstubsConan(BaseHeaderOnly):
    basename = "libpthread-stubs"
    name = basename.lower()
    version = "0.1"
    tags = ("conan", "libpthread-stubs")
    description = 'Stub replacements for POSIX Threads functions'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libpthread-stubs-0.1.tar.gz"
        tools.get(url, sha256="f8f7ca635fa54bcaef372fd5fd9028f394992a743d73453088fcadc1dbf3a704")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libpthread-stubs-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libpthreadstubsConan, self).package_info()
        
        
