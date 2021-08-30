
# WPKIT (Whatsapp kit)

  

![wpkit banner](https://cdn.discordapp.com/attachments/739498862477312001/881784328927969310/unknown.png)

  

Python package to interact with whatsapp using different methods

  

#### Setup

  

    cd wpkit && pip install .

  

##### How to use

  

    import wpkit
    
    kit = wpkit.wpkit(adbpath=r"C:\\adbtools\adb.exe")
    
      
    
    kit.wbrowsermethod("90537xxxxxxx", "Hi")

  

Visit [examples](https://github.com/rootkral4/wpkit/tree/main/examples) folder for more example

  

#### Sending methods

  

- [X] ADB (Android Debug Bridge)
- [X] Webbrowser (Python package)
- [X] Selenium (Python package)
  

#### TO-DO

- [X] Selenium method

- [ ] General code clean up

- [ ] Maybe a chrome extension that sends message when requested from main application (not sure about this)

  

##### Known bugs/problems

  

-  [X] None for now yippee!