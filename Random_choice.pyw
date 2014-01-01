#-*- coding: utf-8-*-

__author__ = 'Aaron'
import win32com.client
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import os
import sys
from time import time
import urllib2

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
        '9930063', '9930045', '9930068', '9930079', '9930078', '9940023', '9930074', '9977005', '9930060',
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
             '9930016', '9930011', '9930010', '9930013', '9930012', '9940023', '9930059', '9930019', '9930080']

class Downloader():

    def __init__(self,text):
        self.Classmap = {'9830013': 'yihua.sun.39',
                         '9830014': '100000114887484',
                         '9843524': '100001498426938',
                         '9917067': '100001569185026',
                         '9930003': 'changan.chen.58',
                         '9930004': 'justin.lin.393',
                         '9930005': '100001725233904',
                         '9930006': '100003608826587',
                         '9930007': '100000338012334',
                         '9930008': 'jennyfirstfirst',
                         '9930009': 'skywingmyth',
                         '9930010': 'liming.chen.75',
                         '9930011': 'chenupon',
                         '9930012': 'stylecoolme',
                         '9930013': 'ethan.lin.37',
                         '9930015': '100002911670253',
                         '9930016': '100001415351686',
                         '9930017': '100000212411275',
                         '9930019': 'sumulie',
                         '9930021': 'esxtfvuhnp',
                         '9930022': '100000106297579',
                         '9930023': 'james.chen.754',
                         '9930024': '100000992483825',
                         '9930025': 'shixuez',
                         '9930026': '100000030683988',
                         '9930027': '100002000012788',
                         '9930028': 'dora.chen.773',
                         '9930029': 'wlhunag',
                         '9930030': 'wenchuan.dai',
                         '9930031': '100000194374197',
                         '9930032': '100000223412886',
                         '9930033': 'chiahsuan.hu',
                         '9930034': 'rafaelshen',
                         '9930035': '100000592306416',
                         '9930036': 'wucrhow',
                         '9930037': 'liao.y.xuan.92',
                         '9930038': '1686103763',
                         '9930039': 'successlarry',
                         '9930040': 'chintzu.chuang',
                         '9930041': '100003809197140',
                         '9930045': 'vector.he',
                         '9930046': '100001372202601',
                         '9930047': '100001584275396',
                         '9930048': '100001728784249',
                         '9930049': 'leonyang810',
                         '9930051': '100000706215425',
                         '9930052': '100000164388955',
                         '9930053': '100001631779094',
                         '9930054': 'shenghua.wang',
                         '9930055': 'Nateliu33049',
                         '9930056': '1684176175',
                         '9930057': 'kevin.jungle.1',
                         '9930059': '100000104566845',
                         '9930060': '100001733077304',
                         '9930061': '100000780846036',
                         '9930062': 'louisa.tsou.7',
                         '9930063': '100001316782004',
                         '9930065': '100001221536728',
                         '9930068': '100001094195874',
                         '9930069': 'chihkai.lee',
                         '9930070': '100002263184356',
                         '9930072': '100001458104025',
                         '9930074': 'fuanmaryjane.lee',
                         '9930076': 'wenchun.huang.75',
                         '9930077': 'junhan.jiang',
                         '9930078': 'johnny.lin.9406',
                         '9930079': 'justinianliu',
                         '9930080': 'chun.ji.180',
                         '9930081': '100001073450222',
                         '9930082': '100001722782839',
                         '9930083': '100000093378211',
                         '9930084': 'iris.chen.14203',
                         '9930085': 'chunhaos',
                         '9930087': 'abby.elizabeth.921',
                         '9930088': 'vman.lee',
                         '9940023': 'dirianlove8217',
                         '9940529': 'ferettechen',
                         '9943050': 'ningchiao',
                         '9952032': 'ch.yang.790',
                         '9970049': 'xiao.l.yun',
                         '9970531': '100000249724935',
                         '9977005': 'arinaazuki'}

        # eg: https://graph.facebook.com/louisa.tsou.7/picture?width=9999&height=9999

    def download(self,text):
        t = time()

        base = r"https://graph.facebook.com/"
        pref = r"/picture?width=9999&height=9999"
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        opener.addheaders = [('Referer', 'http://www.facebook.com')]

        folderpath = os.getcwdu()
        profileID = self.Classmap[text.decode('utf-8')]

        #儲存聲音的資料夾
        piclocation = os.path.join(folderpath,"pic")
        newloc = os.path.join(piclocation, text + ".jpg")
        with open(newloc, "wb") as fh:
            url = base + profileID + pref
            ufile = urllib2.urlopen(url).read()
            fh.write(ufile)
            #data = urllib.urlretrieve(base + i.split('\t')[0] + pref,newloc)

        print time() - t

