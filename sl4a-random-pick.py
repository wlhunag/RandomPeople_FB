#-*- coding: utf-8-*-
__author__ = 'Aaron'
'''Android python app, first try!
There is some posts say that PyQt is available on Android, and some are trying to port python & PyQt4 to Android 
Maybe I should wait until they manage to finish the Android python app build process.

'''
import android
import time
import random

Class99 = {"9830013": u"孫以華", "9830014": u"林秉叡", "9843524": u"傅毓婷", "9930003": u"陳昶安", "9930004": u"林暉育",
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
             '9930016', '9930011', '9930010', '9930013', '9930012', '9940023', '9930059', '9930019', '9930080','9930069']
app = android.Android()
hello_msg = u"抽抽樂 App"
list_title = u'抽出幾人:'
quit_msg = u"Bye~"

def status_update(msg,how_long=2):
    app.makeToast(msg)
    time.sleep(how_long)

def random_choice(numbers):
    random.shuffle(allnumber)
    for i in range(numbers):
#        print "i = " + str(i)
        try:
            text = allnumber.pop()
#            print "text:%s" %text
            status_update( u"中獎的是%s！" %Class99[text],1)
            appa =android.Android()
            appa.dialogCreateAlert(u'中獎者','%s' %Class99[text])
            appa.dialogSetPositiveButtonText(u'繼續')
            appa.dialogShow()
            appa.dialogGetResponse().result
            appa.dialogDismiss()
        except IndexError:
            status_update( u"都抽完了！")

        if len(allnumber) == 0:
            status_update( u"都抽完了！")
            break
            
status_update(hello_msg)
numbers =['1','2','3']
while 1:
    app.dialogCreateAlert(list_title)
    app.dialogSetSingleChoiceItems(numbers)
    app.dialogSetPositiveButtonText(u'抽人')
    app.dialogSetNegativeButtonText(u'離開')
    app.dialogShow()
    resp = app.dialogGetResponse().result
    if resp['which'] in ('positive'):
        num = app.dialogGetSelectedItems().result[0]
#        print num+1
        app.dialogDismiss()
        random_choice(int(num)+1)
    if resp['which'] in ('negative'):
        break
status_update(quit_msg)
