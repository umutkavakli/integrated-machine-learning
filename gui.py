from PyQt5.QtWidgets import *
from interface_design import Ui_MainWindow

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click_button)

    def click_button(self):
        sac_value = int(self.ui.sac_text.toPlainText())
        akma_value = int(self.ui.akma_text.toPlainText())
        cekme_value = int(self.ui.cekme_text.toPlainText())
        kalip_value = int(self.ui.kalip_text.toPlainText())

        self.ui.output_text.setText(str(sac_value+akma_value+cekme_value+kalip_value))

app = QApplication([])
window = GUI()
window.show()
app.exec_()




