import pandas
import pywpkit

kit = pywpkit.wpkit(adbpath=r"C:\\adbtools\adb.exe")

datafr = pandas.read_csv('Contacts.csv')

nums = []

for name, phone_num in datafr.iterrows():
    print(name, phone_num)
    nums.append(phone_num)

kit.adbmethod(None, "sup", morethanone=nums, alreadyawake=False, mode=2, passcode="1337")
