from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(600, 0, 200, 120))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("icons/Inzva-space.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")

        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 130, 671, 394))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.sheet_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.sheet_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sheet_label.setObjectName("sheet_label")
        
        self.verticalLayout.addWidget(self.sheet_label)       
        self.sheet_text = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.sheet_text.setObjectName("sheet_text")       
        self.verticalLayout.addWidget(self.sheet_text)

        self.yield_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.yield_label.setAlignment(QtCore.Qt.AlignCenter)  
        self.yield_label.setObjectName("yield_label")  
        self.verticalLayout.addWidget(self.yield_label)
        self.yield_text = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.yield_text.setObjectName("yield_text")     
        self.verticalLayout.addWidget(self.yield_text)
        
        self.tensile_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.tensile_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tensile_label.setObjectName("tensile_label")       
        self.verticalLayout.addWidget(self.tensile_label)      
        self.tensile_text = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.tensile_text.setObjectName("tensile_text")
        self.verticalLayout.addWidget(self.tensile_text)
      
        self.mold_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.mold_label.setAlignment(QtCore.Qt.AlignCenter)
        self.mold_label.setObjectName("mold_label")       
        self.verticalLayout.addWidget(self.mold_label)      
        self.mold_text = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.mold_text.setObjectName("mold_text")     
        self.verticalLayout.addWidget(self.mold_text)

        self.horizontalLayout.addLayout(self.verticalLayout)
    
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)    
        self.horizontalLayout.addItem(spacerItem)
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")  
        spacerItem1 = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        
        self.output_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.output_label.setAlignment(QtCore.Qt.AlignCenter)
        self.output_label.setObjectName("output_label")  
        self.verticalLayout_2.addWidget(self.output_label)     
        self.output_text = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.output_text.setFrameShape(QtWidgets.QFrame.Box)
        self.output_text.setText("")
        self.output_text.setTextFormat(QtCore.Qt.AutoText)
        self.output_text.setAlignment(QtCore.Qt.AlignCenter)
        self.output_text.setObjectName("output_text")    
        self.verticalLayout_2.addWidget(self.output_text)
        
        spacerItem2 = QtWidgets.QSpacerItem(20, 250, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
    
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(MainWindow.click_button)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.sheet_label.setText(_translate("MainWindow", "Sheet Thickness (mm)"))
        self.yield_label.setText(_translate("MainWindow", "Yield Strength (mpa)"))
        self.tensile_label.setText(_translate("MainWindow", "Tensile Strength (mpa)"))
        self.mold_label.setText(_translate("MainWindow", "Mold Weight (Tons)"))
        self.output_label.setText(_translate("MainWindow", "Cost Prediction (Euro)"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
