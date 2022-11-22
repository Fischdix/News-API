<h1 align="center">News-API</h1>

Requirements: Python 3.*, requests, json, csv, pandas, tkinter, tkinter.ttk, sys
Optional: pyinstaller

Required changes: Line 30 and 55 (path to ico img and API key)
Optional changes: Line 22, 59, 61, 63 (tkinter window name and file names)

<h3 align="center">━━━━━━━━━━━━</h3>
This script uses a VERY simple tkinter GUI in conjunction with newsapi.org to communicate with the top-headlines endpoint using my API key. 
The script then creates a JSON file and converts the JSON into a CSV file.
<h3 align="center">━━━━━━━━━━━━</h3>


To compile script into an .EXE using pyinstaller, (in py file directory) run: **pyinstaller --onefile News-API.py**

<h3 align="center">━━━━━━━━━━━━</h3>
To do:
-Create multiple buttons for different API search criteria (breaking news, trending, politics, etc)
-Fix CSV conversion to human readable
-Create function to pull the article photo and use Python Image Processing(PIL) to edit the photo to become ready for Instagram post.

![image](https://user-images.githubusercontent.com/59261070/203343476-f93037fa-d5cd-467a-b018-d43102223c44.png)
