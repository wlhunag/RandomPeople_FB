#-*- coding: utf-8-*-

__author__ = 'Aaron'
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import random
import os
import sys

ClassA = {"9830013": u"孫以華", "9830014": u"林秉叡", "9843524": u"傅毓婷", "9930003": u"陳昶安", "9930004": u"林暉育",
          "9930005": u"陳奉儀", "9930006": u"黃建程", "9930007": u"陳一萱", "9930008": u"蕭伃君", "9930009": u"李振廷",
          "9930010": u"陳黎鳴", "9930011": u"陳怡蓉", "9930012": u"陳泓諾", "9930013": u"林邑宣", "9930015": u"呂政育",
          "9930016": u"梁宜謙", "9930017": u"陳宥丞", "9930019": u"張啟漢", "9930021": u"楊凱麟", "9930022": u"李昕錞",
          "9930023": u"陳育德", "9930024": u"余文傑", "9930025": u"張仕學", "9930026": u"連欣慈", "9930027": u"許育菁",
          "9930028": u"陳亭伊", "9930029": u"黃文龍", "9930030": u"戴文川", "9930031": u"黃子瑋", "9930032": u"葉人輔",
          "9930033": u"胡家瑄", "9930034": u"沈軒佑", "9930035": u"曾柏蒼", "9930036": u"吳銘浩", "9930037": u"廖育萱",
          "9930038": u"鄭翌玄", "9930039": u"陳柏任", "9930040": u"莊謹慈", "9930041": u"程偉智", "9940529": u"陳怡瑾",
          "9943050": u"詹甯喬", "9970049": u"蕭立芸", "9917067": u"蕭凱瑋"}
numA = ['9930039', '9930038', '9930033', '9930032', '9930031', '9930030', '9930037', '9930036', '9930035', '9930034',
        '9940529', '9830013', '9917067', '9830014', '9930003', '9930006', '9930007', '9930004', '9930005', '9930008',
        '9930009', '9930028', '9930029', '9930021', '9930022', '9930023', '9930024', '9930025', '9930026', '9930027',
        '9843524', '9970049', '9930040', '9930041', '9943050', '9930015', '9930017', '9930016', '9930011', '9930010',
        '9930013', '9930012', '9930019']

ClassB = {"9930045": u"何宗霖", "9930046": u"吳俊昇", "9930047": u"林庭偉", "9930048": u"周靖倫", "9930049": u"楊昱晨",
          "9930051": u"蔡宗霖", "9930052": u"陳盈蓉", "9930053": u"陳柔樺", "9930054": u"王聖驊", "9930055": u"劉柏辰",
          "9930056": u"梁永淮", "9930057": u"姜凱文", "9930059": u"蔡宛蓉", "9930060": u"邱薪庭", "9930061": u"陳彥潔",
          "9930062": u"鄒心儀", "9930063": u"吳建德", "9930065": u"呂曼慈", "9930068": u"潘明哲", "9930069": u"李智凱",
          "9930070": u"劉唯正", "9930072": u"廖彥誠", "9930074": u"李馥安", "9930076": u"黃雯君", "9930077": u"江鈞翰",
          "9930078": u"林昌延", "9930079": u"劉晉嘉", "9930080": u"莊淳霽", "9930081": u"張鍇生", "9930082": u"詹鈞皓",
          "9930083": u"陳翊文", "9930084": u"陳毅珊", "9930085": u"蘇俊豪", "9930087": u"羅潔霞", "9930088": u"李慧明",
          "9940023": u"張禾昀", "9952032": u"楊君皓", "9970531": u"黃書儀", "9977005": u"謝欣諭"}

numB = ['9930051', '9930065', '9930053', '9930052', '9930055', '9930054', '9930048', '9930049', '9930046', '9930047',
        '9930063', '9930045', '9930068', '9930079', '9930078', '9940023', '9930074', '9977005', '9930060', '9930069',
        '9930076', '9930061', '9952032', '9930088', '9930081', '9930057', '9930077', '9930082', '9930083', '9930080',
        '9930056', '9930062', '9930087', '9930084', '9930085', '9930059', '9970531', '9930070', '9930072']

