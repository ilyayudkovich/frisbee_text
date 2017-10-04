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
Selenium firefox driver can be found here: https://github.com/mozilla/geckodriver/releases

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
4. cd ..
5. pip install -e .
```
6. Inside numbers, add a 10 digit number that you want to receive the message
	- The format should just be the numbers themselves, nothing extra
7. Run python setup.py
	- This will open up a selenium firefox window and process to get all the contacts with correct carriers gateways attached
```python
8. FrisbeeText -h
	- This will display how to use the application
```



