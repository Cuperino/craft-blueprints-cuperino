# SPDX-License-Identifier: GPL-3.0
# SPDX-FileCopyrightText: 2022 Javier O. Cordero Pérez

import info

class subinfo(info.infoclass):
    def setTargets(self):
        #self.versionInfo.setDefaultValues()
        self.displayName = "QHotkey"
        self.description = "Global shortcut/hotkey for Desktop Qt-Applications"
        self.webpage = "https://skycoder42.github.io/QHotkey/"
        for ver in ["1.5.1", "1.5.0", "master"]:
            self.svnTargets[ver] = f"[git]https://github.com/Cuperino/QHotkey.git|{ver}|"
        self.defaultTarget = "1.5.1"

    def setDependencies(self):
        # self.buildDependencies["virtual/base"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/x11extras"] = None
        # if CraftCore.compiler.isWindows:
