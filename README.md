# Frisbee Automated Texting

This library will be used to automate sending messages
to whatever numbers are in the numbers file. It will
send messages via the email that is setup in the login
file. There is currently no formatting for numbers yet
so each line in the numbers file should be 10 digits
followed by a new line. The login file contains two lines
`<email address>`
`<password>`

### Requirements:
The following items need to be installed in order for the program to run.
Selenium firefox driver can be found here: https://github.com/mozilla/geckodriver/releases
Once this is downloaded:
```bash
1. go to downloads folder (eg. cd ~/Downloads/ if on linux)
2. tar -xvf <file downloaded>
3. mv geckodriver /usr/bin/
```

### HOW TO USE
Note: Do this after cloning
```bash
1. cd frisbee_text
2. pip install -e .
3. python setup.py build
4. python setup.py install
5. FrisbeeText -h
```


### TO-DO:

There's a lot.
Automatically get a new practice calendar.
    - remove rows that were already used
Optimize code
Write tests (sorry Software Dev. Prof)
If possible, have it send all into one conversation instead of separate numbers.
Have to set up setuptools.py to install the dependencies listed above to make
it more user friendly.