import info


class subinfo(info.infoclass):
    def setTargets(self):
        self.displayName = "Clipboard Inspector"
        self.description = "Native clipboard inspection app for efficient developers"
        self.webpage = "https://cuperino.com"
        for ver in ["v1.0", "main"]:
            self.svnTargets[ver] = f"[git]https://github.com/Cuperino/ClipboardInspector.git|{ver}|"
        self.defaultTarget = "main"

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = None
        if CraftCore.compiler.isLinux:
            self.buildDependencies["dev-utils/linuxdeploy"] = None
            self.buildDependencies["dev-utils/appimagetool"] = None
        elif CraftCore.compiler.isWindows:
            self.buildDependencies["dev-utils/nsis"] = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["libs/qt5/qtsvg"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtdeclarative"] = None
        if CraftCore.compiler.isAndroid:
            self.runtimeDependencies["libs/qt5/qtandroidextras"] = None
        else:
            self.runtimeDependencies["kde/frameworks/tier3/kiconthemes"] = None
            self.runtimeDependencies["kde/frameworks/tier1/breeze-icons"] = None 
        self.runtimeDependencies["libs/qt5/qtquickcontrols"] = None
        self.runtimeDependencies["libs/qt5/qtquickcontrols2"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kirigami"] = None
        self.runtimeDependencies["kde/frameworks/tier1/syntax-highlighting"] = None


from Package.CMakePackageBase import *
from Packager.AppxPackager import AppxPackager


class Package(CMakePackageBase):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if CraftCore.compiler.isMacOS:
            # Add APPLE_IN_APP_BUNDLE flag to enable private DBus, when packing by Craft
            self.subinfo.options.configure.args += " -DAPPLE_IN_APP_BUNDLE=ON"
        elif CraftCore.compiler.isWindows:
            self.defines["shortcuts"] = [{"name" : "Clipboard Inspector", "target":"bin/clipboardinspector.exe", "description" : "Clipboard inspection app for efficient developers"}]

    def createPackage(self):
        self.blacklist_file.append(os.path.join(self.packageDir(), "blacklist.txt"))
        if CraftCore.compiler.isMacOS:
            self.blacklist_file.append(os.path.join(self.packageDir(), 'blacklist_mac.txt'))

        self.defines["website"] = "https://cuperino.com/"
        self.defines["company"] = "Javier O. Cordero Perez"
        self.defines["productname"] = "Clipboard Inspector"
        if CraftCore.compiler.isMacOS:
            self.defines["appname"] = "Clipboard Inspector"
        else:
            self.defines["appname"] = "clipboardinspector"
        self.defines["license"] = os.path.join(self.sourceDir(), "COPYING")
        self.defines["executable"] = r"bin/clipboardinspector.exe"

        self.defines["icon"] = os.path.join(self.sourceDir(), "src", "icons", "clipboardinspector.ico")
        self.defines["icon_png"] = os.path.join(self.packageDir(), ".assets", "150-apps-com.cuperino.clipboardinspector.png")
        self.defines["icon_png_44"] = os.path.join(self.packageDir(), ".assets", "44-apps-com.cuperino.clipboardinspector.png")
        self.defines["icon_png_310x310"] = os.path.join(self.packageDir(), ".assets", "310-apps-com.cuperino.clipboardinspector.png")

        if isinstance(self, AppxPackager):
            self.defines["display_name"] = "Clipboard Inspector"

        self.ignoredPackages.append("binary/mysql")
        return TypePackager.createPackage(self)
