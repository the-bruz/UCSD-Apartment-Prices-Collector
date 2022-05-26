import sys
from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QPushButton, QWidget\
                            ,QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
import price_collector
from tabulate import tabulate

def search():
    apt_list = ''
    curr = comm_box.currentText()
    if(curr ==  'Costa Verde Village'):  apt_list = price_collector.collect_cvv()
    if(curr ==  'Towers at Costa Verde'):  apt_list = price_collector.collect_towers()
    if(curr ==  '360 Luxury'):  apt_list = price_collector.collect_360_lux()
    if(curr ==  'Lux UTC'):  apt_list = price_collector.collect_lux()
    if(curr ==  'La Jolla Crossroads'):  apt_list = price_collector.collect_crossroads()
    if(curr ==  'La Regencia'):  apt_list = price_collector.collect_la_regencia()
    if(curr ==  'Regents La Jolla'):  apt_list = price_collector.collect_regents_la_jolla()
    if(curr == 'Regents Court'): apt_list = price_collector.collect_regents_court()
    infos = list_info(apt_list)
    if (infos == 'No avaliable apartment found.'): result_label.setText(infos)
    else: result_label.setText(tabulate(infos))

def list_info(list):
    if (len(list) == 0):
        return 'No avaliable apartment found.'
    info = []
    info.append(list[0].table_header())
    for a in list:
        info.append(a.info_table())
    return info


app = QApplication([])
app.setStyle('Fusion')

comm_box = QComboBox()
comm_box.addItems(['Costa Verde Village', 'Towers at Costa Verde', '360 Luxury', 
'Lux UTC', 'La Jolla Crossroads', 'La Regencia', 'Regents La Jolla', 'Regents Court'])
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