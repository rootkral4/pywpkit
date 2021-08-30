import pandas
import vobject
import pywpkit

kit = pywpkit.wpkit(adbpath=r"C:\\adbtools\adb.exe")
message="sup"

nums = []

with open("Contacts.vcf") as f:
    for v in vobject.readComponents(f):
        print(v.fn.value, v.tel.value)
        nums.append(v.tel.value)

kit.wbrowsermethod(None, message, nums, 15)
