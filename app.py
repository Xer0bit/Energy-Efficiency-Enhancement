import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QColor
from predict import predict_normal_efficiency, predict_enhanced_efficiency


class DeviceEfficiencyGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Device Efficiency Calculator')
        self.setGeometry(100, 100, 500, 400)

        # Device name input
        self.device_name_label = QLabel('Device name:', self)
        self.device_name_label.move(50, 50)
        self.device_name_input = QLineEdit(self)
        self.device_name_input.move(250, 50)

        # Minimum consumption input
        self.min_consumption_label = QLabel('Minimum consumption:', self)
        self.min_consumption_label.move(50, 100)
        self.min_consumption_input = QLineEdit(self)
        self.min_consumption_input.move(250, 100)

        # Maximum consumption input
        self.max_consumption_label = QLabel('Maximum consumption:', self)
        self.max_consumption_label.move(50, 150)
        self.max_consumption_input = QLineEdit(self)
        self.max_consumption_input.move(250, 150)

        # Calculate button
        self.calculate_button = QPushButton('Calculate', self)
        self.calculate_button.move(200, 220)
        self.calculate_button.clicked.connect(self.calculate_efficiency)

        # Device name label
        self.device_name_output_label = QLabel('', self)
        self.device_name_output_label.setGeometry(50, 280, 400, 30)
        self.device_name_output_label.setStyleSheet('QLabel {background-color: #d9e4f1; color: black; font-weight: bold;}')

        # Normal efficiency label
        self.normal_efficiency_output_label = QLabel('', self)
        self.normal_efficiency_output_label.setGeometry(50, 320, 400, 30)
        self.normal_efficiency_output_label.setStyleSheet('QLabel {background-color: #d9e4f1; color: black; font-weight: bold;}')

        # Enhanced efficiency label
        self.enhanced_efficiency_output_label = QLabel('', self)
        self.enhanced_efficiency_output_label.setGeometry(50, 360, 400, 30)
        self.enhanced_efficiency_output_label.setStyleSheet('QLabel {background-color: #d9e4f1; color: black; font-weight: bold;}')

        self.show()

    def calculate_efficiency(self):
        device_name = self.device_name_input.text()
        min_consumption = float(self.min_consumption_input.text())
        max_consumption = float(self.max_consumption_input.text())


        if not device_name or not min_consumption or not max_consumption:
            self.normal_efficiency_output_label.setText('Error: All fields are required')
            self.enhanced_efficiency_output_label.setText('Error: All fields are required')
            return
        



        if min_consumption > max_consumption:
            self.normal_efficiency_output_label.setText('Error: Minimum consumption must be less than maximum consumption')
            self.enhanced_efficiency_output_label.setText('Error: Minimum consumption must be less than maximum consumption')
            return

        
        normal_efficiency = predict_normal_efficiency(min_consumption, max_consumption)
        self.normal_efficiency_output_label.setText(f'Normal efficiency: {normal_efficiency}')

        
        # Calculate enhanced efficiency
        enhanced_efficiency = predict_enhanced_efficiency(min_consumption, max_consumption)
        self.enhanced_efficiency_output_label.setText(f'Enhanced efficiency: {enhanced_efficiency}')

        print(f'Device name: {device_name}')
        print(f'Normal efficiency: {normal_efficiency}')
        print(f'Enhanced efficiency: {enhanced_efficiency}')

        # Display device name
        self.device_name_output_label.setText(f'Device name: {device_name}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    device_efficiency_gui = DeviceEfficiencyGUI()
    sys.exit(app.exec_())
