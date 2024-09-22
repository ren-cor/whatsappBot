## WhatsApp Bot

This project was created to help a group of users on a WhatsApp group chat to manage the group's bills and expenses using a google sheet as data storage.
This implementation was built to avoid the use of external apps such as tricount to manage the bills but use something that remains relatively user friendly.


## Table of Contents
- [Installation](#Installation)
- [Usage](#Usage)
- [License](#License)

# Installation

To install the WA bot follow these steps. (guide for linux/macOS)

1. Clone the repository to your local machine, from a terminal window use this command

```
git clone https://github.com/ren-cor/whatsappBot.git
```

2. Create a virtual environment using the requirements.txt file provided and activate it
```
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt
```

4. Create a the environemnt variables file
```
touch .env
```
5. Open up the .env file you just created using your favourite editor. To this file add the following configuration options:
```
GROUP_NAME=""
CHROME_SESSION="WA_bot"
HEADLESS=True

SERVICE_ACCOUNT = ''
SPREADSHEET_ID=""
```
You can replace the CHROME_SESSION variable with whatever you prefer, this is just the name of the Chrome profile that the application will use, you can leave the other variables blank for now.

6. Run the setup.py and login into WhatsApp web
```
python setup.py
```
After running, give it a few seconds for the browser to load and WhatsappWeb to open. At this point scan the QR code on screen to login with your account. Once everything has finished loading go back to the terminal and press return, the browser window should close.

# License
Distributed under the MIT license.
