# Frisbee Automated Texting

This library will be used to automate sending messages
to whatever numbers are in the numbers file. It will
send messages via the email that is setup in the login
file. There is currently no formatting for numbers yet
so each line in the numbers file should be 10 digits
followed by a new line. The login file contains two lines
`<email address>`
`<password>`

## Requirements:
The following items need to be installed in order for the program to run.
- openpyxl 2.4.8
- pip 9.0.1 or greater
- python 2.7 or greater
- pywapi 0.3.8 or greater
- selenium for python as well as a selenium firefox driver

### TO-DO:

There's a lot.
Automatically get a new practice calendar.
    - remove rows that were already used
Optimize code
Write tests (sorry Software Dev. Prof)
If possible, have it send all into one conversation instead of separate numbers.
Have to set up setuptools.py to install the dependencies listed above to make
it more user friendly.

### HOW TO USE
```bash
1. cd docs
2. touch numbers
3. touch login
```
4. Inside numbers, add a 10 digit number that you want to receive the message
	- The format should just be the numbers themselves, nothing extra
5. Run python setup.py
	- This will open up a selenium firefox window and process to get all the contacts with correct carriers gateways attached
6. Run python main_mod.py -h
	- This will display how to use the application