class Example(QWidget):
    def __init__(self, parent=None):
        super(Example, self).__init__(parent)

        self.createLayout()
        self.createConnection()
        self.remember = 0
        self.collect = [0]
        self.shown = []


    def createLayout(self):
        self.label = QLabel()
        self.label.setText(u"選出幾人")
        self.spinbox = QSpinBox()
        self.spinbox.size()
        self.spinbox.setRange(1, 82)
        self.spinbox.setValue(1)
        self.spinbox.sizeHint()

        self.labelFB = QLabel(u"即時大頭貼")
        self.checkFB = QCheckBox()
        self.checkFB.setChecked(True)

        self.labelA = QLabel(u"甲班")
        self.labelB = QLabel(u"乙班")
        self.checkA = QCheckBox()
        self.checkA.setChecked(True)
        self.checkB = QCheckBox()
        self.checkB.setChecked(True)

        h1 = QHBoxLayout()
        h1.addWidget(self.label)
        h1.addWidget(self.spinbox)
        h1.addStretch()
        h1.addWidget(self.labelFB)
        h1.addWidget(self.checkFB)
        h1.addWidget(self.labelA)
        h1.addWidget(self.checkA)
        h1.addWidget(self.labelB)
        h1.addWidget(self.checkB)

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
        self.Like = QPushButton(u"答對了！")
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


    def random_choice(self, numbers):

        import random

        if self.checkA.isChecked() and self.checkB.isChecked():
            whichClass = ClassC
            random.shuffle(allnumber)
            includes = allnumber
        elif self.checkA.isChecked() and not self.checkB.isChecked():
            whichClass = ClassA
            random.shuffle(numA)
            includes = numA
        elif not self.checkA.isChecked() and self.checkB.isChecked():
            whichClass = ClassB
            random.shuffle(numB)
            includes = numB


        for i in range(numbers):
            random.shuffle(includes)
            try:
                text = includes.pop()
            except IndexError:
                QMessageBox.warning(self,u"下面沒人了", u"都抽完了！\n請重新啟動程式吧~")
                break
            print(type(text),text)

            if text in self.shown:
                self.random_choice(numbers)
                self.shown.append(text)
                self.spinbox.setFocus(True)
            else:
                self.shown.append(text)
                self.updateTableView(whichClass,text)
                speaker = win32com.client.Dispatch('SAPI.SpVoice')
                speaker.Speak(u"中獎的是，{0}!".format(whichClass[text]))

    def deloldtable(self):

        #delnumber = self.collect[self.remember]
        for i in range(self.spinbox.value()):
            self.viewResultTable.removeRow(i)


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
            des = (temp.name).decode(encoding)
        #以下這行可能只有windows 適用
        os.system(des)


    def Likesound(self):
        QSound.play('Sound\\crowdapplause2.wav')

    def badsound(self):
        QSound.play('Sound\\laugh.wav')


    def updateTableView(self, whichClass, text):

        schoolNumber = QTableWidgetItem(text)
        studentName = QTableWidgetItem(whichClass[text])

        #即時FB大頭貼
        if self.checkFB.isChecked():
            try:
                c = Downloader(text)
                c.download(text)
            except:
                pass

        pic = "pic/"+ text + u".jpg"

        self.label = QLabel()

        self.label.setPixmap(QPixmap(pic).scaledToWidth(400))
        #self.label.setPixmap(QPixmap(pic).copy())
        self.label.resize(400, 400)

        row = self.viewResultTable.rowCount()
        self.viewResultTable.insertRow(row)

        self.viewResultTable.setRowHeight(row, 400)
        self.viewResultTable.setColumnWidth(2, 400)
        self.viewResultTable.setItem(row, 0, schoolNumber)
        self.viewResultTable.setItem(row, 1, studentName)
        self.viewResultTable.setCellWidget(row, 2, self.label)
        self.viewResultTable.item(row, 0).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.viewResultTable.item(row, 1).setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)


app = QApplication(sys.argv)
ex = Example()
ex.show()
app.exec_()

