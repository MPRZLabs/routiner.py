pull:
	adb pull /sdcard/sl4a/scripts/routiner.py
	adb pull /sdcard/sl4a/routiner.sqlite

push:
	adb push routiner.py /sdcard/sl4a/scripts
	adb push routiner.sqlite /sdcard/sl4a
