#This Python file uses the following encoding: utf-8
import os
import sys
from PySide6.QtCore import Qt,QDir
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QWidget, QToolButton, QPushButton, QFileDialog, QGridLayout, QRadioButton, QButtonGroup, QListWidget, QLabel, QCheckBox, QListWidgetItem, QMessageBox, QSpinBox,QComboBox
def mix():
	widget.close()
	global add2
	add2=QWidget()
	add2.setWindowTitle('整体或混合式贴标')
	add2.resize(1280,960)
	add2.setFixedSize(add2.width(),add2.height())
	add2.layout=QGridLayout(add2)
	add2.button0=QPushButton("写入")
	add2.button1=QPushButton("清除本文件")
	add2.button3=QPushButton("返回")
	add2.button4=QPushButton("目录")
	add2.label0=QLabel(selected)
	add2.label1=QLabel("结构类型：")
	add2.label11=QLabel("倒塌详情：")
	add2.label2=QLabel("部件：")
	add2.label21 = QLabel("无损")
	add2.label22 = QLabel("有损")
	add2.label3=QLabel("破坏类型：")
	add2.label4=QLabel("破坏程度：")
	add2.label5=QLabel()
	add2.label6=QLabel('历史记录：')
	add2.radio_button00=QRadioButton('钢混')
	add2.radio_button01=QRadioButton('砖混')
	add2.group0=QButtonGroup()
	add2.group0.addButton(add2.radio_button00)
	add2.group0.addButton(add2.radio_button01)
	add2.radio_button2 = QRadioButton('无')
	add2.radio_button3 = QRadioButton('部分')
	add2.radio_button4 = QRadioButton('全部')
	add2.group00 = QButtonGroup()
	add2.group00.addButton(add2.radio_button2)
	add2.group00.addButton(add2.radio_button3)
	add2.group00.addButton(add2.radio_button4)
	add2.radio_button03=QRadioButton('梁')
	add2.radio_button04=QRadioButton('柱')
	add2.radio_button05=QRadioButton('墙')
	add2.radio_button06=QRadioButton('楼板')
	add2.radio_button090=QRadioButton('支撑')
	add2.radio_button11=QRadioButton('无明显')
	add2.radio_button12=QRadioButton('轻微')
	add2.radio_button13=QRadioButton('中等')
	add2.radio_button14=QRadioButton('严重')
	add2.radio_button15=QRadioButton('完全')
	add2.group1=QButtonGroup()
	add2.group1.addButton(add2.radio_button03)
	add2.group1.addButton(add2.radio_button04)
	add2.group1.addButton(add2.radio_button05)
	add2.group1.addButton(add2.radio_button06)
	add2.group1.addButton(add2.radio_button090)
	add2.spin1=QSpinBox()
	add2.spin2=QSpinBox()
	add2.radio_button09=QRadioButton('有损伤')
	add2.radio_button10=QRadioButton('无明显')
	add2.group2=QButtonGroup()
	add2.group2.addButton(add2.radio_button09)
	add2.group2.addButton(add2.radio_button10)
	add2.group3=QButtonGroup()
	add2.group3.addButton(add2.radio_button11)
	add2.group3.addButton(add2.radio_button12)
	add2.group3.addButton(add2.radio_button13)
	add2.group3.addButton(add2.radio_button14)
	add2.group3.addButton(add2.radio_button15)
	add2.check2=QCheckBox("裂缝")
	add2.check3=QCheckBox("饰面脱落")
	add2.check4=QCheckBox("砼剥落")
	add2.check40=QCheckBox("砖块碎落")
	add2.check5=QCheckBox("钢筋裸露")
	add2.list_widget=QListWidget()
	add2.combo=QComboBox()
	add2.layout.addWidget(add2.label1,1,0)
	add2.layout.addWidget(add2.label11,4,0)
	add2.layout.addWidget(add2.label2,8,0)
	add2.layout.addWidget(add2.label3,18,0)
	add2.layout.addWidget(add2.label4,26,0)
	add2.layout.addWidget(add2.radio_button2,5,0)
	add2.layout.addWidget(add2.radio_button3,6,0)
	add2.layout.addWidget(add2.radio_button4,7,0)
	add2.layout.addWidget(add2.radio_button00,2,0)
	add2.layout.addWidget(add2.radio_button01,3,0)
	add2.layout.addWidget(add2.radio_button03,9,0)
	add2.layout.addWidget(add2.radio_button04,10,0)
	add2.layout.addWidget(add2.radio_button05,11,0)
	add2.layout.addWidget(add2.radio_button06,12,0)
	add2.layout.addWidget(add2.radio_button090,13,0)
	add2.layout.addWidget(add2.label21,14,0)
	add2.layout.addWidget(add2.spin1,15,0)
	add2.layout.addWidget(add2.label22,16,0)
	add2.layout.addWidget(add2.spin2,17,0)
	add2.layout.addWidget(add2.radio_button09,20,0)
	add2.layout.addWidget(add2.radio_button10,19,0)
	add2.layout.addWidget(add2.radio_button11,27,0)
	add2.layout.addWidget(add2.radio_button12,28,0)
	add2.layout.addWidget(add2.radio_button13,29,0)
	add2.layout.addWidget(add2.radio_button14,30,0)
	add2.layout.addWidget(add2.radio_button15,31,0)
	add2.layout.addWidget(add2.button0,32,0)
	add2.layout.addWidget(add2.button1,33,0)
	add2.layout.addWidget(add2.button3,34,0)
	add2.layout.addWidget(add2.button4,0,0)
	add2.layout.addWidget(add2.check2,21,0)
	add2.layout.addWidget(add2.check3,22,0)
	add2.layout.addWidget(add2.check4,23,0)
	add2.layout.addWidget(add2.check40,24,0)
	add2.layout.addWidget(add2.check5,25,0)
	add2.radio_button03.setDisabled(True)
	add2.radio_button04.setDisabled(True)
	add2.radio_button05.setDisabled(True)
	add2.radio_button06.setDisabled(True)
	add2.radio_button090.setDisabled(True)
	add2.radio_button09.setDisabled(True)
	add2.radio_button10.setDisabled(True)
	add2.radio_button11.setDisabled(True)
	add2.radio_button12.setDisabled(True)
	add2.radio_button13.setDisabled(True)
	add2.radio_button14.setDisabled(True)
	add2.radio_button15.setDisabled(True)
	add2.check2.setDisabled(True)
	add2.check3.setDisabled(True)
	add2.check4.setDisabled(True)
	add2.check5.setDisabled(True)
	add2.check40.setDisabled(True)
	add2.radio_button2.setDisabled(True)
	add2.radio_button3.setDisabled(True)
	add2.radio_button4.setDisabled(True)
	for file_name in QDir(selected).entryList(['*.jpg'],QDir.Files|QDir.NoSymLinks):
		add2.combo.addItem(file_name)
	add2.group0.buttonToggled.connect(rgroup_0)
	add2.group00.buttonToggled.connect(rgroup00)
	add2.group00.buttonToggled.connect(rgroup03)
	add2.group0.buttonToggled.connect(rgroup01)
	add2.group1.buttonToggled.connect(rgroup01)
	add2.group1.buttonToggled.connect(rgroup02)
	add2.group1.buttonToggled.connect(cgroup_mix)
	add2.group2.buttonToggled.connect(rgroup02)
	add2.group2.buttonToggled.connect(rgroup03)
	add2.check4.stateChanged.connect(cgroup_mix)
	add2.check5.stateChanged.connect(cgroup_mix)
	add2.combo.activated.connect(display)
	add2.button0.clicked.connect(add_mix)
	add2.button1.clicked.connect(remove2)
	add2.button3.clicked.connect(close)
	add2.button4.clicked.connect(select)
	display()
	add2.layout.addWidget(add2.label0,0,1,1,2)
	add2.layout.addWidget(add2.label6,31,1)
	add2.layout.addWidget(add2.list_widget,32,1,3,1)
	add2.layout.addWidget(add2.combo,34,1)
	add2.show()
