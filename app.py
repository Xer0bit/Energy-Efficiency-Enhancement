import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt6.QtGui import QColor
from predict import predict_normal_efficiency, predict_enhanced_efficiency


class DeviceEfficiencyGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('Device Efficiency Calculator - Taha Imtiaz', self)
        title.move(50, 10)
        title.setStyleSheet('QLabel {background-color: #d9e4f1; color: black; font-weight: bold;}')

        # Device name input
        self.device_name_label = QLabel('Device name:', self)
        self.device_name_label.move(50, 50)
        self.device_name_input = QLineEdit(self)
        self.device_name_input.setGeometry(250, 50, 200, 30)

        # Minimum consumption input
        self.min_consumption_label = QLabel('Minimum consumption:', self)
        self.min_consumption_label.move(50, 100)
        self.min_consumption_input = QLineEdit(self)
        self.min_consumption_input.setGeometry(250, 100, 200, 30)

        # Maximum consumption input
        self.max_consumption_label = QLabel('Maximum consumption:', self)
        self.max_consumption_label.move(50, 150)
        self.max_consumption_input = QLineEdit(self)
        self.max_consumption_input.setGeometry(250, 150, 200, 30)

        # Input power input
        self.input_power_label = QLabel('Input power:', self)
        self.input_power_label.move(50, 200)
        self.input_power_input = QLineEdit(self)
        self.input_power_input.setGeometry(250, 200, 200, 30)
        
        # Calculate button
        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.setGeometry(200, 250, 100, 30)
        self.calculate_button.clicked.connect(self.calculate_efficiency)

        # Device name label
        self.device_name_output_label = QLabel('', self)
        self.device_name_output_label.setGeometry(50, 300, 400, 30)
        self.device_name_output_label.setStyleSheet('QLabel {background-color: #d9e4f1; color: black; font-weight: bold;}')

        # Normal efficiency label
        self.normal_efficiency_output_label = QLabel('', self)
        self.normal_efficiency_output_label.setGeometry(50, 340, 400, 30)
        self.normal_efficiency_output_label.setStyleSheet('QLabel {background-color: #d9e4f1; color: black; font-weight: bold;}')

        # Enhanced efficiency label
        self.enhanced_efficiency_output_label = QLabel('', self)
        self.enhanced_efficiency_output_label.setGeometry(50, 380, 400, 30)
        self.enhanced_efficiency_output_label.setStyleSheet('QLabel {background-color: #d9e4f1; color: black; font-weight: bold;}')
        self.show()
        



    def calculate_efficiency(self):
        device_name = self.device_name_input.text()
        min_consumption = float(self.min_consumption_input.text())
        max_consumption = float(self.max_consumption_input.text())
        input_power = float(self.input_power_input.text())

        #creat error message on improper input
        if min_consumption > max_consumption:
            self.device_name_output_label.setText('Minimum consumption cannot be greater than maximum consumption')
            print('Minimum consumption cannot be greater than maximum consumption')
            self.normal_efficiency_output_label.setText('')
            self.enhanced_efficiency_output_label.setText('')
            return
        if input_power > max_consumption:
            self.device_name_output_label.setText('Input power cannot be greater than maximum consumption')
            print('Input power cannot be greater than maximum consumption')
            self.normal_efficiency_output_label.setText('')
            self.enhanced_efficiency_output_label.setText('')
            return
        if input_power < min_consumption:
            self.device_name_output_label.setText('Input power cannot be less than minimum consumption')
            print('Input power cannot be less than minimum consumption')
            self.normal_efficiency_output_label.setText('')
            self.enhanced_efficiency_output_label.setText('')
            return
        if min_consumption < 0 or max_consumption < 0 or input_power < 0:
            self.device_name_output_label.setText('Input cannot be less than 0')
            print('Input cannot be less than 0')
            self.normal_efficiency_output_label.setText('')
            self.enhanced_efficiency_output_label.setText('')
            return
        #if input is valid is 0
        if min_consumption == 0 or max_consumption == 0 or input_power == 0:
            self.device_name_output_label.setText('Input cannot be 0')
            print('Input cannot be 0')
            self.normal_efficiency_output_label.setText('')
            self.enhanced_efficiency_output_label.setText('')
            return


        normal_efficiency = predict_normal_efficiency(min_consumption, max_consumption, input_power)
        enhanced_efficiency = predict_enhanced_efficiency(min_consumption, max_consumption, input_power)

        self.device_name_output_label.setText(f'Device name: {device_name}')
        self.normal_efficiency_output_label.setText(f'Normal efficiency: {normal_efficiency}')
        self.enhanced_efficiency_output_label.setText(f'Enhanced efficiency: {enhanced_efficiency}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = DeviceEfficiencyGUI()
    sys.exit(app.exec())
