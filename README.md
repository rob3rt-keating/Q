
## Donation
> If you feel this application will help you on your learning path, feel free to send any amount you feel appropriate. Thank you!

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

Q is a Python web application designed to help you practice for the AZ-900 exam.@Spider1


### Features
* Real-time View Answers
* Add additional NOTES to questions
* Limit the number of questions
* Control the Categories you are tested on 
* History - Stats on the question you have seen
* Editor - Create and Edit your own questions
* Backup and Restore functionality
* Quiz results - Highlights focus areas
* SEARCH - Get a question by number quickly

<br>

Q is a Python web application designed to help you practice for the AZ-900 exam.@Spider1


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


PS C:\Users\x\Downloads\Q-master\Q-master> python -m venv venv
PS C:\Users\x\Downloads\Q-master\Q-master> pip install -r .\requirements.txt
Collecting anyio==3.6.1
  Using cached anyio-3.6.1-py3-none-any.whl (80 kB)
Collecting asgiref==3.5.2
  Using cached asgiref-3.5.2-py3-none-any.whl (22 kB)
[excerpt...]

PS C:\Users\x\Downloads\Q-master\Q-master> .\venv\Scripts\activate
(venv) PS C:\Users\x\Downloads\Q-master\Q-master> python.exe .\server.py

Running Q
Started server process 32316
Waiting for application startup.
Application startup complete.
Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```
## Using Q

From the main menu, select [START].
By default, questions are displayed in sequential order. Use [RANDOMIZE] to mix things up.
You can also [LIMIT # of QUESTIONS]

* If you do not select a category, all default categories will be used.

[VIEW ANSWER] - This will automatically score a FAIL for the question as well has display EXPLAIN, URL, custom NOTES.

[NEXT] - This will invisibly grade the question and advance to the next question.

After all the questions have been answered or skipped, the RESULTS page will be displayed showing success/fail counts per catagory.  If you hover over the success or fail counts, question IDs will be displayed.

* You can use the [SEARCH] on the menu bar to view questions without taking an exam


## Adding / Editing Questions

From the [TOOLS] menu, select [EDITOR].

This page is used for both editing existing questions and adding new ones.

TO EDIT: Enter the Question ID and click [Search], NOT Titlebar

To CREATE:
Question ID - Leave blank, SQL is set to auto-increment.  
* Newly created questions will have a starting ID of 1001.

BASIC / MULTI - Sets the question type. Basic: Only 1 answer.  Multi: 2 or more correct answers

ANSWERS - Denote correct answers with a checkmark.

EXPLAIN - Expandable window that accepts carriage returns (new lines).  No font formatting.

EXPLAIN_URL: Single link only. ** Future improvement: convert to a List-object

NOTES - During the practice exam, you can add notes.  Notes are visible after [View Answer] is pressed.

HISTORY - This field will keep track, over multiple exams, of your progress for each question. 

CATEGORY - The options are: cost, services, core, security and cost. Your new questions will be co-mingled with the base-installed questions, by category.
* You can create a custom name which you can access on the START page by selecting CUSTOM.  This will display all question with an ID > 1000.

> To save your new questions, [TOOLS] select [BACKUP DATABASE].
> 
> This will overwrite the 'questions.json' file. Don't worry, there is a backup of the original questions in the BAK directory
## Learning

* LABS
  - This is a list of the official labs used in the Microsoft Official Training (MOC).  If you complete these labs, you will have the required knowledge to pass UI/Procedural questions on the exam.

* MS Training
  - Microsoft also offers training (MOC).  You can choose Instructor led, or self-paced.  Here is the free courseware you will need.

* MS Exam Experience
  - Ever take a MS exam? Or maybe it's been a long time since you did take a MS exam, here is the opportunity to sit in a mock exam so you will not be surprised during the real exam