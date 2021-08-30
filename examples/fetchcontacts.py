import wpkit

kit = wpkit.wpkit(adbpath=r"C:\\adbtools\adb.exe")

contacts = kit._fetchcontacts()

for item in contacts:
    print(item)