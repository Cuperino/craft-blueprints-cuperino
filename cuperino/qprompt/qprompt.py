import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.displayName = "QPrompt"
        self.description = "Teleprompter software for all video creators"
        self.webpage = "https://qprompt.app"
        for ver in ["v2.0", "main"]:
            self.svnTargets[ver] = f"[git]https://github.com/Cuperino/QPrompt.git|{ver}|"
        self.defaultTarget = "v2.0"

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = None
        if CraftCore.compiler.isLinux:
            self.buildDependencies["dev-utils/linuxdeploy"] = None
            self.buildDependencies["dev-utils/appimagetool"] = None
        elif CraftCore.compiler.isWindows:
            self.buildDependencies["dev-utils/nsis"] = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["libs/qt6/qtsvg"] = None
        self.runtimeDependencies["libs/qt6/qtbase"] = None
        self.runtimeDependencies["libs/qt6/qtdeclarative"] = None
        elif not CraftCore.compiler.isFreeBSD:
            self.buildDependencies["cuperino/qhotkey"] = None
            self.runtimeDependencies["cuperino/qhotkey"] = None
            self.runtimeDependencies["kde/frameworks/tier2/kcrash"] = None
        self.runtimeDependencies["libs/qt6/qtquickcontrols"] = None
        self.runtimeDependencies["libs/qt6/qtquickcontrols2"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kirigami"] = None


from Package.CMakePackageBase import *


class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subinfo.options.fetch.checkoutSubmodules = True
        if CraftCore.compiler.isMacOS:
            # Add APPLE_IN_APP_BUNDLE flag to enable private DBus, when packing by Craft
            self.subinfo.options.configure.args += ["-DAPPLE_IN_APP_BUNDLE=ON"]
        elif CraftCore.compiler.isWindows:
            self.defines["shortcuts"] = [{"name" : "QPrompt", "target":"bin/qprompt.exe", "description" : "Teleprompter software for all video creators"}]

    def createPackage(self):
        self.blacklist_file.append(os.path.join(self.blueprintDir(), "blacklist.txt"))
        if CraftCore.compiler.isMacOS:
            self.blacklist_file.append(os.path.join(self.blueprintDir(), 'blacklist_mac.txt'))

        self.defines["website"] = "https://qprompt.app/"
        self.defines["company"] = "Javier O. Cordero Perez"
        self.defines["productname"] = "QPrompt"
        if CraftCore.compiler.isMacOS:
            self.defines["appname"] = "QPrompt"
        else:
            self.defines["appname"] = "qprompt"
        self.defines["license"] = os.path.join(self.sourceDir(), "COPYING")
        self.defines["executable"] = r"bin/qprompt.exe"

        self.defines["icon"] = os.path.join(self.sourceDir(), "src", "icons", "qprompt.ico")
        self.defines["icon_png"] = os.path.join(self.packageDir(), ".assets", "150-apps-com.cuperino.qprompt.png")
        self.defines["icon_png_44"] = os.path.join(self.packageDir(), ".assets", "44-apps-com.cuperino.qprompt.png")
        self.defines["icon_png_310x310"] = os.path.join(self.packageDir(), ".assets", "310-apps-com.cuperino.qprompt.png")

        self.defines["alias"] = "qprompt"

        self.ignoredPackages.append("binary/mysql")
        self.ignoredPackages.append("dev-utils/sed")
        return super().createPackage()
