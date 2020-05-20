from conans import tools
import os
from conanfile_base import BaseLib

class libXcompositeConan(BaseLib):
    basename = "libXcomposite"
    name = basename.lower()
    version = "0.4.5"
    tags = ("conan", "libXcomposite")
    description = 'Xlib-based client library for the Composite extension to the X11 protocol'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("libxfixes/5.0.3@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libXcomposite-0.4.5.tar.gz"
        tools.get(url, sha256="581c7fc0f41a99af38b1c36b9be64bc13ef3f60091cd3f01105bbc7c01617d6c")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "libXcomposite-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libXcompositeConan, self).package_info()
        self.cpp_info.libs.extend(["Xcomposite"])
        
