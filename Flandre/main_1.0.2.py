#This Python file uses the following encoding: utf-8
import os
from PySide6.QtWidgets import QApplication,QWidget,QHBoxLayout,QToolButton,QPushButton,QFileDialog,QGridLayout,QRadioButton,QButtonGroup,QListWidget,QLineEdit,QLabel,QCheckBox,QListWidgetItem,QMessageBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
def entire():
    widget.close()
    global add0
    add0=QWidget()
    add0.setWindowTitle('结构整体')
    add0.resize(640,480)
    add0.setFixedSize(add0.width(),add0.height())
    add0.layout=QGridLayout(add0)
    add0.label0000000=QLabel("")
    add0.label000000=QLabel("")
    add0.label00000=QLabel("")
    add0.label0000=QLabel("")
    add0.label000=QLabel("")
    add0.label00=QLabel("")
    add0.label0=QLabel(selected)
    add0.label1=QLabel("结构类型：")
    add0.label2=QLabel("破坏详情：")
    add0.label3=QLabel()
    add0.label4=QLabel("破坏程度：")
    add0.label5=QLabel("历史记录：")
    add0.button1=QPushButton('写入')
    add0.button2=QPushButton('返回')
    add0.button3=QPushButton("文件夹")
    add0.list_widget=QListWidget()
    add0.input_text=QLineEdit()
    add0.input_text.setPlaceholderText("当前操作的ＪＰＧ文件的主名")
    add0.input_text.textChanged.connect(display0)
    add0.radio_button0=QRadioButton('reinforced ')
    add0.radio_button1=QRadioButton('brick-')
    add0.group0=QButtonGroup()
    add0.group0.addButton(add0.radio_button0)
    add0.group0.addButton(add0.radio_button1)
    add0.radio_button2=QRadioButton('non-')
    add0.radio_button3=QRadioButton('partial ')
    add0.radio_button4=QRadioButton('complete ')
    add0.group1=QButtonGroup()
    add0.group1.addButton(add0.radio_button2)
    add0.group1.addButton(add0.radio_button3)
    add0.group1.addButton(add0.radio_button4)
    add0.radio_button5=QRadioButton('no visible')
    add0.radio_button6=QRadioButton('minor')
    add0.radio_button7=QRadioButton('moderate')
    add0.radio_button8=QRadioButton('heavy')
    add0.radio_button9=QRadioButton('complete')
    add0.group2=QButtonGroup()
    add0.group2.addButton(add0.radio_button5)
    add0.group2.addButton(add0.radio_button6)
    add0.group2.addButton(add0.radio_button7)
    add0.group2.addButton(add0.radio_button8)
    add0.group2.addButton(add0.radio_button9)
    add0.layout.addWidget(add0.label0,0,0)
    add0.layout.addWidget(add0.label1,1,1)
    add0.layout.addWidget(add0.label2,4,1)
    add0.layout.addWidget(add0.label4,8,1)
    add0.layout.addWidget(add0.label5,19,0)
    add0.layout.addWidget(add0.label00,14,1)
    add0.layout.addWidget(add0.label000,15,1)
    add0.layout.addWidget(add0.label0000,16,1)
    add0.layout.addWidget(add0.label00000,17,1)
    add0.layout.addWidget(add0.label000000,18,1)
    add0.layout.addWidget(add0.label0000000,19,1)
    add0.layout.addWidget(add0.radio_button0,2,1)
    add0.layout.addWidget(add0.radio_button1,3,1)
    add0.layout.addWidget(add0.radio_button2,5,1)
    add0.layout.addWidget(add0.radio_button3,6,1)
    add0.layout.addWidget(add0.radio_button4,7,1)
    add0.layout.addWidget(add0.radio_button5,9,1)
    add0.layout.addWidget(add0.radio_button6,10,1)
    add0.layout.addWidget(add0.radio_button7,11,1)
    add0.layout.addWidget(add0.radio_button8,12,1)
    add0.layout.addWidget(add0.radio_button9,13,1)
    add0.layout.addWidget(add0.button1,20,1)
    add0.layout.addWidget(add0.button2,21,1)
    add0.layout.addWidget(add0.button3,0,1)
    add0.layout.addWidget(add0.list_widget,20,0,2,1)
    add0.layout.addWidget(add0.input_text,21,0)
    add0.button1.clicked.connect(write)
    add0.button2.clicked.connect(close0)
    add0.button3.clicked.connect(select)
    add0.radio_button2.setDisabled(True)
    add0.radio_button3.setDisabled(True)
    add0.radio_button4.setDisabled(True)
    add0.group0.buttonToggled.connect(rgroup)
    add0.show()
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
    add1.button4=QPushButton("文件夹")
    add1.label00000=QLabel("")
    add1.label0000=QLabel("")
    add1.label000=QLabel("")
    add1.label00=QLabel("")
    add1.label0=QLabel(selected)
    add1.label1=QLabel("结构类型：")
    add1.label2=QLabel("出现的部件：")
    add1.label3=QLabel("破坏类型：")
    add1.label4=QLabel("破坏程度：")
    add1.label5=QLabel()
    add1.label6=QLabel('历史记录：')
    add1.radio_button00=QRadioButton('reinforced\nconcrete')
    add1.radio_button01=QRadioButton('masonry')
    add1.group0=QButtonGroup()
    add1.group0.addButton(add1.radio_button00)
    add1.group0.addButton(add1.radio_button01)
    add1.radio_button02=QRadioButton('non-structural')
    add1.radio_button03=QRadioButton('beam')
    add1.radio_button04=QRadioButton('column')
    add1.radio_button05=QRadioButton('wall')
    add1.radio_button06=QRadioButton('slab')
    add1.radio_button07=QRadioButton('roof')
    add1.radio_button08=QRadioButton('timber')
    add1.radio_button090=QRadioButton('stairway')
    add1.radio_button11=QRadioButton('no visible')
    add1.radio_button12=QRadioButton('minor')
    add1.radio_button13=QRadioButton('moderate')
    add1.radio_button14=QRadioButton('heavy')
    add1.radio_button15=QRadioButton('complete')
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
    add1.radio_button10=QRadioButton('无明显损伤')
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
    add1.check4=QCheckBox("混凝土剥落")
    add1.check40=QCheckBox("墙砖剥落")
    add1.check5=QCheckBox("钢筋裸露")
    add1.check6=QCheckBox("溜瓦")
    add1.check7=QCheckBox("部分坍塌")
    add1.list_widget=QListWidget()
    add1.input_text=QLineEdit()
    add1.input_text.setPlaceholderText("当前操作的ＪＰＧ文件的主名")
    add1.layout.addWidget(add1.label0,0,0,1,2)
    add1.layout.addWidget(add1.label1,1,1)
    add1.layout.addWidget(add1.label2,4,1)
    add1.layout.addWidget(add1.label3,15,1)
    add1.layout.addWidget(add1.label4,25,1)
    add1.layout.addWidget(add1.label6,35,0)
    add1.layout.addWidget(add1.label00,31,1)
    add1.layout.addWidget(add1.label000,32,1)
    add1.layout.addWidget(add1.label0000,33,1)
    add1.layout.addWidget(add1.label00000,34,1)
    add1.layout.addWidget(add1.radio_button00,2,1)
    add1.layout.addWidget(add1.radio_button01,3,1)
    add1.layout.addWidget(add1.radio_button02,12,1)
    add1.layout.addWidget(add1.radio_button03,5,1)
    add1.layout.addWidget(add1.radio_button04,6,1)
    add1.layout.addWidget(add1.radio_button05,7,1)
    add1.layout.addWidget(add1.radio_button06,8,1)
    add1.layout.addWidget(add1.radio_button07,9,1)
    add1.layout.addWidget(add1.radio_button08,10,1)
    add1.layout.addWidget(add1.radio_button090,11,1)
    add1.layout.addWidget(add1.radio_button09,17,1)
    add1.layout.addWidget(add1.radio_button10,16,1)
    add1.layout.addWidget(add1.radio_button11,26,1)
    add1.layout.addWidget(add1.radio_button12,27,1)
    add1.layout.addWidget(add1.radio_button13,28,1)
    add1.layout.addWidget(add1.radio_button14,29,1)
    add1.layout.addWidget(add1.radio_button15,30,1)
    add1.layout.addWidget(add1.button0,35,1)
    add1.layout.addWidget(add1.button1,36,1)
    add1.layout.addWidget(add1.button3,37,1)
    add1.layout.addWidget(add1.button4,0,1)
    add1.layout.addWidget(add1.check0,13,1)
    add1.layout.addWidget(add1.check1,14,1)
    add1.layout.addWidget(add1.check2,18,1)
    add1.layout.addWidget(add1.check3,19,1)
    add1.layout.addWidget(add1.check4,20,1)
    add1.layout.addWidget(add1.check40,21,1)
    add1.layout.addWidget(add1.check5,22,1)
    add1.layout.addWidget(add1.check6,23,1)
    add1.layout.addWidget(add1.check7,24,1)
    add1.layout.addWidget(add1.list_widget,36,0,2,1)
    add1.layout.addWidget(add1.input_text,37,0)
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
    add1.group0.buttonToggled.connect(rgroup0)
    add1.group0.buttonToggled.connect(rgroup1)
    add1.group1.buttonToggled.connect(rgroup1)
    add1.group1.buttonToggled.connect(rgroup2)
    add1.group2.buttonToggled.connect(rgroup2)
    add1.group2.buttonToggled.connect(rgroup3)
    add1.input_text.textChanged.connect(display1)
    add1.button0.clicked.connect(add)
    add1.button1.clicked.connect(remove)
    add1.button3.clicked.connect(close1)
    add1.button4.clicked.connect(select)
    add1.show()
