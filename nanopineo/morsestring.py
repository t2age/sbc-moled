#!/usr/bin/python
# 
# This script uses Python2 syntax...
# sudo apt-get install python
#

import sys
import os

def morseLetter(theLetter):
    if (theLetter == 'A'):
        os.system("sudo ./A.sh");

    if (theLetter == 'B'):
        os.system("sudo ./B.sh");

    if (theLetter == 'C'):
        os.system("sudo ./C.sh");

    if (theLetter == 'D'):
        os.system("sudo ./D.sh");

    if (theLetter == 'E'):
        os.system("sudo ./E.sh");

    if (theLetter == 'F'):
        os.system("sudo ./F.sh");

    if (theLetter == 'G'):
        os.system("sudo ./G.sh");

    if (theLetter == 'H'):
        os.system("sudo ./H.sh");

    if (theLetter == 'I'):
        os.system("sudo ./I.sh");

    if (theLetter == 'J'):
        os.system("sudo ./J.sh");

    if (theLetter == 'K'):
        os.system("sudo ./K.sh");

    if (theLetter == 'L'):
        os.system("sudo ./L.sh");

    if (theLetter == 'M'):
        os.system("sudo ./M.sh");

    if (theLetter == 'N'):
        os.system("sudo ./N.sh");

    if (theLetter == 'O'):
        os.system("sudo ./O.sh");

    if (theLetter == 'P'):
        os.system("sudo ./P.sh");

    if (theLetter == 'Q'):
        os.system("sudo ./Q.sh");

    if (theLetter == 'R'):
        os.system("sudo ./R.sh");

    if (theLetter == 'S'):
        os.system("sudo ./S.sh");

    if (theLetter == 'T'):
        os.system("sudo ./T.sh");

    if (theLetter == 'U'):
        os.system("sudo ./U.sh");

    if (theLetter == 'V'):
        os.system("sudo ./V.sh");

    if (theLetter == 'X'):
        os.system("sudo ./X.sh");

    if (theLetter == 'Y'):
        os.system("sudo ./Y.sh");

    if (theLetter == 'Z'):
        os.system("sudo ./Z.sh");
        
        
    if (theLetter == '0'):
        os.system("sudo ./0.sh");
        
    if (theLetter == '1'):
        os.system("sudo ./1.sh");
        
    if (theLetter == '2'):
        os.system("sudo ./2.sh");
        
    if (theLetter == '3'):
        os.system("sudo ./3.sh");
        
    if (theLetter == '4'):
        os.system("sudo ./4.sh");
        
    if (theLetter == '5'):
        os.system("sudo ./5.sh");
        
    if (theLetter == '6'):
        os.system("sudo ./6.sh");
        
    if (theLetter == '7'):
        os.system("sudo ./7.sh");
        
    if (theLetter == '8'):
        os.system("sudo ./8.sh");
        
    if (theLetter == '9'):
        os.system("sudo ./9.sh");


if (len(sys.argv) < 2):
    # User did not give argument
    print "Need an argument...";
    print "sudo  python  morsestring.py  hello";
    sys.exit();

# convert letters to upper case
message = sys.argv[1].upper();
# remove blank spaces at start and end, if any...
message = message.strip();    

for letter in message:
    if (letter == ' '):
        # this is a space separating words...
        os.system("sudo ./6unit.sh");
    else:
        morseLetter(letter);
        # this is a space separating letters...
        os.system("sudo ./2unit.sh");

