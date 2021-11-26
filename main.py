from tkinter import *

root = Tk()

def initcal():
    calc = Toplevel()
    root.withdraw()

    def on_closing():
        calc.destroy()
        root.deiconify()

    calc.protocol("WM_DELETE_WINDOW", on_closing)

myButton2 = Button(root, text="search", command=initcal)
myButton2.pack()
from pytube import *
import urllib.request
import re
# ******************************
# https://www.youtube.com/results?search_query=mozart
search_keyword = "Physics Explained in Ten Seconds"
main_search_keyword = search_keyword.replace(' ','')
html = urllib.request.urlopen("https://www.youtube.com/results?search_query="+main_search_keyword)
# print(html.read().decode())
video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
print(video_ids)
print("https://www.youtube.com/watch?v="+video_ids[0])
# ******************************

# returns a dictionary
root.mainloop()
