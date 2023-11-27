"""
01/06/2020

Mnajik II, GUI I.

written w/ python3

Author  @Gregory Page

updated by Thibaud Michelet
added a fourth window to display example and fixed the formatting
fixed issues regarding the possibility of results to contain more numpy arrays stacks than usual

"""

import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from Mnajik_II import Mnain
from termcolor import colored
import requests
import random
import numpy as np

import UIframe as UIFrame

class App1(UIFrame.UIWindow) :

    def __init__(self):
        super().__init__()
        
        QWidget.__init__(self)
        
        # initilize layout and important stuff.
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.title = 'Mnajik vII'
        self.setWindowTitle(self.title)
        
        print("initialized")


    def InitUI(self) :

        print("intiUI")
        # first, resize the window
        
        
        
        # first create list title
        self.label_1 = QLabel('Origin :', self)

        self.label_1.setStyleSheet("color: rgb(115, 1, 230)")
        self.label_1.setAlignment(Qt.AlignCenter)

        # setting font and size
        self.label_1.setFont(QFont('Oxygen', 13))
        self.layout.addWidget(self.label_1)
        
        # create list of possible
        self.listwidget = QListWidget()
        self.listwidget.addItem("English")
        self.listwidget.addItem("French")
        self.listwidget.addItem("Spanish")
        self.listwidget.addItem("Portuguese")

        self.listwidget.clicked.connect(self.clicked)
        self.layout.addWidget(self.listwidget)
        
        self.Resize()
        
    
    def Resize(self) :
        
        screen = self.manager.app.primaryScreen()
        windowHeight = 0
        windowHeight = screen.size().height() / 3
        windowHeight = int(max(100, min(400, windowHeight)))
        self.size = windowHeight
        windowWidth = windowHeight
        
        self.left = 725
        self.top = 425
        self.width = windowWidth
        self.height = windowHeight
        
        self.setGeometry(self.left, self.top, self.width, self.height)

    def clicked(self) :
        item = self.listwidget.currentItem()
        #print( self.listwidget.row(item)  )
        self.manager.sharedData["originID"] =  self.listwidget.row(item)
        self.Next()


    def window2(self):                                             # <===
        self.w = App2(0)
        self.w.show()
        self.hide()


class App2(UIFrame.UIWindow):

    def __init__(self):
        super().__init__()

        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.title = 'Mnajik vII'
        self.setWindowTitle(self.title)
        


    def InitUI(self):

        self.Resize()
        
        self.label_1 = QLabel('Target:', self)
        # moving position
        
        self.label_1.setStyleSheet("color: rgb(115, 1, 230)")
        self.label_1.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.label_1)

        # setting font and size
        self.label_1.setFont(QFont('Oxygen', 13))
        
        self.listwidget = QListWidget()
        self.listwidget.addItem("French")
        self.listwidget.addItem("English (BROKEN)")
        self.listwidget.addItem("Spanish")
        self.listwidget.addItem("Italian")
        self.listwidget.addItem("German")
        self.listwidget.addItem("Hungarian")
        self.listwidget.addItem("Portuguese")
        self.listwidget.clicked.connect(self.clicked) #connect to window2
        self.layout.addWidget(self.listwidget)
        
        self.InitBackButton(self.layout)
    
    
    def Resize(self) :
        
        screen = app.primaryScreen()
        windowHeight = 0
        windowHeight = screen.size().height() / 3
        windowHeight = int(max(100, min(400, windowHeight)))
        self.size = windowHeight
        windowWidth = windowHeight
        
        self.left = 725
        self.top = 425
        self.width = windowWidth
        self.height = windowHeight
        
        self.setGeometry(self.left, self.top, self.width, self.height)

    def clicked(self) :
        item = self.listwidget.currentItem()
        #print( self.listwidget.row(item)  )
        self.manager.sharedData["targetID"] = self.listwidget.row(item)
        self.Next();