def partial():
	widget.close()
	global add1
	add1=QWidget()
	add1.setWindowTitle('结构局部')
	add1.resize(1280,960)
	add1.setFixedSize(add1.width(),add1.height())
	add1.layout=QGridLayout(add1)
	add1.button0=QPushButton("写入")
	add1.button1=QPushButton("清除本文件")
	add1.button3=QPushButton("返回")
	add1.button4=QPushButton("目录")
	add1.label0=QLabel(selected)
	add1.label1=QLabel("结构类型：")
	add1.label2=QLabel("部件：")
	add1.label3=QLabel("破坏类型：")
	add1.label4=QLabel("破坏程度：")
	add1.label5=QLabel()
	add1.label6=QLabel('历史记录：')
	add1.radio_button00=QRadioButton('钢混')
	add1.radio_button01=QRadioButton('砖混')
	add1.group0=QButtonGroup()
	add1.group0.addButton(add1.radio_button00)
	add1.group0.addButton(add1.radio_button01)
	add1.radio_button02=QRadioButton('其他')
	add1.radio_button03=QRadioButton('梁')
	add1.radio_button04=QRadioButton('柱')
	add1.radio_button05=QRadioButton('墙')
	add1.radio_button06=QRadioButton('楼板')
	add1.radio_button07=QRadioButton('屋盖')
	add1.radio_button08=QRadioButton('木制构件')
	add1.radio_button090=QRadioButton('阶梯')
	add1.radio_button11=QRadioButton('无')
	add1.radio_button12=QRadioButton('轻微')
	add1.radio_button13=QRadioButton('中等')
	add1.radio_button14=QRadioButton('严重')
	add1.radio_button15=QRadioButton('完全')
	add1.group1=QButtonGroup()
	add1.group1.addButton(add1.radio_button02)
	add1.group1.addButton(add1.radio_button03)
	add1.group1.addButton(add1.radio_button04)
	add1.group1.addButton(add1.radio_button05)
	add1.group1.addButton(add1.radio_button06)
	add1.group1.addButton(add1.radio_button07)
	add1.group1.addButton(add1.radio_button08)
	add1.group1.addButton(add1.radio_button090)
	add1.radio_button09=QRadioButton('有损伤')
	add1.radio_button10=QRadioButton('无明显')
	add1.group2=QButtonGroup()
	add1.group2.addButton(add1.radio_button09)
	add1.group2.addButton(add1.radio_button10)
	add1.group3=QButtonGroup()
	add1.group3.addButton(add1.radio_button11)
	add1.group3.addButton(add1.radio_button12)
	add1.group3.addButton(add1.radio_button13)
	add1.group3.addButton(add1.radio_button14)
	add1.group3.addButton(add1.radio_button15)
	add1.check0=QCheckBox("吊顶")
	add1.check1=QCheckBox("管道")
	add1.check2=QCheckBox("裂缝")
	add1.check3=QCheckBox("饰面脱落")
	add1.check4=QCheckBox("砼剥落")
	add1.check40=QCheckBox("砖块碎落")
	add1.check5=QCheckBox("钢筋裸露")
	add1.check6=QCheckBox("溜瓦")
	add1.check7=QCheckBox("坍塌")
	add1.list_widget=QListWidget()
	add1.combo=QComboBox()
	add1.layout.addWidget(add1.label1,1,0)
	add1.layout.addWidget(add1.label2,4,0)
	add1.layout.addWidget(add1.label3,15,0)
	add1.layout.addWidget(add1.label4,25,0)
	add1.layout.addWidget(add1.radio_button00,2,0)
	add1.layout.addWidget(add1.radio_button01,3,0)
	add1.layout.addWidget(add1.radio_button02,12,0)
	add1.layout.addWidget(add1.radio_button03,5,0)
	add1.layout.addWidget(add1.radio_button04,6,0)
	add1.layout.addWidget(add1.radio_button05,7,0)
	add1.layout.addWidget(add1.radio_button06,8,0)
	add1.layout.addWidget(add1.radio_button07,9,0)
	add1.layout.addWidget(add1.radio_button08,10,0)
	add1.layout.addWidget(add1.radio_button090,11,0)
	add1.layout.addWidget(add1.radio_button09,17,0)
	add1.layout.addWidget(add1.radio_button10,16,0)
	add1.layout.addWidget(add1.radio_button11,26,0)
	add1.layout.addWidget(add1.radio_button12,27,0)
	add1.layout.addWidget(add1.radio_button13,28,0)
	add1.layout.addWidget(add1.radio_button14,29,0)
	add1.layout.addWidget(add1.radio_button15,30,0)
	add1.layout.addWidget(add1.button0,31,0)
	add1.layout.addWidget(add1.button1,32,0)
	add1.layout.addWidget(add1.button3,33,0)
	add1.layout.addWidget(add1.button4,0,0)
	add1.layout.addWidget(add1.check0,13,0)
	add1.layout.addWidget(add1.check1,14,0)
	add1.layout.addWidget(add1.check2,18,0)
	add1.layout.addWidget(add1.check3,19,0)
	add1.layout.addWidget(add1.check4,20,0)
	add1.layout.addWidget(add1.check40,21,0)
	add1.layout.addWidget(add1.check5,22,0)
	add1.layout.addWidget(add1.check6,24,0)
	add1.layout.addWidget(add1.check7,23,0)
	add1.radio_button02.setDisabled(True)
	add1.radio_button03.setDisabled(True)
	add1.radio_button04.setDisabled(True)
	add1.radio_button05.setDisabled(True)
	add1.radio_button06.setDisabled(True)
	add1.radio_button07.setDisabled(True)
	add1.radio_button08.setDisabled(True)
	add1.radio_button090.setDisabled(True)
	add1.radio_button09.setDisabled(True)
	add1.radio_button10.setDisabled(True)
	add1.radio_button11.setDisabled(True)
	add1.radio_button12.setDisabled(True)
	add1.radio_button13.setDisabled(True)
	add1.radio_button14.setDisabled(True)
	add1.radio_button15.setDisabled(True)
	add1.check0.setDisabled(True)
	add1.check1.setDisabled(True)
	add1.check2.setDisabled(True)
	add1.check3.setDisabled(True)
	add1.check4.setDisabled(True)
	add1.check5.setDisabled(True)
	add1.check6.setDisabled(True)
	add1.check7.setDisabled(True)
	add1.check40.setDisabled(True)
	for file_name in QDir(selected).entryList(['*.jpg'],QDir.Files|QDir.NoSymLinks):
		add1.combo.addItem(file_name)
	add1.group0.buttonToggled.connect(rgroup0)
	add1.group0.buttonToggled.connect(rgroup1)
	add1.group1.buttonToggled.connect(rgroup1)
	add1.group1.buttonToggled.connect(rgroup2)
	add1.group1.buttonToggled.connect(cgroup)
	add1.group2.buttonToggled.connect(rgroup2)
	add1.group2.buttonToggled.connect(rgroup3)
	add1.check4.stateChanged.connect(cgroup)
	add1.check5.stateChanged.connect(cgroup)
	add1.combo.activated.connect(display)
	add1.button0.clicked.connect(add)
	add1.button1.clicked.connect(remove1)
	add1.button3.clicked.connect(close)
	add1.button4.clicked.connect(select)
	display()
	add1.layout.addWidget(add1.label0,0,1,1,2)
	add1.layout.addWidget(add1.label6,30,1)
	add1.layout.addWidget(add1.list_widget,31,1,3,1)
	add1.layout.addWidget(add1.combo,33,1)
	add1.show()
