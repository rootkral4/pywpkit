from webbrowser import open
from keyboard import press_and_release
from time import sleep
from subprocess import call, check_output, PIPE

class ADB_Keycodes:
    KEYCODE_HOME = "3"
    KEYCODE_POWER = "26"
    KEYCODE_ENTER = "66"
    KEYCODE_MENU = "82"
    KEYCODE_UNKNOWN = "0"
    KEYCODE_UNKNOWN = "0"
    KEYCODE_MENU = "1"
    KEYCODE_SOFT_RIGHT = "2"
    KEYCODE_HOME = "3"
    KEYCODE_BACK = "4"
    KEYCODE_CALL = "5"
    KEYCODE_ENDCALL = "6"
    KEYCODE_0 = "7"
    KEYCODE_1 = "8"
    KEYCODE_2 = "9"
    KEYCODE_3 = "10"
    KEYCODE_4 = "11"
    KEYCODE_5 = "12"
    KEYCODE_6 = "13"
    KEYCODE_7 = "14"
    KEYCODE_8 = "15"
    KEYCODE_9 = "16"
    KEYCODE_STAR = "17"
    KEYCODE_POUND = "18"
    KEYCODE_DPAD_UP = "19"
    KEYCODE_DPAD_DOWN = "20"
    KEYCODE_DPAD_LEFT = "21"
    KEYCODE_DPAD_RIGHT = "22"
    KEYCODE_DPAD_CENTER = "23"
    KEYCODE_VOLUME_UP = "24"
    KEYCODE_VOLUME_DOWN = "25"
    KEYCODE_POWER = "26"
    KEYCODE_CAMERA = "27"
    KEYCODE_CLEAR = "28"
    KEYCODE_A = "29"
    KEYCODE_B = "30"
    KEYCODE_C = "31"
    KEYCODE_D = "32"
    KEYCODE_E = "33"
    KEYCODE_F = "34"
    KEYCODE_G = "35"
    KEYCODE_H = "36"
    KEYCODE_I = "37"
    KEYCODE_J = "38"
    KEYCODE_K = "39"
    KEYCODE_L = "40"
    KEYCODE_M = "41"
    KEYCODE_N = "42"
    KEYCODE_O = "43"
    KEYCODE_P = "44"
    KEYCODE_Q = "45"
    KEYCODE_R = "46"
    KEYCODE_S = "47"
    KEYCODE_T = "48"
    KEYCODE_U = "49"
    KEYCODE_V = "50"
    KEYCODE_W = "51"
    KEYCODE_X = "52"
    KEYCODE_Y = "53"
    KEYCODE_Z = "54"
    KEYCODE_COMMA = "55"
    KEYCODE_PERIOD = "56"
    KEYCODE_ALT_LEFT = "57"
    KEYCODE_ALT_RIGHT = "58"
    KEYCODE_SHIFT_LEFT = "59"
    KEYCODE_SHIFT_RIGHT = "60"
    KEYCODE_TAB = "61"
    KEYCODE_SPACE = "62"
    KEYCODE_SYM = "63"
    KEYCODE_EXPLORER = "64"
    KEYCODE_ENVELOPE = "65"
    KEYCODE_ENTER = "66"
    KEYCODE_DEL = "67"
    KEYCODE_GRAVE = "68"
    KEYCODE_MINUS = "69"
    KEYCODE_EQUALS = "70"
    KEYCODE_LEFT_BRACKET = "71"
    KEYCODE_RIGHT_BRACKET = "72"
    KEYCODE_BACKSLASH = "73"
    KEYCODE_SEMICOLON = "74"
    KEYCODE_APOSTROPHE = "75"
    KEYCODE_SLASH = "76"
    KEYCODE_AT = "77"
    KEYCODE_NUM = "78"
    KEYCODE_HEADSETHOOK = "79"
    KEYCODE_FOCUS = "80"
    KEYCODE_PLUS = "81"
    KEYCODE_MENU = "82"
    KEYCODE_NOTIFICATION = "83"
    KEYCODE_SEARCH = "84"
    TAG_LAST_KEYCODE = "85"

