#-*- coding:utf-8 -*-
__author__ = 'Aaron'

from time import time
import threading
import os

class_fb_dict = {"100003608826587": u"黃建程", "100001458104025": u"廖彥誠", "100000194374197": u"黃子瑋",
                 "100002000012788": u"許育菁", "100000106297579": u"李昕錞", "100000030683988": u"連欣慈",
                 "100001728784249": u"周靖倫", "100001584275396": u"林庭偉", "100000114887484": u"林秉叡",
                 "100001094195874": u"潘明哲", "100002911670253": u"呂政育", "100001725233904": u"陳奉儀",
                 "100001073450222": u"張鍇生", "100000992483825": u"余文傑", "100001569185026": u"蕭凱瑋",
                 "100000093378211": u"陳翊文", "100001631779094": u"陳柔樺", "100001722782839": u"詹鈞皓",
                 "100000104566845": u"蔡宛蓉", "100000338012334": u"陳一萱", "100000249724935": u"黃書儀", "1684176175": u"梁永淮",
                 "100001498426938": u"傅毓婷", "100001316782004": u"吳建德", "100001221536728": u"呂曼慈",
                 "100000164388955": u"陳盈蓉", "100000223412886": u"葉人輔", "1686103763": u"鄭翌玄", "100001372202601": u"吳俊昇",
                 "100003809197140": u"程偉智", "100000780846036": u"陳彥潔", "100000592306416": u"曾柏蒼",
                 "100001415351686": u"梁宜謙", "100000212411275": u"陳宥丞", "100000706215425": u"蔡宗霖",
                 "100001733077304": u"邱薪庭", "100002263184356": u"劉唯正", "wlhunag": u"黃文龍", "liao.y.xuan.92": u"廖育萱",
                 "ethan.lin.37": u"林邑宣", "ningchiao": u"詹甯喬", "vman.lee": u"李慧明", "chintzu.chuang": u"莊謹慈",
                 "yihua.sun.39": u"孫以華", "iris.chen.14203": u"陳毅珊", "chiahsuan.hu": u"胡家瑄", "justinianliu": u"劉晉嘉",
                 "fuanmaryjane.lee": u"李馥安", "successlarry": u"陳柏任", "abby.elizabeth.921": u"羅潔霞", "esxtfvuhnp": u"楊凱麟",
                 "arinaazuki": u"謝欣諭", "sumulie": u"張啟漢", "ferettechen": u"陳怡瑾", "ch.yang.790": u"楊君皓",
                 "chenupon": u"陳怡蓉", "xiao.l.yun": u"蕭立芸", "Nateliu33049": u"劉柏辰", "liming.chen.75": u"陳黎鳴",
                 "shenghua.wang": u"王聖驊", "leonyang810": u"楊昱晨", "dirianlove8217": u"張禾昀", "dora.chen.773": u"陳亭伊",
                 "jennyfirstfirst": u"蕭伃君", "wenchuan.dai": u"戴文川", "kevin.jungle.1": u"姜凱文", "justin.lin.393": u"林暉育",
                 "vector.he": u"何宗霖", "skywingmyth": u"李振廷", "james.chen.754": u"陳育德", "stylecoolme": u"陳泓諾",
                 "changan.chen.58": u"陳昶安", "junhan.jiang": u"江鈞翰", "johnny.lin.9406": u"林昌延", "wucrhow": u"吳銘浩",
                 "louisa.tsou.7": u"鄒心儀", "shixuez": u"張仕學", "chihkai.lee": u"李智凱", "rafaelshen": u"沈軒佑",
                 "chunhaos": u"蘇俊豪", "wenchun.huang.75": u"黃雯君", "chun.ji.180": u"莊淳霽"}

