# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0
# SPDX-FileCopyrightText: 2021-2022 Javier O. Cordero Pérez

import info

class subinfo(info.infoclass):
    def setTargets(self):
        #self.versionInfo.setDefaultValues()
        self.displayName = "QPrompt"
        self.description = "Teleprompter software for all video creators"
        self.webpage = "https://qprompt.app"
        for ver in ["v1.0", "main"]:
            self.svnTargets[ver] = f"[git]https://github.com/Cuperino/QPrompt.git|{ver}|"
        self.defaultTarget = "main"

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = None
        if CraftCore.compiler.isLinux:
            self.buildDependencies["dev-utils/linuxdeploy"] = None
            self.buildDependencies["dev-utils/appimagetool"] = None
        elif CraftCore.compiler.isWindows:
            self.buildDependencies["dev-utils/nsis"] = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["libs/qt5/qtsvg"] = "libs/qt5"
        self.runtimeDependencies["libs/qt5/qtbase"] = "libs/qt5"
        self.runtimeDependencies["libs/qt5/qtdeclarative"] = "libs/qt5"
        if CraftCore.compiler.isAndroid:
            self.runtimeDependencies["libs/qt5/qtandroidextras"] = "libs/qt5"
        else:
            self.runtimeDependencies["kde/frameworks/tier3/kiconthemes"] = None
            self.runtimeDependencies["kde/frameworks/tier1/breeze-icons"] = None 
        self.runtimeDependencies["libs/qt5/qtquickcontrols"] = "libs/qt5"
        self.runtimeDependencies["libs/qt5/qtquickcontrols2"] = "libs/qt5"
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kirigami"] = None

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
        if CraftCore.compiler.isMacOS:
            # Add APPLE_IN_APP_BUNDLE flag to enable private DBus, when packing by Craft
            self.subinfo.options.configure.args += " -DAPPLE_IN_APP_BUNDLE=ON"
        elif CraftCore.compiler.isWindows:
            self.defines["shortcuts"] = [{"name" : "QPrompt", "target":"bin/qprompt.exe", "description" : "Teleprompter software for all video creators"}]

    def createPackage(self):
        self.blacklist_file.append(os.path.join(self.packageDir(), "blacklist.txt"))
        if CraftCore.compiler.isMacOS:
            self.blacklist_file.append(os.path.join(self.packageDir(), 'blacklist_mac.txt'))

        self.defines["website"] = "https://qprompt.app/"
        self.defines["company"] = "Javier O. Cordero Perez"
        self.defines["productname"] = "QPrompt"
        self.defines["appname"] = "qprompt"
        self.defines["license"] = os.path.join(self.sourceDir(), "COPYING")
        self.defines["executable"] = r"bin/qprompt.exe"

        self.defines["icon"] = os.path.join(self.sourceDir(), "src", "icons", "qprompt.ico")
        self.defines["icon_png"] = os.path.join(self.packageDir(), ".assets", "150-apps-com.cuperino.qprompt.png")
        self.defines["icon_png_44"] = os.path.join(self.packageDir(), ".assets", "44-apps-com.cuperino.qprompt.png")
        self.defines["icon_png_310x310"] = os.path.join(self.packageDir(), ".assets", "310-apps-com.cuperino.qprompt.png")

        if isinstance(self, AppxPackager):
            self.defines["display_name"] = "QPrompt"

        self.ignoredPackages.append("binary/mysql")
        return TypePackager.createPackage(self)
