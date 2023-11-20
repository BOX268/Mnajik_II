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

    def __init__(self, app):
        super().__init__()
        
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.title = 'Mnajik vII'
        
        
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

        self.listwidget.clicked.connect(self.clicked) #connect to window2
        self.listwidget.clicked.connect(self.window2) #connect to window2
        self.layout.addWidget(self.listwidget)
        self.setFocus()


    def initUI(self) :

        # first, resize the window
        self.Resize();

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
    
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

    def clicked(self, qmodelindex):
        item = self.listwidget.currentItem()
        #print( self.listwidget.row(item)  )
        self.index1 =  self.listwidget.row(item)


    def window2(self):                                             # <===
        self.w = App2(self.index1)
        self.w.show()
        self.hide()


class App2(UIFrame.UIWindow):

    def __init__(self, index1):
        super().__init__()

        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.index1 = index1
        
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
        self.listwidget.clicked.connect(self.window2) #connect to window2
        self.layout.addWidget(self.listwidget)

        self.initUI()


    def initUI(self):

        self.Resize()
        
        self.title = 'Mnajik vII'

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.InitBackButton(self.layout)
        self.show()
    
    
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

    def clicked(self, qmodelindex):
        item = self.listwidget.currentItem()
        #print( self.listwidget.row(item)  )
        self.index2 =  self.listwidget.row(item)


    def window2(self):                                             # <===
        self.w = App3(self.index1, self.index2, self.size)
        self.w.show()
        self.hide()


class App3(UIFrame.UIWindow):

    def __init__(self, index1, index2, size):
        super().__init__()
        self.title = 'Mnajik vII'
        self.left = 725
        self.top = 425
        self.width = size
        self.height = size
        self.size = size

        self.initUI(index1, index2)

    def initUI(self, index1, index2):

        # create the layout first
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)        

        self.label_1 = QLabel('Translated Word:  ', self)
        #
        self.layout.addWidget(self.label_1)

        # setting up background color

        # setting font and size
        self.label_1.setFont(QFont('Oxygen', 15))
    
        

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.getText()

        ################################################################

        #run text through mnajik and return results.
        
        

        self.results = Mnain(self.input_word, index1, index2)
        # results returns [translatedWord, singleWord, pairSplit, syllabSplit, VowelStrip, exampleSentences]
        
        # add the translated word
        self.transWord = QLabel(self.results[0], self) #Translated word
        self.transWord.setStyleSheet("color: rgb(115, 0, 230)")
        self.transWord.setFont(QFont('Oxygen', 14))
        self.layout.addWidget(self.transWord)
        

        # add the title, and then all of the mnemonic outputs.
        self.label_2 = QLabel('Mnemonic outputs:  ', self)
        #
        self.layout.addWidget(self.label_2)

        # setting font and size
        self.label_2.setFont(QFont('Oxygen', 15))
        
        # the last slot is for the example sentences
        
        for result in range(1, len(self.results)-1) :
            self.createLabels(result)
        
        # adds a push button that allows to switch to the last window, showing axample sentences
        
        button = QPushButton("Next", self)
        button.clicked.connect(self.clicked)
        self.layout.addWidget(button)

        self.show()
        return;
        
        # EVERYTHING UNDER THIS LINE IS LEGACY CODE

        self.label_3 = QLabel(results[0], self) #Translated word
        # moving position
        self.label_3.move(50, 25)

        self.label_3.setStyleSheet("color: rgb(115, 0, 230)")

        # setting font and size
        self.label_3.setFont(QFont('Oxygen', 14))

        print(results[1])
        print("\n")

        if results[1] != []: #single word

            self.label_4 = QLabel(results[1][0] , self)
            # moving position
            self.label_4.move(50, 75)
            self.label_4.setStyleSheet("color: rgb(115, 0, 230)")
            # setting font and size
            self.label_4.setFont(QFont('Oxygen', 14))

        print(results[2])
        print("\n")

        if len(results[2]) > 0: #pair split

            self.label_5 = QLabel(results[2][0] , self)
            # moving position
            self.label_5.move(50, 100)
            self.label_5.setStyleSheet("color: rgb(115, 0, 230)")
            # setting font and size
            self.label_5.setFont(QFont('Oxygen', 14))

            #one label for each pair (Learn how to have many)

            self.label_5p = QLabel(results[2][2] , self)
            # moving position
            self.label_5p.move(120, 100)
            self.label_5p.setStyleSheet("color: rgb(115, 0, 230)")
            # setting font and size
            self.label_5p.setFont(QFont('Oxygen', 14))

        print(results[3])
        print("\n")

        if len(results[3]) > 0:

            self.label_6 = QLabel(results[3][0] , self)
            # moving position
            self.label_6.move(50, 125)
            self.label_6.setStyleSheet("color: rgb(115, 0, 230)")
            # setting font and size
            self.label_6.setFont(QFont('Oxygen', 14))

        print(results[4])

        if len(results[4]) > 0:

            self.label_7 = QLabel(results[4][0] , self)
            # moving position
            self.label_7.move(50, 150)
            self.label_7.setStyleSheet("color: rgb(115, 0, 230)")
            # setting font and size
            self.label_7.setFont(QFont('Oxygen', 14))
        #######################################################

        qbtn = QPushButton('Quit', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.move(70, 175)

        self.show()

        self.show()
        
    
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
    ex = App1(app)
    ex.show()
    sys.exit(app.exec_())