def rgroup_0():
	add2.radio_button2.setDisabled(False)
	add2.radio_button3.setDisabled(False)
	add2.radio_button4.setDisabled(False)
def rgroup0():
	add1.radio_button02.setDisabled(False)
	add1.radio_button03.setDisabled(False)
	add1.radio_button04.setDisabled(False)
	add1.radio_button05.setDisabled(False)
	add1.radio_button06.setDisabled(False)
	add1.radio_button090.setDisabled(False)
	if add1.radio_button01.isChecked():
		add1.radio_button07.setDisabled(False)
		add1.radio_button08.setDisabled(False)
	else:
		add1.group0.setExclusive(False)
		add1.radio_button07.setChecked(False)
		add1.radio_button08.setChecked(False)
		add1.group0.setExclusive(True)
		add1.radio_button07.setDisabled(True)
		add1.radio_button08.setDisabled(True)
		add1.check6.setChecked(False)
def add():
	if add1.group0.checkedButton().text():
		text=name+"　"+add1.group0.checkedButton().text()
		if add1.group1.checkedButton().text():
			text=text+"　"+add1.group1.checkedButton().text()
			try:
				with open(f'{name}.json',"r") as f:
					content=f.read()
			except IOError:
				content=''
			if add1.check0.isChecked():
				text=text+"　"+add1.check0.text()
				if content.find('More')==-1:
					if add1.radio_button09.isChecked():
						content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a non-structural component in a '+add1.group0.checkedButton().text()+' building. The component is a piece of celling. Under earthquake, the state of the celling was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced partial falling."},'
					else:
						content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a non-structural component in a '+add1.group0.checkedButton().text()+' building. The component is a piece of celling. Under earthquake, the state of the celling was undamaged."},'
				else:
					pos=content.find('"},')
					if add1.radio_button09.isChecked():
						content=content[:pos]+' And there is also a non-structural component in the '+add1.group0.checkedButton().text()+' building. The component is a piece of celling. Under earthquake, the state of the celling was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced partial falling.'+content[pos:]
					else:
						content=content[:pos]+' And there is also a non-structural component in the '+add1.group0.checkedButton().text()+' building. The component is a piece of celling. Under earthquake, the state of the celling was undamaged.'+content[pos:]
			if add1.check1.isChecked():
				text=text+"　"+add1.check1.text()
				if content.find('More')==-1:
					if add1.radio_button09.isChecked():
						content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a non-structural component in a '+add1.group0.checkedButton().text()+' building. The component is a piece of pipe. Under earthquake, the state of the pipe was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced the fracture of the pipe."},'
					else:
						content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a non-structural component in a '+add1.group0.checkedButton().text()+' building. The component is a piece of pipe. Under earthquake, the state of the pipe was undamaged."},'
				else:
					pos=content.find('"},')
					if add1.radio_button09.isChecked():
						content=content[:pos]+' And there is also a non-structural component in the '+add1.group0.checkedButton().text()+' building. The component is a piece of pipe. Under earthquake, the state of the pipe was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced the fracture of the pipe.'+content[pos:]
					else:
						content=content[:pos]+' And there is also a non-structural component in the '+add1.group0.checkedButton().text()+' building. The component is a piece of pipe. Under earthquake, the state of the pipe was undamaged.'+content[pos:]
			if add1.group2.checkedButton().text():
				text=text+"　"+add1.group2.checkedButton().text()
				if not add1.check0.isChecked() and not add1.check1.isChecked() and not add1.check2.isChecked() and not add1.check3.isChecked() and not add1.check4.isChecked() and not add1.check40.isChecked() and not add1.check5.isChecked() and not add1.check6.isChecked() and not add1.check7.isChecked():

					if content.find('More')==-1:
						content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a component in a '+add1.group0.checkedButton().text()+' building. The component is '+add1.group1.checkedButton().text()+' component. Under earthquake, the state of the '+add1.group1.checkedButton().text()+' component was '+add1.group3.checkedButton().text()+' damage."},'
					else:
						pos=content.find('"},')
						content=content[:pos]+' And there is also a component in the '+add1.group0.checkedButton().text()+' building. The component is '+add1.group1.checkedButton().text()+' component. Under earthquake, the state of the '+add1.group1.checkedButton().text()+' component was '+add1.group3.checkedButton().text()+' damage.'+content[pos:]
				elif not add1.check0.isChecked() and not add1.check1.isChecked():
					if content.find('More')==-1:
						if add1.radio_button00.isChecked() and add1.radio_button05.isChecked():
							content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a non-structural component in a '+add1.group0.checkedButton().text()+' building. The component is infilled '+add1.group1.checkedButton().text()+'. Under earthquake, the state of the infilled '+add1.group1.checkedButton().text()+' was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced ."},'
						else:
							content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a structural component in a '+add1.group0.checkedButton().text()+' building. The component is '+add1.group1.checkedButton().text()+'. Under earthquake, the state of the '+add1.group1.checkedButton().text()+' was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced ."},'
					else:
						pos=content.find('"},')
						if add1.radio_button00.isChecked() and add1.radio_button05.isChecked():
							content=content[:pos]+' And there is also a non-structural component in the '+add1.group0.checkedButton().text()+' building. The component is infilled '+add1.group1.checkedButton().text()+'. Under earthquake, the state of the infilled '+add1.group1.checkedButton().text()+' was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced .'+content[pos:]
						else:
							content=content[:pos]+' And there is also a structural component in the '+add1.group0.checkedButton().text()+' building. The component is '+add1.group1.checkedButton().text()+'. Under earthquake, the state of the '+add1.group1.checkedButton().text()+' was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced .'+content[pos:]
					if add1.check2.isChecked():
						text=text+"　"+add1.check2.text()
						initpos=content.find('experienced .')
						pos=content.find('."},')
						if pos!=-1:
							if initpos!=-1:
								content=content[:pos]+"cracks"+content[pos:]
							else:
								content=content[:pos]+", cracks"+content[pos:]
					if add1.check3.isChecked():
						text=text+"　"+add1.check3.text()
						initpos=content.find('experienced .')
						pos=content.find('."},')
						if pos!=-1:
							if initpos!=-1:
								content=content[:pos]+"facades spalling"+content[pos:]
							else:
								content=content[:pos]+", facades spalling"+content[pos:]
					if add1.check4.isChecked():
						text=text+"　"+add1.check4.text()
						initpos=content.find('experienced .')
						pos=content.find('."},')
						if pos!=-1:
							if initpos!=-1:
								content=content[:pos]+"concrete spalling"+content[pos:]
							else:
								content=content[:pos]+", concrete spalling"+content[pos:]
					if add1.check40.isChecked():
						text=text+"　"+add1.check40.text()
						initpos=content.find('experienced .')
						pos=content.find('."},')
						if pos!=-1:
							if initpos!=-1:
								content=content[:pos]+"bricks falling"+content[pos:]
							else:
								content=content[:pos]+" and bricks falling"+content[pos:]
					if add1.check5.isChecked():
						text=text+"　"+add1.check5.text()
						initpos=content.find('experienced .')
						pos=content.find('."},')
						if pos!=-1:
							if initpos!=-1:
								content=content[:pos]+"buckling of reinforcement bars"+content[pos:]
							else:
								content=content[:pos]+" and buckling of reinforcement bars"+content[pos:]
					if add1.check6.isChecked():
						text=text+"　"+add1.check6.text()
						initpos=content.find('experienced .')
						pos=content.find('."},')
						if pos!=-1:
							if initpos!=-1:
								content=content[:pos]+"slipping tiles"+content[pos:]
							else:
								content=content[:pos]+" and slipping tiles"+content[pos:]
					if add1.check7.isChecked():
						text=text+"　"+add1.check7.text()
						initpos=content.find('experienced .')
						pos=content.find('."},')
						if pos!=-1:
							if initpos!=-1:
								content=content[:pos]+"collapse"+content[pos:]
							else:
								content=content[:pos]+" and collapse"+content[pos:]
			text=text+"　"+add1.group3.checkedButton().text()
			item=QListWidgetItem(text)
			add1.list_widget.insertItem(0,item)
			add1.list_widget.setCurrentRow(0)
			content = content.replace('钢混', 'reinforced concrete')
			content = content.replace('砖混', 'masonry')
			content = content.replace('梁', 'beam')
			content = content.replace('柱', 'column')
			content = content.replace('墙', 'wall')
			content = content.replace('楼板', 'slab')
			content = content.replace('屋盖', 'roof')
			content = content.replace('木制构件', 'timber')
			content = content.replace('阶梯', 'stairway')
			content = content.replace('其他', 'non-structural')
			content = content.replace('无 damage', 'undamaged')
			content = content.replace('轻微', 'minor')
			content = content.replace('中等', 'moderate')
			content = content.replace('严重', 'heavy')
			content = content.replace('完全', 'complete')
			with open(f'{name}.json',"w") as f:
				f.writelines(content)
	exist(add1)
