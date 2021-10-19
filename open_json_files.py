import webbrowser
#nfdjkndflv
import os

count = 1
for filename in os.listdir('savetext'):
    webbrowser.open_new_tab(os.path.join('savetext', filename))
    count+=1
    if(count%100==0):
        input("Press enter to continue")