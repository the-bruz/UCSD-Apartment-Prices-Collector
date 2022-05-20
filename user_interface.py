import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import rent_collector

def search():
    apt_list = ''
    match comm_box.currentText():
        case 'Costa Verde Village':
            apt_list = rent_collector.collect_cvv()
        case 'Towers at Costa Verde':
            apt_list = rent_collector.collect_towers()
        case '360 Luxury':
            apt_list = rent_collector.collect_360_lux()
        case 'Lux UTC':
            apt_list = rent_collector.collect_lux()
        case 'La Jolla Crossroads':
            apt_list = rent_collector.collect_crossroads()
        case 'La Regencia':
            apt_list = rent_collector.collect_la_regencia()
    infos = list_info(apt_list)
    result_label.setText(infos)

def list_info(list):
    if (len(list) == 0):
        return "No avaliable apartment found."
    info = ""
    for a in list:
        info += a.info() + '\n'
    return info


app = QApplication([])
app.setStyle('Fusion')

comm_box = QComboBox()
comm_box.addItems(['Costa Verde Village', 'Towers at Costa Verde', '360 Luxury', 
'Lux UTC', 'La Jolla Crossroads', 'La Regencia'])
comm_label = QLabel("Community:")
comm_label.setBuddy(comm_box)

search_button = QPushButton('Search')
result_label = QLabel()
search_button.clicked.connect(search)

top_widget = QWidget()
top_layout = QHBoxLayout()
top_layout.addWidget(comm_label)
top_layout.addWidget(comm_box, Qt.AlignLeft)
top_layout.addWidget(search_button)
top_widget.setLayout(top_layout)


window = QWidget()
window_layout = QVBoxLayout()
window_layout.setAlignment(Qt.AlignTop)
window_layout.addWidget(top_widget)
window_layout.addWidget(result_label)
window.setLayout(window_layout)
window.setFixedWidth(1000)
window.setFixedHeight(600)
window.show()
app.setWindowIcon(QIcon('icon.ico'))
app.exec()