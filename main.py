import threading
import os
import subprocess
import time
import socket

start_time = time.time()

art = '''
                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en:``
?MXT@Wx.~    :     ~"##*$$$$M~

.______    __  .__   __.   _______      ______    _______     _______   _______     ___   .___________. __    __  
|   _  \  |  | |  \ |  |  /  _____|    /  __  \  |   ____|   |       \ |   ____|   /   \  |           ||  |  |  | 
|  |_)  | |  | |   \|  | |  |  __     |  |  |  | |  |__      |  .--.  ||  |__     /  ^  \ `---|  |----`|  |__|  | 
|   ___/  |  | |  . `  | |  | |_ |    |  |  |  | |   __|     |  |  |  ||   __|   /  /_\  \    |  |     |   __   | 
|  |      |  | |  |\   | |  |__| |    |  `--'  | |  |        |  '--'  ||  |____ /  _____  \   |  |     |  |  |  | 
| _|      |__| |__| \__|  \______|     \______/  |__|        |_______/ |_______/__/     \__\  |__|     |__|  |__|

Made by github.com/k4k4du
                                                                                                                 
'''
lines = art.split('\n')

space_count = 0

direction = 1







def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    if time.time() - start_time > 5:
        clear_console()
        break

    for line in lines:
        print(' ' * space_count + line)
    space_count += direction

    if space_count == 20 or space_count == 0:
        direction *= -1
    time.sleep(0.1)

    clear_console()

print("Warning: Your IP address is sensitive information. Keep it private and don't share it with unauthorized parties.")
ip_address = input("Please enter the IP address you want to ping: ")
num_tabs = int(input("Please enter the number of CMD tabs you want to open: "))

try:
    for i in range(num_tabs):
        command = f"start cmd /c ping {ip_address}"
        subprocess.run(command, shell=True)
    print(f"Pinging {ip_address} in {num_tabs} separate CMD tabs.")

    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣼⣿⣅⣽⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣿⡟⠋⠀⠉⠀⠛⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⡇⠀⠀⠀⠀⢀⣻⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⣿⡶⣄⡶⣤⢾⣏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⠀⠀⠀⠀⠀⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣠⣤⣶⣶⠶⢶⣶⣶⣤⣄⣀⡈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣀⣰⣿⠉⢻⣷⣠⣀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣄⣠⣾⣿⠟⠉⣉⣤⣤⠀⠀⠀⠀⣩⣭⣝⠛⢿⣿⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣰⣿⠟⠛⠛⠋⠀⠀⢿⣟⠿⢿⣷⠀⠀⠀⢰⣿⠛⠁⠀⢹⣿⢁⡟⠀⠀⣧⣻⣹⣇⣤⣀⣸⣇⡿⣻⠇⠀⢿⠉⠻⣷⣤⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⠁⠀⠀⠀⠀⠀⣰⡾⠿⠷⠿⠿⠾⠿⠷⢿⣧⠀⠀⠀⠈⢿⣾⡇⠀⣀⡤⢭⣹⠋⠀⠀⢹⣯⠿⢭⡀⠀⠈⣇⣰⡿⠁⠀⠉⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠈⣿⡄⠀⠀⠀⠀⣼⣿⡳⢤⣄⡀⠀⠀⠀⠀⠈⢻⣧⣄⠀⠀⠀⢹⣿⠀⣿⠀⢠⡉⠳⠦⠴⠚⢁⣄⠀⢹⠀⣰⡟⠉⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⣿⣄⠀⠀⠀⣿⣇⠙⠂⠀⠀⠀⠀⠀⠀⠀⠀⣩⣿⡇⠀⠀⠀⢻⣧⡘⢧⡀⠙⠲⠦⠶⠖⠋⢁⡴⠋⣰⡿⠀⠀⠀⠀⠀⠀⠀⣼⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⠙⠿⠿⠿⠛⠹⢿⣦⣀⠀⠀⠀⠀⠀⠀⣾⡏⠁⠀⠀⠀⠀⠀⠙⢿⣦⣍⣛⠲⠶⠶⠶⠛⣉⣠⡾⠏⠀⠀⢠⣶⠶⣶⣶⣾⣏⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢷⣦⣤⣀⠀⠀⠸⣷⣄⠀⠀⠀⣀⣄⠀⠀⠉⠙⠻⠿⠿⠿⡿⠿⠛⠋⠁⠀⠀⠀⣿⡇⠀⠀⠀⠀⠉⠻⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠻⠿⢶⣾⡿⢿⣶⡿⠛⠛⢿⣄⠀⠀⠀⠀⢠⣾⠿⣦⡀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣀⣤⣴⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⠀⠀⠀⠀⢸⣿⡀⠀⠀⢀⣿⠃⠀⠘⣿⠀⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠙⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣾⠟⠉⠉⠉⠉⢻⣦⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣿⡇⠀⠀⠀⠀⠀⠀⠙⠿⢷⡾⣟⣁⠀⠀⠀⠻⣷⣦⣀⣠⣾⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀
