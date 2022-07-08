
## Donation
> If you think that any information you obtained here is worth of some money and are willing to pay for it, feel free to send any amount through paypal.

<table>
<th>Paypal</th>
<th>Vimeo</th>
<tr>
    <td>
        <a href="https://paypal.me/jameskeating1509">
        <img src="https://raw.githubusercontent.com/stefan-niedermann/paypal-donate-button/master/paypal-donate-button.png" height="80" width="160" alt="Donate with PayPal" />
        </a>
    </td>
    <td> <a href="https://www.venmo.com/tonya-keating">
        <img src="https://raw.githubusercontent.com/rob3rt-keating/Q/master/static/images/venmo.png" height="60" width="60" alt="Donate with Venmo" />
        </a> </td>

</table>

# Q

Q is a Python web application designed to help you practice for the AZ-900 exam

## Installation

(assuming you have Python 3.7 or greater already installed)

1) Download the application (.zip) file, and unpack it in a directory of your choosing.
2) Create a virtual environment.
```bash 
   python -m venv venv
   ```
3) Next activate the virtual environment
```bash 
   .\venv\Scripts\activate
   ```

4) Install the python dependencies
```bash 
   pip -install -r requirements
   ```
5) Run the application
```bash 
   python server.py
   ```
6) ```bash 
   Navigate to http://localhost:8080
   ```

## Actual  install commands (if you get stuck)

```bash
(venv) PS C:\Users\x\Downloads> cd .\Q-master\
(venv) PS C:\Users\x\Downloads\Q-master> cd .\Q-master\
(venv) PS C:\Users\x\Downloads\Q-master\Q-master>ls


    Directory: C:\Users\x\Downloads\Q-master\Q-master


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----          7/4/2022   3:00 PM                static
d-----          7/4/2022   3:00 PM                templates
-a----          7/4/2022   3:00 PM         270913 database.py
-a----          7/4/2022   3:00 PM          11433 main.py
-a----          7/4/2022   3:00 PM         278528 questions.db
-a----          7/4/2022   3:00 PM         293509 questions.json
-a----          7/4/2022   3:00 PM           1068 requirements.txt
-a----          7/4/2022   3:00 PM            149 server.py
-a----          7/4/2022   3:00 PM        1101312 sqlite3.exe


(venv) PS C:\Users\x\Downloads\Q-master\Q-master> python -m venv venv
(venv) PS C:\Users\x\Downloads\Q-master\Q-master> pip install -r .\requirements.txt
Collecting anyio==3.6.1
  Using cached anyio-3.6.1-py3-none-any.whl (80 kB)
Collecting asgiref==3.5.2
  Using cached asgiref-3.5.2-py3-none-any.whl (22 kB)
[excerpt...]

(venv) PS C:\Users\x\Downloads\Q-master\Q-master> .\venv\Scripts\activate
(venv) PS C:\Users\x\Downloads\Q-master\Q-master> python.exe .\server.py

Running Q
Started server process 32316
Waiting for application startup.
Application startup complete.
Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```

## Adding / Editing Questions

The manual method 
Step 1 - Open the 'questions.json' file.Edit any question you like and save the json file.
Step 2 - In the UI, select TOOLS/RESTORE Database.  This will delete the .db file and create a new .db file and populate it with the contents of the 'questions.json' file.

You can use this approach to ADD new questions. ** Make sure NOT to duplicate the ID number

A UI-based editor is currently being developed.