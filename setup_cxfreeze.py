#-*- coding: utf-8-*-
__author__ = 'Aaron'
from cx_Freeze import setup, Executable
import sys

if sys.platform == "win32":
    base = "Win32GUI"

#因為已經包含下列檔案了，所以就comment掉了
includefiles= ['icons','imageformats','Flaticon_1430.ico','Sound/laugh.wav','Sound/crowdapplause2.wav']
# includefiles= ['imageformats\qgif4.dll','imageformats\qico4.dll','imageformats\qjpeg4.dll','imageformats\qmng4.dll','imageformats\qsvg4.dll','imageformats\qtga4.dll','imageformats\qtiff4.dll','Flaticon_1430.png','Flaticon_1430.ico','Sound/laugh.wav','Sound/crowdapplause2.wav',"pic/9830013.jpg","pic/9830014.jpg","pic/9843524.jpg","pic/9930003.jpg","pic/9930004.jpg","pic/9930005.jpg","pic/9930006.jpg","pic/9930007.jpg","pic/9930008.jpg","pic/9930009.jpg","pic/9930010.jpg","pic/9930011.jpg","pic/9930012.jpg","pic/9930013.jpg","pic/9930015.jpg","pic/9930016.jpg","pic/9930017.jpg","pic/9930019.jpg","pic/9930021.jpg","pic/9930022.jpg","pic/9930023.jpg","pic/9930024.jpg","pic/9930025.jpg","pic/9930026.jpg","pic/9930027.jpg","pic/9930028.jpg","pic/9930029.jpg","pic/9930030.jpg","pic/9930031.jpg","pic/9930032.jpg","pic/9930033.jpg","pic/9930034.jpg","pic/9930035.jpg","pic/9930036.jpg","pic/9930037.jpg","pic/9930038.jpg","pic/9930039.jpg","pic/9930040.jpg","pic/9930041.jpg","pic/9940529.jpg","pic/9943050.jpg","pic/9970049.jpg","pic/9917067.jpg","pic/9930045.jpg","pic/9930046.jpg","pic/9930047.jpg","pic/9930048.jpg","pic/9930049.jpg","pic/9930051.jpg","pic/9930052.jpg","pic/9930053.jpg","pic/9930054.jpg","pic/9930055.jpg","pic/9930056.jpg","pic/9930057.jpg","pic/9930059.jpg","pic/9930060.jpg","pic/9930061.jpg","pic/9930062.jpg","pic/9930063.jpg","pic/9930065.jpg","pic/9930068.jpg","pic/9930069.jpg","pic/9930070.jpg","pic/9930072.jpg","pic/9930074.jpg","pic/9930076.jpg","pic/9930077.jpg","pic/9930078.jpg","pic/9930079.jpg","pic/9930080.jpg","pic/9930081.jpg","pic/9930082.jpg","pic/9930083.jpg","pic/9930084.jpg","pic/9930085.jpg","pic/9930087.jpg","pic/9930088.jpg","pic/9940023.jpg","pic/9952032.jpg","pic/9970531.jpg","pic/9977005.jpg"]
#記得要加上C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats 這個資料夾
includes = ['sip', 'PyQt4.QtCore']


setup(
        name = "Random_Choice",
        version = "0.5",
        description = u"亂數抽籤程式",
        options = {'build_exe': {'include_files':includefiles}},
        executables = [Executable("Random_choice.pyw" ,base = base, icon = "Flaticon_1430.ico")])