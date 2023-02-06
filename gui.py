from PyQt5.QtWidgets import *
from interface_design import Ui_MainWindow
from model import Model
import numpy as np

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click_button)
        self.model = Model()
        self.model.preprocessing()
        self.model.train_model()

    def predict_output(self, sac: float, akma: float, cekme: float, kalip: float):
        self.ui.output_text.setText(str(self.model.model_predict(np.array([sac, akma, cekme, kalip]).reshape(1, -1))))
 

    def click_button(self):
        sheet_thickness = float(self.ui.sheet_text.toPlainText())
        yield_strength = float(self.ui.yield_text.toPlainText())
        tensile_strength = float(self.ui.tensile_text.toPlainText())
        mold_weight = float(self.ui.mold_text.toPlainText())

        self.predict_output(sheet_thickness, yield_strength, tensile_strength, mold_weight)

    # def web_server(self, sheet_thickness, yield_strength, tensile_value, mold_value):
    #     self.ui.sac_text.setText(sheet_thickness)
    #     self.ui.akma_text.setText(yield_strength)
    #     self.ui.cekme_text.setText(tensile_value)
    #     self.ui.kalip_text.setText(mold_value)

    #     self.predict_output(sheet_thickness, yield_strength, tensile_value, mold_value)

if __name__ == '__main__':
    app = QApplication([])
    window = GUI()
    window.show()
    app.exec()