class InputWindow(UIFrame.UIWindow) :
    
    def __init__(self) :
        super().__init__()
        
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        
        self.title = "Mnajik vII"
        self.setWindowTitle(self.title)
    
    def Resize(self) :
        screen = app.primaryScreen()
        windowHeight = 0
        windowHeight = screen.size().height() / 3
        windowHeight = int(max(100, min(400, windowHeight)))
        self.size = windowHeight
        windowWidth = windowHeight * 2
        
        self.left = 725
        self.top = 425
        self.width = windowWidth
        self.height = windowHeight
        
        self.setGeometry(self.left, self.top, self.width, self.height)
    
    def InitUI(self) :
        
        self.Resize()
        
        self.containerOrigin = QGroupBox(self)
        self.containerTarget = QGroupBox(self)
        self.containerWord = QGroupBox(self)
        
        # will need to add some beauty to those groupboxes here
        self.containerOrigin.setLayout(QVBoxLayout())
        self.containerTarget.setLayout(QVBoxLayout())
        self.containerWord.setLayout(QVBoxLayout())
        
        self.layout.addWidget(self.containerOrigin)
        self.layout.addWidget(self.containerTarget)
        self.layout.addWidget(self.containerWord)
        
        # now, initialize the origin selection
        tempTitle = QLabel('Origin Language :', self.containerOrigin)
        tempTitle.setStyleSheet("color: rgb(115, 1, 230)")
        tempTitle.setAlignment(Qt.AlignCenter)
        tempTitle.setFont(QFont('Oxygen', 13))
        self.containerOrigin.layout().addWidget(tempTitle)
        
        # create list of possible origin languages
        self.originListwidget = QListWidget(self.containerOrigin)
        self.originListwidget.addItem("English")
        self.originListwidget.addItem("French")
        self.originListwidget.addItem("Spanish")
        self.originListwidget.addItem("Portuguese")
        self.containerOrigin.layout().addWidget(self.originListwidget)
        
        tempTitle = QLabel('Target Language :', self.containerTarget)
        tempTitle.setStyleSheet("color: rgb(115, 1, 230)")
        tempTitle.setAlignment(Qt.AlignCenter)
        tempTitle.setFont(QFont('Oxygen', 13))
        self.containerTarget.layout().addWidget(tempTitle)
        
        self.targetListwidget = QListWidget(self.containerTarget)
        self.targetListwidget.addItem("French")
        self.targetListwidget.addItem("English (BROKEN)")
        self.targetListwidget.addItem("Spanish")
        self.targetListwidget.addItem("Italian")
        self.targetListwidget.addItem("German")
        self.targetListwidget.addItem("Hungarian")
        self.targetListwidget.addItem("Portuguese")
        self.containerTarget.layout().addWidget(self.targetListwidget)
        
        tempTitle = QLabel('Word to translate :', self.containerWord)
        tempTitle.setStyleSheet("color: rgb(115, 1, 230)")
        tempTitle.setAlignment(Qt.AlignCenter)
        tempTitle.setFont(QFont('Oxygen', 13))
        self.containerWord.layout().addWidget(tempTitle)
        
        self.wordInput = QLineEdit(self.containerWord)
        self.containerWord.layout().addWidget(self.wordInput)
        self.wordInput.returnPressed.connect(self.WordSubmit)
        
        self.errorDisplay = QLabel('', self.containerWord)
        self.errorDisplay.setStyleSheet("color: rgb(180, 1, 1)")
        self.errorDisplay.setAlignment(Qt.AlignCenter)
        self.errorDisplay.setFont(QFont('Oxygen', 13))
        self.containerWord.layout().addWidget(self.errorDisplay)
    
    def WordSubmit(self):
        # When the word is submitted, the first thing to do is to obtain the traduction.
        results = Mnain(self.wordInput.text(), self.originListwidget.row(self.originListwidget.currentItem()), self.targetListwidget.row(self.targetListwidget.currentItem()))
        self.manager.sharedData["results"] = results
        self.Next()
        return;