⢠⣿⠁⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⢀⣴⡾⠟⠛⠛⠛⢻⣷⠀⠀⠀⠀⠀⠀⢰⡖⠚⠙⠋⠈⢧⣄⡀⠀⠀⠈⠉⠉⠀⠀⠀⠀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣄⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠀⠀⠀⠀⠀⠀⠐⢿⣧⣀⣾⠟⠁⠀⠀⠀⠀⠀⠈⣿⣆⡀⠀⠀⠀⠀⣸⡇⠀⠀⠀⠀⢸⣏⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣦⡀⠀⠀⠀⠀⠀⠀⡀⠀⢿⣆⣶⣶⣄⠀⠀⠀
⠸⣿⠀⠀⠀⠀⠀⠀⠀⠈⣻⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠘⠛⠁⠀⠀⠀⠀⠙⠶⠺⣆⣴⠶⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⠹⣷⣄⠀⠀⠀⠀⡀⠘⣆⠈⢿⡏⠙⣿⡄⠀⠀
⠀⢿⣆⠀⠀⠀⠀⠀⠀⠀⣿⣇⣠⠴⣛⣥⠖⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡆⠈⠻⣷⣄⡀⠀⠳⣄⠈⣆⢈⣿⣾⣿⡁⠀⠀
⠀⠘⣿⣄⠀⠀⠀⠀⠀⠀⣿⣯⣶⡋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠈⠙⠿⣶⣤⣈⣣⣽⣿⠋⠉⠛⠛⢷⡆
⠀⠀⠈⢿⣦⡀⠀⠀⠀⢸⣿⠿⠟⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠉⢹⡿⠉⠁⠀⠀⠀⠀⣠⣿
⠀⠀⠀⠀⠛⢿⣦⣀⣀⣸⣧⡀⣠⣼⡿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⢸⣇⠀⠀⠀⠀⠀⠈⣿⡅
⠀⠀⠀⠀⠀⠀⠉⠛⠛⠋⠙⠻⠟⠻⠿⠶⣦⣤⣤⣤⣤⣤⣤⣴⡶⠿⠛⠉⢸⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⢀⣿⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣶⣤⣀⣤⡾⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⡷⠀⢀⠀⠀⠀⠀⠀⠀⠀⣴⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⡆⠀⣷⠀⣾⠀⠀⢀⠀⠀⢀⣼⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡀⢹⣠⣿⣤⣾⡿⠿⣶⣿⣉⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⡾⠟⠻⣾⣿⣽⣿⡉⠁⠀⣌⣹⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠋⠀⠀⠀⠀⠀⠙⣿⣀⣈⡛⢰⣼⣿⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⠛⢹⣿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣇⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣧⡄⠀⠀⠀⠀⣀⣴⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣛⠿⠷⠾⠿⠛⢉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
except subprocess.CalledProcessError:
    print("Invalid IP address")