def add_mix():
	if add2.group0.checkedButton().text():
		text=name+"　"+add2.group0.checkedButton().text()
		num = add2.spin1.value() + add2.spin2.value()
		if num==0:
			text=text+"　"+add2.group00.checkedButton().text()
			content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a '+add2.group0.checkedButton().text()+' building. Under earthquake, the building has experienced '+add2.group00.checkedButton().text()+', the state of the building was '+add2.group3.checkedButton().text()+' damage."},'
		elif add2.group1.checkedButton().text():
			text=text+"　"+add2.group1.checkedButton().text()
			try:
				with open(f'{name}.json',"r") as f:
					content=f.read()
			except IOError:
				content=''
			if add2.group00.checkedButton().text():
				text = text+"　"+add2.group00.checkedButton().text()
				if add2.group2.checkedButton().text():
					text=text+"　"+add2.group2.checkedButton().text()
					if not add2.check2.isChecked() and add2.check3.isChecked() and not add2.check4.isChecked() and not add2.check40.isChecked() and not add2.check5.isChecked():
						if content.find('More')==-1:
							if add2.spin2.value()>1:
								content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a ' + add2.group0.checkedButton().text() + ' building. Under earthquake, the building has experienced ' + add2.group00.checkedButton().text() + '. More specifically, there are a total of '+str(num)+' '+add2.group1.checkedButton().text()+'s in the picture, including '+str(add2.spin1.value())+' undamaged '+add2.group1.checkedButton().text()+' and '+str(add2.spin2.value())+' damaged '+add2.group1.checkedButton().text()+'. Under earthquake, the state of the damaged component was '+add2.group3.checkedButton().text()+' damage."},'
							elif add2.spin2.value()==1:
								content = '{"image_id": "' + name + '",' + '"caption": "In this picture, there is a ' + add2.group0.checkedButton().text() + ' building. Under earthquake, the building has experienced ' + add2.group00.checkedButton().text() + '. More specifically, there is a total of ' + str(num) + ' ' + add2.group1.checkedButton().text() + ' in the picture, including ' +str(add2.spin1.value())+ ' undamaged ' + add2.group1.checkedButton().text() + ' and ' +str(add2.spin2.value())+ ' damaged ' + add2.group1.checkedButton().text() + '. Under earthquake, the state of the damaged component was ' + add2.group3.checkedButton().text() + ' damage."},'
							elif add2.spin2.value()==0 and num==1:
								content = '{"image_id": "' + name + '",' + '"caption": "In this picture, there is a ' + add2.group0.checkedButton().text() + ' building. Under earthquake, the building has experienced ' + add2.group00.checkedButton().text() + '. More specifically, there is a total of ' + str(num) + ' ' + add2.group1.checkedButton().text() + ' in the picture, including ' +str(add2.spin1.value())+ ' undamaged ' + add2.group1.checkedButton().text() + ' and ' +str(add2.spin2.value())+ ' damaged ' + add2.group1.checkedButton().text() + '. Under earthquake, the state of the component was ' + add2.group3.checkedButton().text() + ' damage."},'
							else:
								content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a ' + add2.group0.checkedButton().text() + ' building. Under earthquake, the building has experienced ' + add2.group00.checkedButton().text() + '. More specifically, there are a total of '+str(num)+' '+add2.group1.checkedButton().text()+'s in the picture, including '+str(add2.spin1.value())+' undamaged '+add2.group1.checkedButton().text()+' and '+str(add2.spin2.value())+' damaged '+add2.group1.checkedButton().text()+'. Under earthquake, the state of the component was '+add2.group3.checkedButton().text()+' damage."},'
						else:
							pos=content.find('"},')
							if add2.spin2.value()>1:
								content=content[:pos]+' And there are also a total of '+str(num)+' '+add2.group1.checkedButton().text()+'s in the picture, including '+str(add2.spin1.value())+' undamaged '+add2.group1.checkedButton().text()+' and '+str(add2.spin2.value())+' damaged '+add2.group1.checkedButton().text()+'. Under earthquake, the state of the damaged component was '+add2.group3.checkedButton().text()+' damage.'+content[pos:]
							elif add2.spin2.value() == 1:
								content=content[:pos]+' And there is also a total of ' + str(num) + ' ' + add2.group1.checkedButton().text() + ' in the picture, including ' +str(add2.spin1.value())+ ' undamaged ' + add2.group1.checkedButton().text() + ' and ' +str(add2.spin2.value())+ ' damaged ' + add2.group1.checkedButton().text() + '. Under earthquake, the state of the damaged component was ' + add2.group3.checkedButton().text() + ' damage.'+content[pos:]
							elif add2.spin2.value() == 0 and num == 1:
								content=content[:pos]+' And there is also a total of ' + str(num) + ' ' + add2.group1.checkedButton().text() + ' in the picture, including ' +str(add2.spin1.value())+ ' undamaged ' + add2.group1.checkedButton().text() + ' and ' +str(add2.spin2.value())+ ' damaged ' + add2.group1.checkedButton().text() + '. Under earthquake, the state of the component was ' + add2.group3.checkedButton().text() + ' damage.'+content[pos:]
							else:
								content=content[:pos]+' And there are also a total of '+str(num)+' '+add2.group1.checkedButton().text()+'s in the picture, including '+str(add2.spin1.value())+' undamaged '+add2.group1.checkedButton().text()+' and '+str(add2.spin2.value())+' damaged '+add2.group1.checkedButton().text()+'. Under earthquake, the state of the component was '+add2.group3.checkedButton().text()+' damage.'+content[pos:]
					else:
						if content.find('More')==-1:
							if add2.radio_button05.isChecked():
								if num > 1:
									content = '{"image_id": "' + name + '",' + '"caption": "In this picture, there is a ' + add2.group0.checkedButton().text() + ' building. Under earthquake, the building has experienced ' + add2.group00.checkedButton().text() + '. More specifically, there are a total of ' + str(num) + ' infilled ' + add2.group1.checkedButton().text() + 's in the picture, including ' +str(add2.spin1.value())+ ' undamaged ' + add2.group1.checkedButton().text() + ' and ' +str(add2.spin2.value())+ ' damaged ' + add2.group1.checkedButton().text() + '. Under earthquake, the state of the damaged component was ' + add2.group3.checkedButton().text() + ' damage. More specifically, it experienced ."},'
								else:
									content = '{"image_id": "' + name + '",' + '"caption": "In this picture, there is a ' + add2.group0.checkedButton().text() + ' building. Under earthquake, the building has experienced ' + add2.group00.checkedButton().text() + '. More specifically, there is a total of ' + str(num) + ' infilled ' + add2.group1.checkedButton().text() + ' in the picture, including ' +str(add2.spin1.value())+ ' undamaged ' + add2.group1.checkedButton().text() + ' and ' +str(add2.spin2.value())+ ' damaged ' + add2.group1.checkedButton().text() + '. Under earthquake, the state of the damaged component was ' + add2.group3.checkedButton().text() + ' damage. More specifically, it experienced ."},'
							else:
								if num > 1:
									content = '{"image_id": "' + name + '",' + '"caption": "In this picture, there is a ' + add2.group0.checkedButton().text() + ' building. Under earthquake, the building has experienced ' + add2.group00.checkedButton().text() + '. More specifically, there are a total of ' + str(num) + ' ' + add2.group1.checkedButton().text() + 's in the picture, including ' +str(add2.spin1.value())+ ' undamaged ' + add2.group1.checkedButton().text() + ' and ' +str(add2.spin2.value())+ ' damaged ' + add2.group1.checkedButton().text() + '. Under earthquake, the state of the damaged component was ' + add2.group3.checkedButton().text() + ' damage. More specifically, it experienced ."},'
								else:
									content = '{"image_id": "' + name + '",' + '"caption": "In this picture, there is a ' + add2.group0.checkedButton().text() + ' building. Under earthquake, the building has experienced ' + add2.group00.checkedButton().text() + '. More specifically, there is a total of ' + str(num) + ' ' + add2.group1.checkedButton().text() + ' in the picture, including ' +str(add2.spin1.value())+ ' undamaged ' + add2.group1.checkedButton().text() + ' and ' +str(add2.spin2.value())+ ' damaged ' + add2.group1.checkedButton().text() + '. Under earthquake, the state of the damaged component was ' + add2.group3.checkedButton().text() + ' damage. More specifically, it experienced ."},'
						else:
							pos=content.find('"},')
							if add2.radio_button00.isChecked() and add2.radio_button05.isChecked():
								if num > 1:
									content =content[:pos]+' And there are a total of ' + str(num) + ' infilled ' + add2.group1.checkedButton().text() + 's in the picture, including ' +str(add2.spin1.value())+ ' undamaged ' + add2.group1.checkedButton().text() + ' and ' +str(add2.spin2.value())+ ' damaged ' + add2.group1.checkedButton().text() + '. Under earthquake, the state of the damaged component was ' + add2.group3.checkedButton().text() + ' damage. More specifically, it experienced .'+content[pos:]
								else:
									content =content[:pos]+' And there is a total of ' + str(num) + ' infilled ' + add2.group1.checkedButton().text() + ' in the picture, including ' +str(add2.spin1.value())+ ' undamaged ' + add2.group1.checkedButton().text() + ' and ' +str(add2.spin2.value())+ ' damaged ' + add2.group1.checkedButton().text() + '. Under earthquake, the state of the damaged component was ' + add2.group3.checkedButton().text() + ' damage. More specifically, it experienced .'+content[pos:]
							else:
								if num > 1:
									content =content[:pos]+' And there are a total of ' + str(num) + ' ' + add2.group1.checkedButton().text() + 's in the picture, including ' +str(add2.spin1.value())+ ' undamaged ' + add2.group1.checkedButton().text() + ' and ' +str(add2.spin2.value())+ ' damaged ' + add2.group1.checkedButton().text() + '. Under earthquake, the state of the damaged component was ' + add2.group3.checkedButton().text() + ' damage. More specifically, it experienced .'+content[pos:]
								else:
									content =content[:pos]+' And there is a total of ' + str(num) + ' ' + add2.group1.checkedButton().text() + ' in the picture, including ' +str(add2.spin1.value())+ ' undamaged ' + add2.group1.checkedButton().text() + ' and ' +str(add2.spin2.value())+ ' damaged ' + add2.group1.checkedButton().text() + '. Under earthquake, the state of the damaged component was ' + add2.group3.checkedButton().text() + ' damage. More specifically, it experienced .'+content[pos:]
						if add2.check2.isChecked():
							text=text+"　"+add2.check2.text()
							initpos=content.find('experienced .')
							pos=content.find('."},')
							if pos!=-1:
								if initpos!=-1:
									content=content[:pos]+"cracks"+content[pos:]
								else:
									content=content[:pos]+", cracks"+content[pos:]
						if add2.check3.isChecked():
							text=text+"　"+add2.check3.text()
							initpos=content.find('experienced .')
							pos=content.find('."},')
							if pos!=-1:
								if initpos!=-1:
									content=content[:pos]+"facades spalling"+content[pos:]
								else:
									content=content[:pos]+", facades spalling"+content[pos:]
						if add2.check4.isChecked():
							text=text+"　"+add2.check4.text()
							initpos=content.find('experienced .')
							pos=content.find('."},')
							if pos!=-1:
								if initpos!=-1:
									content=content[:pos]+"concrete spalling"+content[pos:]
								else:
									content=content[:pos]+", concrete spalling"+content[pos:]
						if add2.check40.isChecked():
							text=text+"　"+add2.check40.text()
							initpos=content.find('experienced .')
							pos=content.find('."},')
							if pos!=-1:
								if initpos!=-1:
									content=content[:pos]+"bricks falling"+content[pos:]
								else:
									content=content[:pos]+" and bricks falling"+content[pos:]
						if add2.check5.isChecked():
							text=text+"　"+add2.check5.text()
							initpos=content.find('experienced .')
							pos=content.find('."},')
							if pos!=-1:
								if initpos!=-1:
									content=content[:pos]+"buckling of reinforcement bars"+content[pos:]
								else:
									content=content[:pos]+" and buckling of reinforcement bars"+content[pos:]
						if not add2.check40.isChecked() and not add2.check2.isChecked() and not add2.check3.isChecked() and not add2.check4.isChecked() and not add2.check5.isChecked():
							text=text+add2.radio_button10.text()
							initpos=content.find('experienced .')
							pos=content.find('."},')
							content = content[:pos] + "undamaged" + content[pos:]
		text=text+"　"+add2.group3.checkedButton().text()
		item=QListWidgetItem(text)
		add2.list_widget.insertItem(0,item)
		add2.list_widget.setCurrentRow(0)
		content = content.replace('钢混', 'reinforced concrete')
		content = content.replace('砖混', 'masonry')
		content = content.replace('梁', 'beam')
		content = content.replace('柱', 'column')
		content = content.replace('墙', 'wall')
		content = content.replace('楼板', 'slab')
		content = content.replace('支撑', 'brace')
		content = content.replace('无明显 damage', 'undamaged')
		content = content.replace('轻微', 'minor')
		content = content.replace('中等', 'moderate')
		content = content.replace('严重', 'heavy')
		content = content.replace('完全', 'complete')
		content = content.replace('无', 'non-collapse')
		content = content.replace('部分', 'partial collapse')
		content = content.replace('全部', 'global collapse')
		with open(f'{name}.json',"w") as f:
			f.writelines(content)
	exist(add2)
