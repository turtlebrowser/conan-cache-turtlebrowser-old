from conans import tools
import os
from conanfile_base import BaseLib

class libXtstConan(BaseLib):
    basename = "libXtst"
    name = basename.lower()
    version = "1.2.3"
    tags = ("conan", "libXtst")
    description = 'Xlib-based library for XTEST & RECORD extensions'
    exports = ["conanfile_base.py"]

    requires = ("libxi/1.7.10@bincrafters/stable")

    def source(self):
        url = "https://www.x.org/archive/individual/lib/libXtst-1.2.3.tar.gz"
        tools.get(url, sha256="a0c83acce02d4923018c744662cb28eb0dbbc33b4adc027726879ccf68fbc2c2")
        extracted_dir = "libXtst-" + self.version
        os.rename(extracted_dir, self._source_subfolder)

    def package_info(self):
        super(libXtstConan, self).package_info()
        self.cpp_info.libs.extend(["Xtst"])
