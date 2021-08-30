import pywpkit

kit = pywpkit.wpkit(adbpath=r"C:\\adbtools\adb.exe")

contacts = kit._fetchcontacts()

for item in contacts:
    print(item)