def display0():
    global name
    name=add0.input_text.text()
    path=selected+"/"+name+".JPG"
    pix=QPixmap(path).scaled(add0.label3.size(),aspectMode=Qt.KeepAspectRatio)
    add0.label3.setPixmap(pix)
    add0.label3.setAlignment(Qt.AlignLeft|Qt.AlignTop)
    add0.layout.addWidget(add0.label3,0,0,20,1)
def display1():
    global name
    name=add1.input_text.text()
    path=selected+"/"+name+".JPG"
    pix=QPixmap(path).scaled(add1.label5.size(),aspectMode=Qt.KeepAspectRatio)
    add1.label5.setPixmap(pix)
    add1.label5.setAlignment(Qt.AlignLeft|Qt.AlignTop)
    add1.layout.addWidget(add1.label5,0,0,36,1)
def close0():
    add0.close()
    widget.show()
def close1():
    add1.close()
    widget.show()
def write():
    if add0.group0.checkedButton().text():
        text=name+add0.group0.checkedButton().text()+add0.group1.checkedButton().text()+add0.group2.checkedButton().text()
        with open(f'{name}.json',"w") as f:
            f.writelines('{"image_id": "'+name+'",'+'"caption": "In this picture, there is a '+add0.group0.checkedButton().text()+' building. Under earthquake, the building has experienced '+add0.group1.checkedButton().text()+'collapse, the state of the '+add0.group0.checkedButton().text()+' building was '+add0.group2.checkedButton().text()+' damage."},')
        item=QListWidgetItem(text)
        add0.list_widget.addItem(item)
        add0.list_widget.scrollToBottom()
