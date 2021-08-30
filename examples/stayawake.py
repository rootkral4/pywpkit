from threading import Thread
from time import sleep
import pywpkit

kit = pywpkit.wpkit(adbpath=r"C:\\adbtools\adb.exe")
Thread(target=kit._stayawake).start()

sleep(20) # sleep for 20 seconds
kit.awake_lock = False # release thread lock to stop thread

