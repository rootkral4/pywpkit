import pywpkit

kit = pywpkit.wpkit(adbpath=r"C:\\adbtools\adb.exe")

contacts = kit.fetchcontacts()

for item in contacts:
    print(item)