class ResultsWindow(UIFrame.UIWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Mnajik vII'
        self.setWindowTitle(self.title)
    
    def Resize(self) :
        screen = app.primaryScreen()
        windowHeight = 0
        windowHeight = screen.size().height() / 3
        windowHeight = int(max(100, min(400, windowHeight)))
        self.size = windowHeight
        windowWidth = windowHeight
        
        self.left = 725
        self.top = 425
        self.width = windowWidth
        self.height = windowHeight
        
        self.setGeometry(self.left, self.top, self.width, self.height)


    def InitUI(self):

        self.Resize()
        
        # create the layout first
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)    
        

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        ################################################################

        # now, we show the results of mnajik's translation, stored in the shared data of the window manager
        self.raw = QLabel("", self)
        self.raw.setAlignment(Qt.AlignCenter)
        self.raw.setStyleSheet("color : rgb(115, 0, 230)")
        self.raw.setFont(QFont('Oxygen', 16))
        self.layout.addWidget(self.raw)
        
        self.translation = QLabel("", self)
        self.translation.setAlignment(Qt.AlignCenter)
        self.translation.setStyleSheet("color : rgb(115, 0, 230)")
        self.translation.setFont(QFont('Oxygen', 16))
        self.layout.addWidget(self.translation)
        
        self.pair_split = QLabel("", self)
        self.pair_split.setAlignment(Qt.AlignCenter)
        self.pair_split.setStyleSheet("color : rgb(115, 0, 230)")
        self.pair_split.setFont(QFont('Oxygen', 14))
        self.layout.addWidget(self.pair_split)
        
        

        
        # results returns [translatedWord, singleWord, pairSplit, syllabSplit, VowelStrip, exampleSentences]
        
        return;
        
    
    def Reload(self) :
        
        if (not "results" in self.manager.sharedData) :
            return
        
        results = self.manager.sharedData["results"]
        
        self.raw.setText("Input word : " + results.raw_word)
        self.translation.setText("Translated word : " + results.translated_word)
        
        temp_str = ""
        for i in range(0, len(results.pair_split), 2) :
            temp_str = temp_str + str(results.pair_split[i]) + "-"
        temp_str = temp_str[:-1]
        
        self.pair_split.setText(temp_str)
        
    
    def createLabels(self, index) :
        
        if (len(self.results[index]) == 0) :
            return;
        
        # apparently this create an error because some results are not always a string
        print("label : ", self.results[index])
        
        thing = self.results[index]
        
        if (isinstance(thing[0], (list, tuple, np.ndarray))) :
            for i in range(len(thing)) :
                self.createLabel(thing[i][0])
        else :
            self.createLabel(thing[0])
            
        
    
    def createLabel(self, string) :
        label = QLabel(string, self)
        
        label.setStyleSheet("color: rgb(115, 0, 230)")
        label.setFont(QFont('Oxygen', 14))
        
        self.layout.addWidget(label)
        


    def getText(self): #For entering word
        text, okPressed = QInputDialog.getText(self, "Mnajik vII","Enter origin word:", QLineEdit.Normal, "")
        if okPressed and text != '':
            self.input_word = text
        else:

            sys.exit(app.exec_())
    
    def clicked(self):
        print("next")
        self.w = app4(self.size, self.results)
        self.w.show()
        self.hide()
        
            


class app4(UIFrame.UIWindow):
    # this class is a fourth app window
    # it will be used to present some sentences examples
    
    
    def __init__(self, size, results):
        super().__init__()
        self.title = 'Mnajik vII'
        self.left = 725
        self.top = 425
        self.width = size
        self.height = size
        
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.results = results;

        self.initUI()
        
    def initUI(self):
        
        # create the layout first
        self.layout = QVBoxLayout()
        self.setLayout(self.layout) 
        
        # Then, we add the title
        self.title = QLabel("Examples : ", self)
        self.title.setFont(QFont('Oxygen', 17))
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        
        # first, get examples
        self.examples = self.results[5]
        print(self.examples)
        
        if (len(self.examples) == 0) :
            # doesn't displays anything else if there is no examples
            return;
    
        example = self.examples[random.randint(0, len(self.examples)-1)]
        print(example)
        
        # display the original language example
        
        self.exampleSRC = QLabel(example["src"], self)
        self.exampleSRC.setFont(QFont('Oxygen', 15))
        self.exampleSRC.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.exampleSRC)
        
        # displays dest language example
        
        self.exampleDST = QLabel(example["dst"], self)
        self.exampleDST.setFont(QFont('Oxygen', 15))
        self.exampleDST.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.exampleDST)
        
            
        
        
        


# this block of code will run only if this is the main program, not if it is imported as a module.
if __name__ == '__main__':
    windowManager = UIFrame.WindowManager()
    app = QApplication(sys.argv)
    windowManager.Initialize((InputWindow(), ResultsWindow()), app)
    windowManager.Switch(0)
    #ex = App1(app)
    #ex.show()
    sys.exit(app.exec_())