def rgroup1():
	add1.radio_button09.setDisabled(False)
	add1.radio_button10.setDisabled(False)
	if add1.radio_button02.isChecked():
		add1.check0.setDisabled(False)
		add1.check1.setDisabled(False)
	else:
		add1.check0.setDisabled(True)
		add1.check1.setDisabled(True)
		add1.check0.setChecked(False)
		add1.check1.setChecked(False)
def rgroup2():
	add1.check2.setDisabled(True)
	add1.check3.setDisabled(True)
	add1.check4.setDisabled(True)
	add1.check5.setDisabled(True)
	add1.check6.setDisabled(True)
	add1.check7.setDisabled(True)
	add1.check40.setDisabled(True)
	if not add1.radio_button09.isChecked() and not add1.radio_button10.isChecked():
		add1.check2.setChecked(False)
		add1.check3.setChecked(False)
		add1.check4.setChecked(False)
		add1.check40.setChecked(False)
		add1.check5.setChecked(False)
		add1.check6.setChecked(False)
		add1.check7.setChecked(False)
	elif add1.radio_button07.isChecked() and add1.radio_button09.isChecked():
		add1.check2.setChecked(False)
		add1.check3.setChecked(False)
		add1.check4.setChecked(False)
		add1.check40.setChecked(False)
		add1.check5.setChecked(False)
		add1.check6.setDisabled(False)
		add1.check7.setDisabled(False)
	elif add1.radio_button08.isChecked():
		add1.check2.setDisabled(False)
		add1.check3.setDisabled(False)
		add1.check4.setChecked(False)
		add1.check40.setChecked(False)
		add1.check5.setChecked(False)
		add1.check6.setChecked(False)
		add1.check7.setDisabled(False)
	elif add1.radio_button02.isChecked() or add1.radio_button10.isChecked():
		add1.check2.setChecked(False)
		add1.check3.setChecked(False)
		add1.check4.setChecked(False)
		add1.check40.setChecked(False)
		add1.check5.setChecked(False)
	else:
		add1.check2.setDisabled(False)
		add1.check3.setDisabled(False)
		add1.check40.setDisabled(False)
		add1.check6.setChecked(False)
		add1.check7.setDisabled(False)
		if add1.radio_button09.isChecked():
			add1.check4.setDisabled(False)
			add1.check5.setDisabled(False)
			add1.check5.setChecked(False)
