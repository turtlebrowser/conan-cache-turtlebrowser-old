from conans import tools
import os
from conanfile_base import BaseHeaderOnly

class xkeyboardconfigConan(BaseHeaderOnly):
    basename = "xkeyboard-config"
    name = basename.lower()
    version = "2.28"
    tags = ("conan", "xkeyboard-config")
    description = 'keyboard configuration database for the X Window System.'
    exports = ["conanfile_base.py", "patches/*.patch"]
    _patches = []

    requires = ("xproto/7.0.31@bincrafters/stable", "libx11/1.6.8@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/data/xkeyboard-config/xkeyboard-config-2.28.tar.gz"
        tools.get(url, sha256="4424ffaafdf9f09dea69a317709353c4e2b19f69b2405effadce0bac3bdebdff")
        for p in self._patches:
            tools.patch(".", "patches/%s" % p)
        extracted_dir = "xkeyboard-config-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(xkeyboardconfigConan, self).package_info()
        
        
