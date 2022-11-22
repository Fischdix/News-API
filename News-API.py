#! /usr/bin/env python3

# News API 
# Created by Jack Fischer
# 22 November 2022
# This script utilizes newsapi.org to pull headlines, and convert JSON to CSV
# Version 1.0


import requests
import json
import csv
import pandas as pd
import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Label
import sys



root = tk.Tk()
root.title('TICR Group News')
window_width = 600
window_height = 600
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.iconbitmap('Path to .ico photo')


###### This is just test stuff during development ######
#message = tk.Label(root, text="this is the root window").pack()
#message = tk.Label(test, text="this is the test window").pack()
#tk.Label(root, text='Classic Label').pack()
#ttk.Label(root, text='Themed Label').pack()
#photo = tk.PhotoImage(file='./tinkter_practice_img.png')
#def button_clicked():
#    print('Button clicked!')
#def close_button():
#    print('Later, Tater!')
#    exit()
#button = ttk.Button(root, text='Click here', command=button_clicked).pack()
#button = ttk.Button(root, text='Click here to close', command=close_button).pack()


#label = Label(root, text='This is a label')#, image=photo)
#label.pack(ipadx=10, ipady=10)

def close_button():
    print('Later, Tater!')
    sys.exit()
def pull_top_war():
    response = requests.get("https://newsapi.org/v2/top-headlines?q=war&apiKey=YOUR API KEY")
    print("HTTP Status: ",response.status_code) # Print status to terminal
    json_a = response.json() # convert repsonse to json
    formatted = json.dumps(json_a, indent=4) # Format json with indentions
    with open('top_war.json', mode='a') as f:
        f.write(formatted)
    with open('top_war.json', encoding='utf-8') as inputfile:
        df = pd.read_json(inputfile)
    df.to_csv('top_war.csv', encoding='utf-8', index=False) 


    

button = ttk.Button(root, text='Collect Top War Headlines', command=pull_top_war).pack()
button = ttk.Button(root, text='Click here to close', command=close_button).pack()

root.mainloop()