def cgroup():
	if add1.check4.isChecked() or add1.check5.isChecked():
		add1.check2.setDisabled(True)
		add1.check2.setChecked(False)
		add1.check3.setDisabled(True)
		add1.check3.setChecked(False)
		if add1.check5.isChecked():
			add1.check4.setDisabled(True)
			add1.check4.setChecked(True)
		elif add1.radio_button09.isChecked():
			add1.check4.setDisabled(False)
	else:
		add1.check2.setDisabled(False)
		add1.check3.setDisabled(False)
def cgroup_mix():
	if add2.check4.isChecked() or add2.check5.isChecked():
		add2.check2.setDisabled(True)
		add2.check2.setChecked(False)
		add2.check3.setDisabled(True)
		add2.check3.setChecked(False)
		if add2.check5.isChecked():
			add2.check4.setDisabled(True)
			add2.check4.setChecked(True)
		elif add2.radio_button09.isChecked():
			add2.check4.setDisabled(False)
	else:
		add2.check2.setDisabled(False)
		add2.check3.setDisabled(False)

def rgroup3():
	if add1.radio_button09.isChecked():
		add1.group3.setExclusive(False)
		add1.radio_button11.setChecked(False)
		add1.radio_button12.setChecked(True)
		add1.group3.setExclusive(True)
		add1.radio_button12.setDisabled(False)
		add1.radio_button13.setDisabled(False)
		add1.radio_button14.setDisabled(False)
		add1.radio_button15.setDisabled(False)
	else:
		add1.radio_button11.setChecked(True)
		add1.radio_button12.setDisabled(True)
		add1.radio_button13.setDisabled(True)
		add1.radio_button14.setDisabled(True)
		add1.radio_button15.setDisabled(True)
