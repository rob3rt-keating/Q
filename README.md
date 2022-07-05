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
(venv) PS C:\Users\robert\Downloads> cd .\Q-master\
(venv) PS C:\Users\robert\Downloads\Q-master> cd .\Q-master\
(venv) PS C:\Users\robert\Downloads\Q-master\Q-master>ls


    Directory: C:\Users\robert\Downloads\Q-master\Q-master


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


(venv) PS C:\Users\robert\Downloads\Q-master\Q-master> python -m venv venv
(venv) PS C:\Users\robert\Downloads\Q-master\Q-master> pip install -r .\requirements.txt
Collecting anyio==3.6.1
  Using cached anyio-3.6.1-py3-none-any.whl (80 kB)
Collecting asgiref==3.5.2
  Using cached asgiref-3.5.2-py3-none-any.whl (22 kB)
[excerpt...]

(venv) PS C:\Users\robert\Downloads\Q-master\Q-master> .\venv\Scripts\activate
(venv) PS C:\Users\robert\Downloads\Q-master\Q-master> python.exe .\server.py

Running Q
Started server process 32316
Waiting for application startup.
Application startup complete.
Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```