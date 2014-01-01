@echo off
@setup_cxfreeze.py build
@echo 接下來要壓縮亂數程式

"C:\Program Files\7-Zip\7z.exe" a -tzip G:\Installer\亂數程式.zip build\exe.win32-2.7
@echo 接下來要製作安裝檔案

@echo
"C:\Program Files (x86)\Inno Setup 5\Compil32.exe" /cc "C:\Users\Aaron\Documents\random_choice_portable_Ramdisk.iss"

@echo
@echo 接下來要連線到 ftp
pause

"C:\Program Files (x86)\FileZilla FTP Client\filezilla.exe" --site="0D99 manager"