def rgroup00():
	add2.group1.setExclusive(False)
	add2.radio_button03.setChecked(False)
	add2.radio_button04.setChecked(False)
	add2.radio_button05.setChecked(False)
	add2.radio_button06.setChecked(False)
	add2.radio_button090.setChecked(False)
	add2.group1.setExclusive(True)
	add2.radio_button03.setDisabled(False)
	add2.radio_button04.setDisabled(False)
	add2.radio_button05.setDisabled(False)
	add2.radio_button06.setDisabled(False)
	add2.radio_button090.setDisabled(False)
	add2.group2.setExclusive(False)
	add2.radio_button09.setChecked(False)
	add2.radio_button10.setChecked(False)
	add2.group2.setExclusive(True)
	add2.radio_button09.setDisabled(True)
	add2.radio_button10.setDisabled(True)
def rgroup01():
	add2.radio_button09.setDisabled(False)
	add2.radio_button10.setDisabled(False)
def rgroup02():
	add2.check2.setDisabled(True)
	add2.check3.setDisabled(True)
	add2.check4.setDisabled(True)
	add2.check5.setDisabled(True)
	add2.check40.setDisabled(True)
	if not add2.radio_button09.isChecked() and not add2.radio_button10.isChecked():
		add2.check2.setChecked(False)
		add2.check3.setChecked(False)
		add2.check4.setChecked(False)
		add2.check40.setChecked(False)
		add2.check5.setChecked(False)
	elif add2.radio_button10.isChecked():
		add2.check2.setChecked(False)
		add2.check3.setChecked(False)
		add2.check4.setChecked(False)
		add2.check40.setChecked(False)
		add2.check5.setChecked(False)
	else:
		add2.check2.setDisabled(False)
		add2.check3.setDisabled(False)
		add2.check40.setDisabled(False)
		if add2.radio_button09.isChecked():
			add2.check4.setDisabled(False)
			add2.check5.setDisabled(False)
			add2.check5.setChecked(False)
