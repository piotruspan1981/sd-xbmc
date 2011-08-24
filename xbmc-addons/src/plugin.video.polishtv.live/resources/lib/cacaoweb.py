# -*- coding: utf-8 -*-
import subprocess
import string, urllib
import sys
import re
import os
import xbmcaddon

scriptID = 'plugin.video.polishtv.live'
scriptname = "Polish Live TV"
ptv = xbmcaddon.Addon(scriptID)

BASE_RESOURCE_PATH = os.path.join( ptv.getAddonInfo('path'), "resources" )
sys.path.append( os.path.join( BASE_RESOURCE_PATH, "lib" ) )

import pLog

log = pLog.pLog()


class CacaoWeb:
    def __init__(self):
        log.info('Starting cacaoweb')
    
    
    def runApp(self):
        try:
            appRun = ''
            if self.typeOS() == "linux":
                appRun = '"' + os.getenv("HOME") + '/.xbmc/addons/plugin.video.polishtv.live/bin/cacaoweb.linux" &'
            elif self.typeOS() == "windows":
                appRun = '"' + os.getenv("USERPROFILE") + '\\AppData\\Roaming\\XBMC\\addons\\plugin.video.polishtv.live\\bin\\cacaoweb.exe"'
            if appRun != '':
                self.delTMPFiles()
                os.system(appRun)
        except OSError, e:
            return 1
      

    def delTMPFiles(self):
        tmpDir = ''
        if self.typeOS() == "linux":
            tmpDir = '"' + os.getenv("HOME") + '/.cacaoweb"'
        elif self.typeOS() == "windows":
            tmpDir = '"' + os.getenv("USERPROFILE") + '\\AppData\\Roaming\\cacaoweb"'
        if os.path.isdir(tmpDir):
            for fileName in os.listdir(tmpDir):
                if fileName.endswith('.cacao'):
                    os.remove(tmpDir + '/' + fileName)


    def process_num(self, process):
        return os.system('pidof %s |wc -w' % process)
    
    
    def stopApp(self):
        if self.typeOS() == "linux":
            os.system("killall -9 cacaoweb.linux")
        elif self.typeOS() == "windows":
            os.system("taskkill /F /PID cacaoweb.exe")
            
            
    def typeOS(self):
        os = ''
        try:
            #if os.uname()[0] == "Linux":
            if sys.platform.startswith("linux"):
                os = 'linux'
            #elif os.uname()[0] == "Windows":
            elif sys.platform.startswith("win32"):
                os = 'windows'
        except:
            pass
        #    if platform.system() == 'Linux':
        #        os = 'Linux'
        #    elif platform.system() == 'Windows':
        #        os = 'Windows'
        return os