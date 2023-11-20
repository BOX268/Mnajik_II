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
    
    sharedData = {} # this dict contains all the data that should be shared between windows
    
    # this class contains all the windows of the app
    def __init__(self) :
        self.windows = [] # this variable will contain all the window's classes. 
        self.index = 0
        #They should all implement the UIWindow class
    
    def Initialize(self, windowsToUse):
        self.windows = windowsToUse
        for i, window in enumerate(self.windows) :
            window.InitUI(i, self)
        
    def Switch(self, newIndex):
        if newIndex < 0 : newIndex = 0
        if newIndex > len(windows) - 1 : newIndex = len(windows) - 1
        if (newIndex == index) : return
        
        # close the windows that need it, and also wipe them if necessary
        if (index > newIndex) :
            for i in range(newIndex + 1, index + 1) :
                self.windows[i].Close(wipe = True)
                self.windows[i].Wipe()
        else :
            self.windows[index].Close()
        
        # now, open the desired window
        index = newIndex
        self.windows[index].Open()
        


class UIWindow(QWidget) :
    
    def __init__(self) :
        super().__init__()
    
    def InitUI(self, hierarchy, manager) :
        self.hierachy = hierarchy
        self.manager = manager
    
    def Resize(self) :
        return;
        
    def Open(self) :
        self.show()
        
    def Close(self, wipe=False) :
        self.hide()
        # if wipe is true, should start anew
    
    def Wipe(self) :
        # child classes should implement a method named like this
        return
    
    def InitBackButton (self, layout) :
        self.backButton = QPushButton("Back", self)
        self.backButton.clicked.connect(self.Back)
        layout.addWidget(self.backButton)
    
    def Back(self) :
        # this method add a standard "back" button to the window
        manager.Switch(hierarchy)
        return