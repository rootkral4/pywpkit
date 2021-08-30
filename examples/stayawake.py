from threading import Thread
from time import sleep
import wpkit

kit = wpkit.wpkit(adbpath=r"C:\\adbtools\adb.exe")
Thread(target=kit._stayawake).start()

sleep(20) # after 20 seconds stop thread
kit.awake_lock = False