def rgroup03():
	if not add2.group2.checkedButton():
		add2.radio_button11.setDisabled(False)
		add2.radio_button12.setDisabled(False)
		add2.radio_button13.setDisabled(False)
		add2.radio_button14.setDisabled(False)
		add2.radio_button15.setDisabled(False)
	elif add2.radio_button09.isChecked():
		add2.group3.setExclusive(False)
		add2.radio_button11.setChecked(False)
		add2.group3.setExclusive(True)
		add2.radio_button11.setDisabled(True)
		add2.radio_button12.setDisabled(False)
		add2.radio_button13.setDisabled(False)
		add2.radio_button14.setDisabled(False)
		add2.radio_button15.setDisabled(False)
	else:
		add2.radio_button11.setChecked(True)
		add2.radio_button12.setDisabled(True)
		add2.radio_button13.setDisabled(True)
		add2.radio_button14.setDisabled(True)
		add2.radio_button15.setDisabled(True)
def remove1():
	os.remove(f'{name}.json')
	add1.list_widget.insertItem(0,''+name+'.json文件已从目录中被移除')
	add1.list_widget.setCurrentRow(0)
	exist(add1)
def remove2():
	os.remove(f'{name}.json')
	add2.list_widget.insertItem(0,''+name+'.json文件已从目录中被移除')
	add2.list_widget.setCurrentRow(0)
	exist(add2)
def select():
	global selected
	file_dialog=QFileDialog()
	selected=file_dialog.getExistingDirectory(None)
	try:
		add1.label0.deleteLater()
		add1.label0=QLabel(selected)
		add1.layout.removeWidget(add1.label0)
		add1.layout.addWidget(add1.label0,0,1,1,2)
		add1.combo.clear()
		for file_name in QDir(selected).entryList(['*.jpg'],QDir.Files|QDir.NoSymLinks):
			add1.combo.addItem(file_name)
	except (NameError,RuntimeError):
		add2.label0.deleteLater()
		add2.label0=QLabel(selected)
		add2.layout.removeWidget(add2.label0)
		add2.layout.addWidget(add2.label0,0,1,1,2)
		add2.combo.clear()
		for file_name in QDir(selected).entryList(['*.jpg'],QDir.Files|QDir.NoSymLinks):
			add2.combo.addItem(file_name)
	display()
def display():
	global name
	try:
		name=add1.combo.currentText()
	except (NameError,RuntimeError):
		name=add2.combo.currentText()
	try:
		name=name[:name.index('.jpg')]
	except ValueError:
		pass
	path=selected+"/"+name+'.jpg'
	try:
		pix=QPixmap(path).scaled(add1.label5.size(),aspectMode=Qt.KeepAspectRatio)
		add1.label5.setPixmap(pix)
		add1.label5.setAlignment(Qt.AlignLeft|Qt.AlignTop)
		add1.layout.addWidget(add1.label5,0,1,34,1)
	except (NameError,RuntimeError):
		pix=QPixmap(path).scaled(add2.label5.size(),aspectMode=Qt.KeepAspectRatio)
		add2.label5.setPixmap(pix)
		add2.label5.setAlignment(Qt.AlignLeft|Qt.AlignTop)
		add2.layout.addWidget(add2.label5,0,1,35,1)
	try:
		exist(add1)
	except (NameError,RuntimeError):
		exist(add2)
def exist(self):
	if os.path.exists(f'{name}.json'):
		self.button1.setEnabled(True)
	else:
		self.button1.setEnabled(False)
def close():
	try:
		add1.deleteLater()
	except (NameError,RuntimeError):
		add2.deleteLater()
	widget.show()
def pop():
	QMessageBox.information(widget,'StarryProject-L 1.4.3 "Sylphy Horn"',"建筑损伤图像贴标程序\n版本　1.4.3　2025/1/7\nby　4N☆E　<Starry4N@stu.scu.edu.cn>\n2024-2025　StarryProject™\n内部软件　请勿外传\n\nV1.4新增特性：\n⒈输入框更改为下拉列表，进入模块将立即加载目录中的首个JPG文件并显示；\n⒉「混合式」模块已经替代「整体」模块，在不选择构件时的输出与曾经的「整体」模块完全一致；\n⒊当前目录的显示将即时更新。\n\nV1.4.1：⒈修复「局部」模块布局显示不正常，根本无法进行贴标的恶性BUG；⒉优化图像显示布局。\nV1.4.2：⒈修复切换模块或目录异常的恶性BUG；⒉修正了一些复选框逻辑错误；⒊仅当图像对应JSON文件存在时「清除本文件」按钮才可用。\nV1.4.3：⒈「砼剥落」与「钢筋屈服」复选框将仅在「有损伤」按钮被选中的情况下可用；⒉修正「整体」下无明显损伤时生成错误文本的问题；⒊修复「整体」下清除文件无提示的问题；⒋有损伤时的破坏程度默认为轻微；⒌「楼板」在写入ＪＳＯＮ时将被正确替换；⒍display函数name将从「.jpg」截断，修复了json文件名产生时的错误。\n\n\n——不是因为房间太暗了吗？\n——是不是身体里铁不足啊")
app=QApplication.instance()
if app is None:
	app=QApplication(sys.argv)
widget=QWidget()
widget.setWindowTitle('StarryProject-L 1.4.3')
widget.resize(320,240)
widget.setFixedSize(widget.width(),widget.height())
layout=QGridLayout(widget)
button0=QToolButton()
button0.setToolButtonStyle(Qt.ToolButtonTextOnly)
button0.setToolTip("关于")
button1=QPushButton('整体')
button2=QPushButton('局部')
layout.addWidget(button0,0,1)
layout.addWidget(button1,0,0)
layout.addWidget(button2,0,2)
button0.clicked.connect(pop)
button1.clicked.connect(mix)
button2.clicked.connect(partial)
widget.setLayout(layout)
selected=os.getcwd()
widget.show()
sys.exit(app.exec())