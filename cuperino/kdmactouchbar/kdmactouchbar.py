# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0
# SPDX-FileCopyrightText: 2022 Javier O. Cordero Pérez

import info

class subinfo(info.infoclass):
    def registerOptions(self):
        self.parent.package.categoryInfo.platforms = CraftCore.compiler.Platforms.MacOS

    def setTargets(self):
        if CraftCore.compiler.isMacOS:
        #self.versionInfo.setDefaultValues()
        self.displayName = "KDMacTouchbar"
        self.description = "Provides a Qt-based API for the Mac Touch Bar"
        self.webpage = "https://www.kdab.com/kdmactouchbar/"

        self.svnTargets["master"] = "[git]https://github.com/KDAB/KDMacTouchBar.git"
        for ver in []:
            self.targets[ver] = f"https://github.com/KDAB/KDMacTouchBar/archive/kdmactouchbar-{ver}.tar.gz"
            self.targetInstSrc[ver] = f"KDMacTouchBar-kdmactouchbar-{ver}"
            self.archiveNames[ver] = f"kdmactouchbar-{ver}.tar.gz"
        self.defaultTarget = "master"

    def setDependencies(self):
        if CraftCore.compiler.isMacOS:
            self.runtimeDependencies["libs/qt5/qtbase"] = None

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
