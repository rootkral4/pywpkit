import vobject
import pywpkit


def main() -> None:
    """
    Example of getcontactsfromcsv
    """
    kit = pywpkit.wpkit(adbpath=r"C:\\adbtools\adb.exe")
    nums = []

    with open("Contacts.vcf", encoding="utf-8") as f:
        for v in vobject.readComponents(f):
            print(v.fn.value, v.tel.value)
            nums.append(v.tel.value)

    kit.wbrowsermethod(None, "sup", nums, 15)


