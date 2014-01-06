#-*- coding: utf-8-*-
__author__ = 'Aaron'
from cx_Freeze import setup, Executable
import sys

if sys.platform == "win32":
    base = "Win32GUI"

#因為已經包含下列檔案了，所以就comment掉了
includefiles= ['icons','Sound','imageformats']

#記得要加上C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats 這個資料夾
includes = ['sip', 'PyQt4.QtCore']


setup(
        name = u"亂數抽籤程式",
        version = "1.0",
        description = u"亂數抽籤程式",
        options = {'build_exe': {'include_files':includefiles}},
        executables = [Executable("Random_choice.pyw" ,base = base, icon = "icons/Flaticon_1430.ico")])