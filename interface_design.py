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
        
        self.sac_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.sac_label.setAlignment(QtCore.Qt.AlignCenter)
        self.sac_label.setObjectName("sac_label")
        
        self.verticalLayout.addWidget(self.sac_label)       
        self.sac_text = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.sac_text.setObjectName("sac_text")       
        self.verticalLayout.addWidget(self.sac_text)

        self.akma_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.akma_label.setAlignment(QtCore.Qt.AlignCenter)  
        self.akma_label.setObjectName("akma_label")  
        self.verticalLayout.addWidget(self.akma_label)
        self.akma_text = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.akma_text.setObjectName("akma_text")     
        self.verticalLayout.addWidget(self.akma_text)
        
        self.cekme_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.cekme_label.setAlignment(QtCore.Qt.AlignCenter)
        self.cekme_label.setObjectName("cekme_label")       
        self.verticalLayout.addWidget(self.cekme_label)      
        self.cekme_text = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.cekme_text.setObjectName("cekme_text")
        self.verticalLayout.addWidget(self.cekme_text)
      
        self.kalip_label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.kalip_label.setAlignment(QtCore.Qt.AlignCenter)
        self.kalip_label.setObjectName("kalip_label")       
        self.verticalLayout.addWidget(self.kalip_label)      
        self.kalip_text = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.kalip_text.setObjectName("kalip_text")     
        self.verticalLayout.addWidget(self.kalip_text)

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
        self.sac_label.setText(_translate("MainWindow", "Sac Kalınlığı (mm)"))
        self.akma_label.setText(_translate("MainWindow", "Akma Mukavvemeti (mpa)"))
        self.cekme_label.setText(_translate("MainWindow", "Çekme Mukavvemeti (mpa)"))
        self.kalip_label.setText(_translate("MainWindow", "Kalıp Ağırlığı (Ton)"))
        self.output_label.setText(_translate("MainWindow", "Tahmini Maliyet (Euro)"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