ClassC = {"9830013": u"孫以華", "9830014": u"林秉叡", "9843524": u"傅毓婷", "9930003": u"陳昶安", "9930004": u"林暉育",
          "9930005": u"陳奉儀", "9930006": u"黃建程", "9930007": u"陳一萱", "9930008": u"蕭伃君", "9930009": u"李振廷",
          "9930010": u"陳黎鳴", "9930011": u"陳怡蓉", "9930012": u"陳泓諾", "9930013": u"林邑宣", "9930015": u"呂政育",
          "9930016": u"梁宜謙", "9930017": u"陳宥丞", "9930019": u"張啟漢", "9930021": u"楊凱麟", "9930022": u"李昕錞",
          "9930023": u"陳育德", "9930024": u"余文傑", "9930025": u"張仕學", "9930026": u"連欣慈", "9930027": u"許育菁",
          "9930028": u"陳亭伊", "9930029": u"黃文龍", "9930030": u"戴文川", "9930031": u"黃子瑋", "9930032": u"葉人輔",
          "9930033": u"胡家瑄", "9930034": u"沈軒佑", "9930035": u"曾柏蒼", "9930036": u"吳銘浩", "9930037": u"廖育萱",
          "9930038": u"鄭翌玄", "9930039": u"陳柏任", "9930040": u"莊謹慈", "9930041": u"程偉智", "9940529": u"陳怡瑾",
          "9943050": u"詹甯喬", "9970049": u"蕭立芸", "9917067": u"蕭凱瑋", "9930045": u"何宗霖", "9930046": u"吳俊昇",
          "9930047": u"林庭偉", "9930048": u"周靖倫", "9930049": u"楊昱晨", "9930051": u"蔡宗霖", "9930052": u"陳盈蓉",
          "9930053": u"陳柔樺", "9930054": u"王聖驊", "9930055": u"劉柏辰", "9930056": u"梁永淮", "9930057": u"姜凱文",
          "9930059": u"蔡宛蓉", "9930060": u"邱薪庭", "9930061": u"陳彥潔", "9930062": u"鄒心儀", "9930063": u"吳建德",
          "9930065": u"呂曼慈", "9930068": u"潘明哲", "9930069": u"李智凱", "9930070": u"劉唯正", "9930072": u"廖彥誠",
          "9930074": u"李馥安", "9930076": u"黃雯君", "9930077": u"江鈞翰", "9930078": u"林昌延", "9930079": u"劉晉嘉",
          "9930080": u"莊淳霽", "9930081": u"張鍇生", "9930082": u"詹鈞皓", "9930083": u"陳翊文", "9930084": u"陳毅珊",
          "9930085": u"蘇俊豪", "9930087": u"羅潔霞", "9930088": u"李慧明", "9940023": u"張禾昀", "9952032": u"楊君皓",
          "9970531": u"黃書儀", "9977005": u"謝欣諭"}

allnumber = ['9930051', '9930076', '9930039', '9930038', '9930055', '9930054', '9930057', '9930053', '9843524',
             '9930032', '9930031', '9930030', '9930037', '9930036', '9930035', '9930034', '9970049', '9930084',
             '9930065', '9930083', '9940529', '9930033', '9930072', '9952032', '9930088', '9977005', '9930062',
             '9930078', '9830013', '9930047', '9930056', '9917067', '9930087', '9830014', '9930085', '9930003',
             '9930006', '9930007', '9930004', '9930005', '9930070', '9930008', '9930009', '9930074', '9930028',
             '9930029', '9930045', '9930060', '9930061', '9930048', '9930049', '9930046', '9930021', '9930022',
             '9930023', '9930024', '9930025', '9930026', '9930027', '9930063', '9930040', '9930041', '9970531',
             '9943050', '9930068', '9930079', '9930052', '9930077', '9930081', '9930015', '9930082', '9930017',
             '9930016', '9930011', '9930010', '9930013', '9930012', '9940023', '9930059', '9930019', '9930080',
             '9930069']