def add():
    if add1.group0.checkedButton().text():
        text=name+add1.group0.checkedButton().text()
        if add1.group1.checkedButton().text():
            text=text+add1.group1.checkedButton().text()
            try:
                with open(f'{name}.json',"r") as f:
                    content=f.read()
            except IOError:
                    content=''
            if add1.check0.isChecked():
                text=text+add1.check0.text()
                initpos=content.find('picture')
                if initpos==-1:
                    if add1.radio_button09.isChecked()== True:
                        content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a '+add1.group1.checkedButton().text()+' component in a '+add1.group0.checkedButton().text()+' building. The component is a piece of celling. Under earthquake, the state of the celling was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced partial falling."},'
                    else:
                        content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a '+add1.group1.checkedButton().text()+' component in a '+add1.group0.checkedButton().text()+' building. The component is a piece of celling. Under earthquake, the state of the celling was not visibly damaged."},'
                else:
                    pos=content.find('"},')
                    if add1.radio_button09.isChecked()== True:
                        content=content[:pos]+' And there is also a '+add1.group1.checkedButton().text()+' component in the '+add1.group0.checkedButton().text()+' building. The component is a piece of celling. Under earthquake, the state of the celling was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced partial falling.'+content[pos:]
                    else:
                        content=content[:pos]+' And there is also a '+add1.group1.checkedButton().text()+' component in the '+add1.group0.checkedButton().text()+' building. The component is a piece of celling. Under earthquake, the state of the celling was not visibly damaged.'+content[pos:]
            if add1.check1.isChecked():
                text=text+add1.check1.text()
                initpos=content.find('picture')
                if initpos==-1:
                    if add1.radio_button09.isChecked()== True:
                        content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a '+add1.group1.checkedButton().text()+' component in a '+add1.group0.checkedButton().text()+' building. The component is a piece of pipe. Under earthquake, the state of the pipe was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced the fracture of the pipe."},'
                    else:
                        content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a '+add1.group1.checkedButton().text()+' component in a '+add1.group0.checkedButton().text()+' building. The component is a piece of pipe. Under earthquake, the state of the pipe was not visibly damaged."},'
                else:
                    pos=content.find('"},')
                    if add1.radio_button09.isChecked()== True:
                        content=content[:pos]+' And there is also a '+add1.group1.checkedButton().text()+' component in the '+add1.group0.checkedButton().text()+' building. The component is a piece of pipe. Under earthquake, the state of the pipe was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced the fracture of the pipe.'+content[pos:]
                    else:
                        content=content[:pos]+' And there is also a '+add1.group1.checkedButton().text()+' component in the '+add1.group0.checkedButton().text()+' building. The component is a piece of pipe. Under earthquake, the state of the pipe was not visibly damaged.'+content[pos:]
            if add1.group2.checkedButton().text():
                text=text+add1.group2.checkedButton().text()
                if add1.check0.isChecked()== False and add1.check1.isChecked()== False and add1.check2.isChecked()== False and add1.check3.isChecked()== False and add1.check4.isChecked()== False and add1.check40.isChecked()== False and add1.check5.isChecked()== False and add1.check6.isChecked()== False and add1.check7.isChecked()== False:
                    initpos=content.find('picture')
                    if initpos==-1:
                        content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a component in a '+add1.group0.checkedButton().text()+' building. The component is '+add1.group1.checkedButton().text()+' component. Under earthquake, the state of the '+add1.group1.checkedButton().text()+' component was '+add1.group3.checkedButton().text()+' damage."},'
                    else:
                        pos=content.find('"},')
                        content=content[:pos]+' And there is also a component in the '+add1.group0.checkedButton().text()+' building. The component is '+add1.group1.checkedButton().text()+' component. Under earthquake, the state of the '+add1.group1.checkedButton().text()+' component was '+add1.group3.checkedButton().text()+' damage.'+content[pos:]
                elif add1.check0.isChecked()== False and add1.check1.isChecked()== False:
                    initpos=content.find('picture')
                    if initpos==-1:
                        content='{"image_id": "'+name+'",'+'"caption": "In this picture, there is a structural component in a '+add1.group0.checkedButton().text()+' building. The component is '+add1.group1.checkedButton().text()+'. Under earthquake, the state of the '+add1.group1.checkedButton().text()+' was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced ."},'
                    else:
                        pos=content.find('"},')
                        content=content[:pos]+' And there is also a structural component in the '+add1.group0.checkedButton().text()+' building. The component is '+add1.group1.checkedButton().text()+'. Under earthquake, the state of the '+add1.group1.checkedButton().text()+' was '+add1.group3.checkedButton().text()+' damage. More specifically, it experienced .'+content[pos:]
                    if add1.check2.isChecked():
                        text=text+add1.check2.text()
                        initpos=content.find('experienced .')
                        pos=content.find('."},')
                        if pos!=-1:
                            if initpos!=-1:
                                content=content[:pos]+"cracks"+content[pos:]
                            else:
                                content=content[:pos]+" and cracks"+content[pos:]
                    if add1.check3.isChecked():
                        text=text+add1.check3.text()
                        initpos=content.find('experienced .')
                        pos=content.find('."},')
                        if pos!=-1:
                            if initpos!=-1:
                                content=content[:pos]+"facades spalling"+content[pos:]
                            else:
                                content=content[:pos]+" and facades spalling"+content[pos:]
                    if add1.check4.isChecked():
                        text=text+add1.check4.text()
                        initpos=content.find('experienced .')
                        pos=content.find('."},')
                        if pos!=-1:
                            if initpos!=-1:
                                content=content[:pos]+"concrete spalling"+content[pos:]
                            else:
                                content=content[:pos]+" and concrete spalling"+content[pos:]
                    if add1.check40.isChecked():
                        text=text+add1.check40.text()
                        initpos=content.find('experienced .')
                        pos=content.find('."},')
                        if pos!=-1:
                            if initpos!=-1:
                                content=content[:pos]+"bricks falling"+content[pos:]
                            else:
                                content=content[:pos]+" and bricks falling"+content[pos:]
                    if add1.check5.isChecked():
                        text=text+add1.check5.text()
                        initpos=content.find('experienced .')
                        pos=content.find('."},')
                        if pos!=-1:
                            if initpos!=-1:
                                content=content[:pos]+"buckling of reinforcement bars"+content[pos:]
                            else:
                                content=content[:pos]+" and buckling of reinforcement bars"+content[pos:]
                    if add1.check6.isChecked():
                        text=text+add1.check6.text()
                        initpos=content.find('experienced .')
                        pos=content.find('."},')
                        if pos!=-1:
                            if initpos!=-1:
                                content=content[:pos]+"slipping tiles"+content[pos:]
                            else:
                                content=content[:pos]+" and slipping tiles"+content[pos:]
                    if add1.check7.isChecked():
                        text=text+add1.check7.text()
                        initpos=content.find('experienced .')
                        pos=content.find('."},')
                        if pos!=-1:
                            if initpos!=-1:
                                content=content[:pos]+"partial falling"+content[pos:]
                            else:
                                content=content[:pos]+" and partial falling"+content[pos:]
            text=text+add1.group3.checkedButton().text()
            item=QListWidgetItem(text)
            add1.list_widget.addItem(item)
            add1.list_widget.scrollToBottom()
            with open(f'{name}.json',"w") as f:
                f.writelines(content)
