@echo off
@setup_cxfreeze.py build
@echo ���U�ӭn���Y�üƵ{��

"C:\Program Files\7-Zip\7z.exe" a -tzip G:\Installer\�üƵ{��.zip build\exe.win32-2.7
@echo ���U�ӭn�s�@�w���ɮ�

@echo
"C:\Program Files (x86)\Inno Setup 5\Compil32.exe" /cc "C:\Users\Aaron\Documents\random_choice_portable_Ramdisk.iss"

@echo
@echo ���U�ӭn�s�u�� ftp
pause

"C:\Program Files (x86)\FileZilla FTP Client\filezilla.exe" --site="0D99 manager"