class wpkit:
    def __init__(self, suppressbanner=False, adbpath="adbtools/adb.exe", swipe=[400, 200, 400, 500]) -> None:
        """
        :suppressbanner: False -> Print banner at startup, True -> Print nothing
        :adbpath: Path to adb ( necessary for adbmethod() and _fetchcontacts() )
        :swipe: swipe coordinates to unlock screen [x1,y1,x2,y2]
        """
        self.awake_lock = True
        self.swipe = swipe
        self.adbpath = adbpath
        if not suppressbanner:
            banner = """
            .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
            | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
            | | _____  _____ | || |   ______     | || |  ___  ____   | || |     _____    | || |  _________   | |
            | ||_   _||_   _|| || |  |_   __ \   | || | |_  ||_  _|  | || |    |_   _|   | || | |  _   _  |  | |
            | |  | | /\ | |  | || |    | |__) |  | || |   | |_/ /    | || |      | |     | || | |_/ | | \_|  | |
            | |  | |/  \| |  | || |    |  ___/   | || |   |  __'.    | || |      | |     | || |     | |      | |
            | |  |   /\   |  | || |   _| |_      | || |  _| |  \ \_  | || |     _| |_    | || |    _| |_     | |
            | |  |__/  \__|  | || |  |_____|     | || | |____||____| | || |    |_____|   | || |   |_____|    | |
            | |              | || |              | || |              | || |              | || |              | |
            | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
            '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
            """
            print(banner)
        self._startadbserver()
    
    def _startadbserver(self) -> None:
        """
        Start ADB daemon
        """
        call([self.adbpath, "start-server"], stdout=PIPE, stderr=PIPE)

    def _powerup(self) -> None:
        """
        Send POWER key through adb
        """
        call([self.adbpath, "shell", "input", "keyevent", ADB_Keycodes.KEYCODE_POWER])
        call([self.adbpath, "shell", "input", "keyevent", ADB_Keycodes.KEYCODE_MENU])

    def _sendenter(self) -> None:
        """
        Send ENTER key through adb
        """
        call([self.adbpath, "shell", "input", "keyevent", ADB_Keycodes.KEYCODE_ENTER])

    def _returnhome(self) -> None:
        """
        Send HOME key through adb
        """
        call([self.adbpath, "shell", "input", "keyevent", ADB_Keycodes.KEYCODE_HOME])

    def _stayawake(self, bright=True) -> int:
        """
        Keep phone busy so screen will not be locked until awake_lock set to False (blocks code use thread to run this function)

        :bright: True -> Set brightness to 5 while screen not locked (if awake_lock changes to false it reverts brightness level to user default), False -> Don't change brightness
        """
        brightness = check_output([self.adbpath, "shell", "settings", "get", "system", "screen_brightness"]) if bright == True else 100
        if bright:
            call([self.adbpath, "shell", "settings", "put", "system", "screen_brightness", "5"])
        while self.awake_lock:
            call([self.adbpath, "shell", "input", "keyevent", "mouse"])
            sleep(5)
        if bright:
            call([self.adbpath, "shell", "settings", "put", "system", "screen_brightness", brightness.strip()])
        
        return 1

    def _startwp(self):
        call([self.adbpath, "shell", "am", "start", "-n", "com.whatsapp/.Main"], stdout=PIPE)

    def _unlockscreen(self, mode, passcode=1234):
        if mode == 1:
            call([self.adbpath, "shell", "input", "touchscreen", "swipe", str(self.swipe[0]), str(self.swipe[1]), str(self.swipe[2]), str(self.swipe[3])])
        elif mode == 2:
            call([self.adbpath, "shell", "input", "touchscreen", "swipe", str(self.swipe[0]), str(self.swipe[1]), str(self.swipe[2]), str(self.swipe[3])])
            call([self.adbpath, "shell", "input", "text", f"{passcode}"])
            self._sendenter()

    def _fetchcontacts(self, screen_locked=False, mode=1, passcode="1234"):
        """
        Fetch all contacts from phone (no-root)

        :screen_locked: False -> fetch contacts now (use this if screen already unlocked),
        True -> Unlock screen then fetch contacts (use this if screen locked or won't fetching while locked)
        :mode: 1 - Swipe to unlock, 2 - Passcode (change passcode variable)
        :passcode: Passcode to unlock (not required for swipe)
        """
        if screen_locked:
            self._powerup()
            self._unlockscreen(mode, passcode)
            self._sendenter()
            ret = check_output([self.adbpath, "shell", "content", "query", "--uri", "content://com.android.contacts/data", "--projection", "display_name:data1:data4:contact_id"])
            values = ret.decode().splitlines()
            filteredvalues = list(filter(None, values))
        else:
            ret = check_output([self.adbpath, "shell", "content", "query", "--uri", "content://com.android.contacts/data", "--projection", "display_name:data1:data4:contact_id"])
            values = ret.decode().splitlines()
            filteredvalues = list(filter(None, values))
            
        return filteredvalues

    def adbmethod(self, number, msg, morethanone=None, alreadyawake=False, mode=1, passcode="1234"):
        """
        for this method USB Debugging should be enabled (enable "Always trust this computer") and 
        "enter is send" setting must be enabled (whatsapp > settings > chat > "Enter is send")

        :number: phone number to send message
        :msg: message to send
        :alreadyawake: True -> Screen already unlocked, False -> Unlock screen
        :mode: 1 - Swipe to unlock, 2 - Passcode (change passcode variable)
        :passcode: Passcode to unlock (not required for swipe)
        :bulk: None means single number if you want to send message to multiple numbers you should give a list to bulk
        :speed: how much time to wait before sending message (10 recommended for standart networks)
        """
    
        if alreadyawake == False:
            self._powerup()
            self._unlockscreen(mode, passcode)
        if morethanone == None:
            jid = number + "@s.whatsapp.net"
            self._startwp()
            sleep(1)
            call([self.adbpath, "shell", "am", "start", "-a", "android.intent.action.SEND",
            "-c", "android.intent.category.DEFAULT", "-t", "text/plain", "-e", "jid", jid, "-e", "android.intent.extra.TEXT", f"\"{msg}\"", "-p", "com.whatsapp"], stdout=PIPE)
            sleep(1.5)
            self._sendenter()
            self._returnhome()
        else:
            self._startwp()
            for num in morethanone:
                jid = num + "@s.whatsapp.net"
                call([self.adbpath, "shell", "am", "start", "-a", "android.intent.action.SEND",
                "-c", "android.intent.category.DEFAULT", "-t", "text/plain", "-e", "jid", jid, "-e", "android.intent.extra.TEXT", f"\"{msg}\"", "-p", "com.whatsapp"], stdout=PIPE)
                sleep(1)
                self._sendenter()


    def wbrowsermethod(self, number, msg, morethanone=None, speed=15):
        """
        for this method you must be logged in to web.whatsapp.com from your default browser

        :number: phone number to send message
        :msg: message to send
        :morethanone: None means single number if you want to send message to multiple numbers you should give a list to this variable
        :speed: how much time to wait before sending message (15 recommended)
        """
        print("[+] Don't touch anything !\nStarting to send message(s)")
        if morethanone == None:
            open("https://web.whatsapp.com/send?phone={}&text={}&app_absent=1".format(number, msg))
            sleep(speed)
            press_and_release('enter')
            sleep(0.5)
            press_and_release("ctrl + w")
        else:
            open("https://web.whatsapp.com/")
            sleep(5)
            for num in morethanone:
                open("https://web.whatsapp.com/send?phone={}&text={}&app_absent=1".format(num, msg), new=0)
                sleep(speed)
                press_and_release('enter')
            sleep(0.5)
            press_and_release("ctrl + w")
        sleep(1)
        press_and_release('enter') # confirm exit
        print("[+] Done")

if __name__ == "__main__":
    print("[!] Please don't run this file directly")