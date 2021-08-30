import pywpkit
import pandas

kit = pywpkit.wpkit(adbpath=r"C:\\adbtools\adb.exe")

datafr = pandas.read_csv('Contacts.csv')
msg = "sup"
nums = []

for name, phone_num in datafr.iterrows():
    print(name, phone_num)
    nums.append(phone_num)

kit.adbmethod(None, msg, morethanone=nums, alreadyawake=False, mode=2, passcode="1337")
