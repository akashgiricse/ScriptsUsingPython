# How to use this script

### Getting started
Dependenciies:
- Python 3.6.x
- Ubuntu 17.04 or later or Linux Mint 18.x 

#### 1. Clone this repoistory
```bash
git clone https://github.com/akashgiricse/ScriptsUsingPython.git
cd quiz_app
```

### Copy any text which contains phone numbers and emails.

### 2. Open terminal in PhoneNumberAndEmailAddressExtractor directory and type
```
python3 phoneAndEmail.py
```

if you get the error "cannot import pyperclip", run this command 
```
sudo apt-get install python3-pip  
sudo pip3 install --upgrade pip
sudo pip3 install setuptools
sudo pip3 install pyperclip
```

if you get the error "Pyperclip could not find a copy/paste mechanism for your system. Please see https://pyperclip.readthedocs.io/en/latest/introduction.html#not-implemented-error for how to fix this.", run this command
```
sudo apt-get install xclip
```