class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        self.createLayout()
        self.createConnection()
        self.shown = []


    def createLayout(self):
        self.labelleft = QLabel()
        iconpeo = QPixmap("icons/people.png")#, QIcon.Normal, QIcon.Off
        self.labelleft.setPixmap(iconpeo)
        self.label = QLabel()
        self.label.setText(u"選出幾人")
        self.spinbox = QSpinBox()
        self.spinbox.size()
        self.spinbox.setRange(1, 82)
        self.spinbox.setValue(1)
        self.spinbox.sizeHint()

        self.FBButton = QPushButton(u"更新全班大頭貼")
        iconfb = QIcon()
        iconfb.addPixmap(QPixmap("icons/profile.png"), QIcon.Normal, QIcon.Off)
        self.FBButton.setIcon(iconfb)
        self.FBButton.setToolTip(u"與 Facebook 同步大頭貼資料庫")

        self.labelA = QLabel(u"甲班")
        self.labelB = QLabel(u"乙班")
        self.checkA = QCheckBox()
        self.checkA.setChecked(True)
        self.checkB = QCheckBox()
        self.checkB.setChecked(True)

        h1 = QHBoxLayout()
        h1.addWidget(self.labelleft)
        h1.addWidget(self.label)
        h1.addWidget(self.spinbox)
        h1.addStretch(9)
        h1.addWidget(self.labelA)
        h1.addWidget(self.checkA)
        h1.addWidget(self.labelB)
        h1.addWidget(self.checkB)
        h1.addStretch(1)
        h1.addWidget(self.FBButton)

        self.goButton = QPushButton("&GO")
        self.goButton.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_G))
        self.goButton.setToolTip(u"開始抽抽樂 (Ctrl + G )")
        icong = QIcon()
        icong.addPixmap(QPixmap("icons/dice.png"), QIcon.Normal, QIcon.Off)
        self.goButton.setIcon(icong)
        self.goButton.setFocus()
        self.clearButton = QPushButton("&Clear")
        self.clearButton.setShortcut(QKeySequence(Qt.CTRL + Qt.Key_F))
        self.clearButton.setToolTip(u"清除...(Ctrl + F)")
        iconc = QIcon()
        iconc.addPixmap(QPixmap("icons/eraser.png"), QIcon.Normal, QIcon.Off)
        self.clearButton.setIcon(iconc)

        h2 = QHBoxLayout()
        h2.setMargin(10)
        h2.addWidget(self.goButton)
        h2.addWidget(self.clearButton)

        self.viewResultTable = QTableWidget(0, 3)
        self.viewResultTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.viewResultTable.setHorizontalHeaderLabels((u'學號', u'姓名', u'FaceBook大頭貼'))
        self.viewResultTable.verticalHeader().hide()
        self.viewResultTable.setShowGrid(False)
        h3 = QVBoxLayout()
        h3.setMargin(2)
        h3.addWidget(self.viewResultTable)

        self.exportButton = QPushButton(u"匯出名單(&E)")
        iconx = QIcon()
        iconx.addPixmap(QPixmap("icons/text.png"), QIcon.Normal, QIcon.Off)
        self.exportButton.setIcon(iconx)
        self.Like = QPushButton(u"答對了！")
        iconl = QIcon()
        iconl.addPixmap(QPixmap("icons/like.png"), QIcon.Normal, QIcon.Off)
        self.Like.setIcon(iconl)
        self.bad = QPushButton(u"答錯囉")
        h4 = QHBoxLayout()
        h4.setMargin(5)
        h4.addWidget(self.Like)
        h4.addStretch(10)
        h4.addWidget(self.bad)
        h4.addStretch(10)
        h4.addWidget(self.exportButton)

        layout = QVBoxLayout()
        layout.addLayout(h1)
        layout.addLayout(h2)
        layout.addLayout(h3)
        layout.addLayout(h4)

        self.setLayout(layout)
        self.setWindowTitle(u"抽抽樂")
        self.setWindowIcon(QIcon("icons/Flaticon_1430.png"))
        self.resize(650, 600)


    def createConnection(self):
        self.goButton.clicked.connect(lambda: self.random_choice(self.spinbox.value()))
        self.clearButton.clicked.connect(lambda: self.deloldtable())
        self.exportButton.clicked.connect(lambda: self.export())
        self.Like.clicked.connect(lambda: self.Likesound())
        self.bad.clicked.connect(lambda: self.badsound())
        self.FBButton.clicked.connect(lambda: self.downloadthread())
        self.viewResultTable.itemChanged.connect(lambda: self.status_update())
        self.checkA.stateChanged.connect(lambda: self.status_update())
        self.checkB.stateChanged.connect(lambda: self.status_update())

    def status_update(self):
        if self.checkA.isChecked() and self.checkB.isChecked():
            self.whichClass = ClassC
            random.shuffle(allnumber)
            self.includes = allnumber
        elif self.checkA.isChecked() and not self.checkB.isChecked():
            self.whichClass = ClassA
            random.shuffle(numA)
            self.includes = numA
        elif not self.checkA.isChecked() and self.checkB.isChecked():
            self.whichClass = ClassB
            random.shuffle(numB)
            self.includes = numB
        self.spinbox.setMaximum(len(self.includes))
        self.spinbox.setValue(1)


    def random_choice(self, numbers):
        if self.checkA.isChecked() and self.checkB.isChecked():
            self.whichClass = ClassC
            random.shuffle(allnumber)
            self.includes = allnumber
        elif self.checkA.isChecked() and not self.checkB.isChecked():
            self.whichClass = ClassA
            random.shuffle(numA)
            self.includes = numA
        elif not self.checkA.isChecked() and self.checkB.isChecked():
            self.whichClass = ClassB
            random.shuffle(numB)
            self.includes = numB

        for i in range(numbers):
            random.shuffle(self.includes)
            try:
                text = self.includes.pop()
                try:
                    allnumber.remove(text)
                except ValueError:
                    pass
                try:
                    numA.remove(text)
                except ValueError:
                    pass
                try:
                    numB.remove(text)
                except ValueError:
                    pass
            except IndexError:
                QMessageBox.warning(self,u"下面沒人了", u"都抽完了！\n請重新啟動程式吧~")
                break
            # print(type(text),text)
            # print("lense of allnumber is %d" % len(self.includes))

            self.shown.append(text)
            self.updateTableView(self.whichClass,text)

            if len(self.includes) == 0:
                QMessageBox.warning(self, u"下面沒人了", u"都抽完了！下面沒人了！\n請重新啟動程式吧~")
                break
            self.spinbox.setMaximum(len(self.includes))
            self.spinbox.setValue(1)

    def deloldtable(self):
        for i in reversed(range(self.row)):
            self.viewResultTable.removeRow(i)

    def downloadthread(self):
        import Qbatch_DL_FB_profile
        self.dl = Qbatch_DL_FB_profile.my_progress_bar()
        self.dl.show()



    def export(self):
        #依照系統編碼而定
        encoding = sys.getfilesystemencoding()
        print encoding

        allrows = self.viewResultTable.rowCount()
        result = u"學號\t姓名\n"
        for row in range(0, allrows):
            items = self.viewResultTable.item(row, 0).text()
            result += unicode(items) + "\t" + dict(ClassA.items() + ClassB.items())[str(items)] + "\n"

        import tempfile

        with tempfile.NamedTemporaryFile(mode='w+t', suffix='.txt', delete=False) as temp:
            temp.write(result.encode(encoding))
            #下面不要改成unicode 就可以避免UnicodeEncode Error
            des = (temp.name)#.decode(encoding)
        import subprocess
        subprocess.call(des,shell=True)


    def Likesound(self):
        #TODO 也許多加一點聲音
        QSound.play('Sound\\crowdapplause2.wav')

    def badsound(self):
        QSound.play('Sound\\laugh.wav')


    def updateTableView(self, whichClass, text):

        schoolNumber = QTableWidgetItem(text)
        studentName = QTableWidgetItem(whichClass[text])

        pic = "pic/"+ text + u".jpg"

        self.label = QLabel()
        #TODO 如何讓照片大小隨視窗大小變化

        width = 400
        hight = 400

        self.label.setPixmap(QPixmap(pic).scaledToWidth(width))
        self.label.resize(width, hight)
        self.row = self.viewResultTable.rowCount()
        self.viewResultTable.insertRow(self.row)

        self.viewResultTable.setRowHeight(self.row, hight)
        self.viewResultTable.setColumnWidth(2, width)
        self.viewResultTable.setItem(self.row, 0, schoolNumber)
        self.viewResultTable.setItem(self.row, 1, studentName)
        self.viewResultTable.setCellWidget(self.row, 2, self.label)
        self.viewResultTable.item(self.row, 0).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.viewResultTable.item(self.row, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


app = QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()

