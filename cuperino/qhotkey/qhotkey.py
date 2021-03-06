# -*- coding: utf-8 -*-
# SPDX-License-Identifier: GPL-3.0
# SPDX-FileCopyrightText: 2022 Javier O. Cordero Pérez

import info

class subinfo(info.infoclass):
    def setTargets(self):
        #self.versionInfo.setDefaultValues()
        self.displayName = "QHotkey"
        self.description = "Global shortcut/hotkey for Desktop Qt-Applications"
        self.webpage = "https://skycoder42.github.io/QHotkey/"
        for ver in ["1.5.2", "master"]:
            self.svnTargets[ver] = f"[git]https://github.com/Cuperino/QHotkey.git|{ver}|"
        self.defaultTarget = "1.5.2"

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = None
        self.buildDependencies["libs/qt5/qtx11extras"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtx11extras"] = None
        # if CraftCore.compiler.isWindows:

from Package.CMakePackageBase import *

class Package(CMakePackageBase):
    def __init__(self):
        CMakePackageBase.__init__(self)
