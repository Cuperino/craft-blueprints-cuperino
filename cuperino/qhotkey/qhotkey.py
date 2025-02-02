import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.displayName = "QHotkey"
        self.description = "Global shortcut/hotkey for Desktop Qt-Applications"
        self.webpage = "https://github.com/Skycoder42/QHotkey"
        for ver in ["master"]:
            self.svnTargets[ver] = f"[git]https://github.com/Cuperino/QHotkey.git|{ver}|"
        self.defaultTarget = "master"

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt6/qtbase"] = None


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.configure.args += ["-DBUILD_SHARED_LIBS=ON"]
