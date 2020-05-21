from conans import tools
import os
from conanfile_base import BaseLib

class libXScrnSaverConan(BaseLib):
    basename = "libXScrnSaver"
    name = basename.lower()
    version = "1.2.3"
    tags = ("conan", "libXScrnSaver")
    description = 'Xlib-based X11 Screen Saver extension client library'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("libx11/1.6.8@bincrafters/stable", "libxext/1.3.4@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libXScrnSaver-1.2.3.tar.gz"
        tools.get(url, sha256="4f74e7e412144591d8e0616db27f433cfc9f45aae6669c6c4bb03e6bf9be809a")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libXScrnSaver-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libXScrnSaverConan, self).package_info()
        self.cpp_info.libs.extend(["Xss"])
        
