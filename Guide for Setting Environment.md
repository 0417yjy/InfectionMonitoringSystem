# Installation
## Django project
### 1. Clone git repository
Linux Terminal / Windows cmd, PowerShell / Git bash
```
git clone https://github.com/0417yjy/InfectionMonitoringSystem.git
cd InfectionMonitoringSystem
```
[Git Download Link](https://git-scm.com/downloads)
***
### 2. Check python3 version
Linux Terminal / Windows cmd, PowerShell
```
python3 --version
```
or
```
python --version
```
*Python 3.6.9* or later  
[Python3 Download Link](https://www.python.org/downloads/)
***
### 3. Make a virtual environment
>Linux
>```
>python3 -m venv venv # Make a virtual environment named 'venv'
>```
>Windows (cmd, powershell)
>```
>python -m venv .\venv
>```
***
### 4. Activate the venv and check venv's default python version
>Linux
>```
>source venv/bin/activate # Activate venv
>```
>Windows (cmd)
>```
>venv\Scripts\activate.bat
>```
```
(venv) python --version
```
*Python 3.6.9* or later
***
### 5. Install required packages
```
(venv) python -m pip install --upgrade pip
(venv) pip install -r requirements.txt
```
### 6. Run Django server for test
```
(venv) cd django_monitoring
(venv) python manage.py runserver
```
After running the server in your localhost, check whether everything's good in to click [here](http://127.0.0.1:8000/)