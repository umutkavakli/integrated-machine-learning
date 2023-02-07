from PyQt5.QtWidgets import *
from interface_design import Ui_MainWindow
from model_loader import ModelLoader
import numpy as np
import warnings

warnings.filterwarnings('ignore')

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.click_button)
        self.model = ModelLoader()

    def predict_output(self, sheet_thickness: float, yield_strength: float, tensile_strength: float, mold_weight: float):
        self.ui.output_text.setText(str(self.model.model.predict(np.array([sheet_thickness, yield_strength, tensile_strength, mold_weight]).reshape(1, -1))))
 

    def click_button(self):
        sheet_thickness = float(self.ui.sheet_text.toPlainText())
        yield_strength = float(self.ui.yield_text.toPlainText())
        tensile_strength = float(self.ui.tensile_text.toPlainText())
        mold_weight = float(self.ui.mold_text.toPlainText())

        self.model.set_model(self.ui.comboBox.currentText())

        self.predict_output(sheet_thickness, yield_strength, tensile_strength, mold_weight)


if __name__ == '__main__':
    app = QApplication([])
    window = GUI()
    window.show()
    app.exec()