#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 16:03:28 2023

@author: thibaud

it also contains a class specifically made to manage them. This should allow to easily switch between them

this script contain the parent class of pyQT windows used in the app
"""

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication


class WindowManager :
    
    
    
    # this class contains all the windows of the app
    def __init__(self) :
        self.windows = [] # this variable will contain all the window's classes. 
        self.index = 0
        self.app = None;
        #They should all implement the UIWindow class
        
        self.sharedData = {} # this dict contains all the data that should be shared between windows
    
    def Initialize(self, windowsToUse, app):
        self.windows = windowsToUse
        self.app = app
        for i, window in enumerate(self.windows) :
            print("initialization")
            window.hierarchy = i
            window.manager = self
            window.InitUI()
        windowsToUse[0].Open()
        
    def Switch(self, newIndex):
        if newIndex < 0 : newIndex = 0
        if newIndex > len(self.windows) - 1 : newIndex = len(self.windows) - 1
        if (newIndex == self.index) : return
        
        print("new window index : " + str(newIndex))
        
        # close the windows that need it, and also wipe them if necessary
        if (self.index > newIndex) :
            for i in range(newIndex + 1, self.index + 1) :
                self.windows[i].Close(wipe = True)
                self.windows[i].Wipe()
        else :
            self.windows[self.index].Close()
        
        # now, open the desired window
        self.index = newIndex
        self.windows[self.index].Open()
        


class UIWindow(QWidget) :
    
    def __init__(self) :
        self.hierarchy = 0
        self.manager = 0
        super().__init__()
    
    def InitUI(self) :
        return;
    
    def Resize(self) :
        return;
        
    def Open(self) :
        self.setFocus()
        self.show()
        
    def Close(self, wipe=False) :
        self.hide()
        # if wipe is true, should start anew
    
    def Wipe(self) :
        # child classes should implement a method named like this
        return
    
    def InitBackButton (self, layout) :
        # this method add a standard "back" button to the window
        self.backButton = QPushButton("Back", self)
        self.backButton.clicked.connect(self.Back)
        layout.addWidget(self.backButton)
    
    def Back(self) :
        self.manager.Switch(self.hierarchy - 1)
        return
    
    def Next(self) :
        print("next window :)")
        self.manager.Switch(self.hierarchy + 1)