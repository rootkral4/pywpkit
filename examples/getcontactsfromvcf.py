import pywpkit
import pandas
import vobject

kit = pywpkit.wpkit(adbpath=r"C:\\adbtools\adb.exe")
msg="sup"

vcf_path = "Contacts.vcf"

nums = []

with open(vcf_path) as f:
    for v in vobject.readComponents(f):
        print(v.fn.value, v.tel.value)
        nums.append(v.tel.value)

kit.wbrowsermethod(None, msg, nums, 15)