class_dict = {u"孫以華": "9830013", u"林秉叡": "9830014", u"傅毓婷": "9843524", u"陳昶安": "9930003", u"林暉育": "9930004",
              u"陳奉儀": "9930005", u"黃建程": "9930006", u"陳一萱": "9930007", u"蕭伃君": "9930008", u"李振廷": "9930009",
              u"陳黎鳴": "9930010", u"陳怡蓉": "9930011", u"陳泓諾": "9930012", u"林邑宣": "9930013", u"呂政育": "9930015",
              u"梁宜謙": "9930016", u"陳宥丞": "9930017", u"張啟漢": "9930019", u"楊凱麟": "9930021", u"李昕錞": "9930022",
              u"陳育德": "9930023", u"余文傑": "9930024", u"張仕學": "9930025", u"連欣慈": "9930026", u"許育菁": "9930027",
              u"陳亭伊": "9930028", u"黃文龍": "9930029", u"戴文川": "9930030", u"黃子瑋": "9930031", u"葉人輔": "9930032",
              u"胡家瑄": "9930033", u"沈軒佑": "9930034", u"曾柏蒼": "9930035", u"吳銘浩": "9930036", u"廖育萱": "9930037",
              u"鄭翌玄": "9930038", u"陳柏任": "9930039", u"莊謹慈": "9930040", u"程偉智": "9930041", u"陳怡瑾": "9940529",
              u"詹甯喬": "9943050", u"蕭立芸": "9970049", u"蕭凱瑋": "9917067", u"何宗霖": "9930045", u"吳俊昇": "9930046",
              u"林庭偉": "9930047", u"周靖倫": "9930048", u"楊昱晨": "9930049", u"蔡宗霖": "9930051", u"陳盈蓉": "9930052",
              u"陳柔樺": "9930053", u"王聖驊": "9930054", u"劉柏辰": "9930055", u"梁永淮": "9930056", u"姜凱文": "9930057",
              u"蔡宛蓉": "9930059", u"邱薪庭": "9930060", u"陳彥潔": "9930061", u"鄒心儀": "9930062", u"吳建德": "9930063",
              u"呂曼慈": "9930065", u"潘明哲": "9930068", u"李智凱": "9930069", u"劉唯正": "9930070", u"廖彥誠": "9930072",
              u"李馥安": "9930074", u"黃雯君": "9930076", u"江鈞翰": "9930077", u"林昌延": "9930078", u"劉晉嘉": "9930079",
              u"莊淳霽": "9930080", u"張鍇生": "9930081", u"詹鈞皓": "9930082", u"陳翊文": "9930083", u"陳毅珊": "9930084",
              u"蘇俊豪": "9930085", u"羅潔霞": "9930087", u"李慧明": "9930088", u"張禾昀": "9940023", u"楊君皓": "9952032",
              u"黃書儀": "9970531", u"謝欣諭": "9977005"}

import urllib2

base = r"https://graph.facebook.com/"
pref = r"/picture?width=9999&height=9999"
#ex:https://graph.facebook.com/louisa.tsou.7/picture?width=9999&height=9999

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
opener.addheaders = [('Referer', 'http://www.facebook.com')]


folderpath = os.path.join(os.getcwdu(), 'pic')
if not os.path.exists(folderpath):
    os.mkdir(folderpath)

#這邊改線程數量，不知改高一點會不會怎樣，剛剛測試一切正常~
thread_number = 40


def download(sequence):
    t = time()
    sequence = int(sequence)
    total = len(class_dict)

    #儲存聲音的資料夾
    for i in list(class_fb_dict)[sequence:total:thread_number]:
        newloc = os.path.join(folderpath, class_dict[class_fb_dict[i]].decode("utf-8") + u".jpg")
        try:

            with open(newloc, "wb") as fh:
                url = base + i + pref
                ufile = urllib2.urlopen(url).read()
                fh.write(ufile)
        except IOError as e:
            #怎麼把錯誤訊息傳回主程式？
            return e


    print "thread %d run time:" % sequence
    print time() - t


class MyThreading(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self, name=id)

    def run(self):
        download(self.name)


def main():
    tl = []            # 定義列表
    for i in range(thread_number):
        #如果不轉str，會因為0而產生ValueError: invalid literal for int() with base 10: 'Thread-1'
        i = str(i)
        t = MyThreading(i)
        tl.append(t)          # 將類對象添加到列表中

    for i in tl:
        i.start()           # 依次運行線程

#這行不要打錯了，免得一import 就執行
if __name__ == "__main__":
    main()


    #2013-11-19 without threading
    #total run time:
    #155.391000032


    #2014-01-02 using urllib2 and threading *15
    #total run time:
    #大約 12 秒


    #2014-01-02 using urllib2 and threading *40
    #total run time:
    #大約 7 秒