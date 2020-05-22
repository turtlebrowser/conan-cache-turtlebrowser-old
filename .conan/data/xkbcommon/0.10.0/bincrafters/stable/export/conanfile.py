from conans import ConanFile, Meson, tools
from conans.errors import ConanInvalidConfiguration
import os
import shutil


class XkbcommonConan(ConanFile):
    name = "xkbcommon"
    description = "keymap handling library for toolkits and window systems"
    topics = ("conan", "xkbcommon", "keyboard")
    url = "https://github.com/bincrafters/conan-xkbcommon"
    homepage = "https://github.com/xkbcommon/libxkbcommon"
    license = "MIT"
    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "with_x11": [True, False],
        "with_wayland": [True, False],
        "docs": [True, False]
    }
    default_options = {
        "shared": True,
        "fPIC": True,
        "with_x11": True,
        "with_wayland": False,
        "docs": False
    }
    exports = '*.diff'
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def configure(self):
        if self.settings.os != "Linux":
            raise ConanInvalidConfiguration("This library is only compatible with Linux")
        del self.settings.compiler.libcxx
        del self.settings.compiler.cppstd

    def build_requirements(self):
        if not tools.which("meson"):
            self.build_requires("meson/0.53.2")
        if not tools.which("bison"):
            self.build_requires("bison_installer/3.2.4@bincrafters/stable")
        if not tools.which("pkg-config"):
            self.build_requires("pkg-config_installer/0.29.2@bincrafters/stable")

    def requirements(self):
        self.requires("xkeyboard-config/2.28@bincrafters/stable")
        if self.options.with_x11:
            self.requires("libxcb/1.13.1@bincrafters/stable")

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = "libxkbcommon-" + self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)
        tools.patch(base_path=self._source_subfolder, patch_file='option_use-static.diff')

    def _configure_meson(self):
        defs={
            "enable-wayland": self.options.with_wayland,
            "enable-docs": self.options.docs,
            "enable-x11": self.options.with_x11,
            "libdir": os.path.join(self.package_folder, "lib"),
            "default_library": ("shared" if self.options.shared else "static")}
        if self.options.with_x11:
            defs["use-static-xcb"] = ("false" if self.options["libxcb"].shared else "true")

        meson = Meson(self)
        meson.configure(
            defs=defs,
            source_folder=self._source_subfolder,
            build_folder=self._build_subfolder,
            pkg_config_paths=self.build_folder)
        return meson

    def build(self):
        def _get_pc_files(package):
            if package in self.deps_cpp_info.deps:
                lib_path = self.deps_cpp_info[package].rootpath
                for dirpath, _, filenames in os.walk(lib_path):
                    for filename in filenames:
                        if filename.endswith('.pc'):
                            shutil.copyfile(os.path.join(dirpath, filename), filename)
                            tools.replace_prefix_in_pc_file(filename, lib_path)
                for dep in self.deps_cpp_info[package].public_deps:
                    _get_pc_files(dep)
        _get_pc_files('libxcb')
        _get_pc_files('xkeyboard-config')
        meson = self._configure_meson()
        meson.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)
        meson = self._configure_meson()
        meson.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
