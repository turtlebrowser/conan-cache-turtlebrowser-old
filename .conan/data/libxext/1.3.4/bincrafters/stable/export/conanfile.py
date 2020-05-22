from conans import tools
import os
from conanfile_base import BaseLib

class libXextConan(BaseLib):
    basename = "libXext"
    name = basename.lower()
    version = "1.3.4"
    tags = ("conan", "libXext")
    description = 'Xlib-based library for common extensions to the X11 protocol'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("libx11/1.6.8@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libXext-1.3.4.tar.gz"
        tools.get(url, sha256="8ef0789f282826661ff40a8eef22430378516ac580167da35cc948be9041aac1")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libXext-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libXextConan, self).package_info()
        self.cpp_info.libs.extend(["Xext"])
        self.cpp_info.system_libs.extend(["dl"])
