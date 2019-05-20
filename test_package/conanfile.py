from conans import ConanFile, python_requires


base = python_requires("pyreq/version@user/channel")

class ConsumerConan(base.get_conanfile()):
    name = "consumer"
    version = "1.2"

    # Everything else is inherited

    def test(self):
        print(base.get_version())

