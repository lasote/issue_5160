import os
import shutil
from conans import ConanFile, CMake, tools


class PythonRequires(ConanFile):
    name = "pyreq"
    version = "version"


def get_version():
    return "My2 version"

def get_conanfile():

    class BaseConanFile(ConanFile):

        settings = "os", "compiler", "build_type", "arch"
        options = {"shared": [True, False]}
        default_options = {"shared": False}
        generators = "cmake"
        exports_sources = "src/*"

        def package(self):
            self.copy("*.h", dst="include", src="src")
            self.copy("*.lib", dst="lib", keep_path=False)
            self.copy("*.dll", dst="bin", keep_path=False)
            self.copy("*.dylib*", dst="lib", keep_path=False)
            self.copy("*.so", dst="lib", keep_path=False)
            self.copy("*.a", dst="lib", keep_path=False)

        def package_info(self):
            self.cpp_info.libs = [self.name]

    return BaseConanFile