def remove():
    if name:
        os.remove(f'{name}.json')
        add1.list_widget.addItem('截止的'+name+'.json文件已从目录中被移除')
        add1.list_widget.scrollToBottom()
def rgroup():
    add0.radio_button2.setDisabled(False)
    add0.radio_button3.setDisabled(False)
    add0.radio_button4.setDisabled(False)
def rgroup0():
    add1.radio_button02.setDisabled(False)
    add1.radio_button03.setDisabled(False)
    add1.radio_button04.setDisabled(False)
    add1.radio_button05.setDisabled(False)
    add1.radio_button06.setDisabled(False)
    add1.radio_button090.setDisabled(False)
    if add1.radio_button01.isChecked()==True:
        add1.radio_button07.setDisabled(False)
        add1.radio_button08.setDisabled(False)
        # if add1.radio_button09.isChecked()==True:
        #     add1.check40.setDisabled(False)
    else:
        add1.radio_button07.setDisabled(True)
        add1.radio_button08.setDisabled(True)
        add1.check6.setChecked(False)
        add1.check7.setChecked(False)
        # add1.check40.setDisabled(True)
        # add1.check40.setChecked(False)
def rgroup1():
    add1.radio_button09.setDisabled(False)
    add1.radio_button10.setDisabled(False)
    if add1.radio_button02.isChecked()==True:
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
    if add1.radio_button09.isChecked()==False and add1.radio_button10.isChecked()==False:
        add1.check2.setChecked(False)
        add1.check3.setChecked(False)
        add1.check4.setChecked(False)
        add1.check40.setChecked(False)
        add1.check5.setChecked(False)
        add1.check6.setChecked(False)
        add1.check7.setChecked(False)
    elif add1.radio_button07.isChecked()==True and add1.radio_button09.isChecked()==True:
        add1.check2.setChecked(False)
        add1.check3.setChecked(False)
        add1.check4.setChecked(False)
        add1.check40.setChecked(False)
        add1.check5.setChecked(False)
        add1.check6.setDisabled(False)
        add1.check7.setDisabled(False)
    elif add1.radio_button02.isChecked()==True or add1.radio_button10.isChecked()==True:
        add1.check2.setChecked(False)
        add1.check3.setChecked(False)
        add1.check4.setChecked(False)
        add1.check40.setChecked(False)
        add1.check5.setChecked(False)
    else:
        add1.check40.setDisabled(False)
        add1.check2.setDisabled(False)
        add1.check3.setDisabled(False)
        add1.check4.setDisabled(False)
        add1.check5.setDisabled(False)
        add1.check6.setChecked(False)
        add1.check7.setChecked(False)
        # if add1.radio_button00.isChecked()==True:
        #     add1.check40.setDisabled(True)
def rgroup3():
    if add1.radio_button09.isChecked()==True:
        add1.group3.setExclusive(False)
        add1.radio_button11.setChecked(False)
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
def select():
    global selected
    file_dialog=QFileDialog()
    selected=file_dialog.getExistingDirectory(None,"选取文件夹")
def pop():
    msgbox=QMessageBox.information(widget,'StarryProject-L 1.0.2 "Laevatein"',"地震震后建筑照片贴标程序\n版本　１.０.２　２０２４／７／１８\nｂｙ　４Ｎ☆Ｅ　＜Ｓｔａｒｒｙ４Ｎ＠ｓｔｕ．ｓｃｕ．ｅｄｕ．ｃｎ＞\n２０２４　ＳｔａｒｒｙＰｒｏｊｅｃｔ™\n内部软件　请勿外传\n\nＶ１.０新增特性：\n１.【局部结构】历史记录列表提示条目清除时也将自动滚动到最底端；\n２.【局部结构】为防止误操作，使“墙砖剥落”复选框在ＲＣ选中的情况下不可用；\n３.【局部结构】另外修复在选择“吊顶”等非结构构件无损伤时生成自相矛盾的caption的问题；\n４.ＵＩ与生成文字微调。\nＶ１.０.１：修复了管道在历史记录中显示为吊顶的错误。\nＶ１.０.２：\n修复管道在有损伤时可能生成错误语句的问题；\n修复整体结构生成的ＪＳＯＮ格式错误；\n修复ＲＣ结构下墙砖剥落多选框不可用的问题。\n\n\n——你在叫谁吗？\n——我谁也没叫")
    if msgbox==QMessageBox.Ok:
        QMessageBox.about(widget,'已知问题',"Ｏｒｚ\n１.浏览文件夹按钮选择新文件夹后需要返回主菜单再进入才能更新显示的路径；\n２.无法使单选按钮的显示文本为中文的同时输出内容为英文，以现有代码的逻辑无法做到。")
app=QApplication([])
widget=QWidget()
widget.setWindowTitle('StarryProject-L 1.0.2')
widget.resize(320,240)
widget.setFixedSize(widget.width(),widget.height())
layout=QHBoxLayout(widget)
button0=QToolButton()
button0.setToolButtonStyle(Qt.ToolButtonTextOnly)
button0.setToolTip("关于")
button1=QPushButton('结构整体')
button2=QPushButton('结构局部')
layout.addWidget(button1)
layout.addWidget(button0)
layout.addWidget(button2)
button0.clicked.connect(pop)
button1.clicked.connect(entire)
button2.clicked.connect(partial)
widget.setLayout(layout)
select()
if selected:
    widget.show()
    app.exec()