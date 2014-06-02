#Algebra Solver 1.0

---------------------------------------------------------------

###Written by: Sam Rapaport
###Contact: samrapdev.com
###Report a bug: rapaport.sam7@gmail.com

---------------------------------------------------------------

Algebra Solver is a command line application for solving simple
and complicated algebraic formulas and equations. The interface
combines Python's IDLE prompt style with the simple notation of
command line functions for an easy-to-learn command line function
calculator. Users, read sections 1-4 to learn about easy
installation and the various functions this program has to offer!
Devlopers, skip to section 5 for a quick intro on the structure
of the program.

>> **Table of Contents**

>>* Section 1:        Installation
* Section 2:          Running the program
* Section 3:          Navigating around
* Section 4:          Using the manuals
* Section 5:          Developers

---------------------------------------------------------------

## Section 1 | Installation

Welcome to Algebra Solver! In this section we will go over the
installation process. It is very simple,  but if you've never
used the command line, you'll need to pay attention.  Most of
the instructions apply to all platforms, but in general they
refer to Mac OSX/Unix and Linux operating systems. If you are on
Windows, a quick tutorial on the command line is recommended.

1. The first step is to save this folder to somewhere that is
easy to get to. I suggest saving it straight to your Desktop,
but it is completely up to you. The following instructions
will assume the folder (called a directory) is saved to the
desktop. Once the directory is saved to the desktop, open the
terminal. On Mac, the terminal is located in the Applications
folder under "utilities". Open the app, wait for $ to show up
and type the following (<enter> means to type the enter/return
key, do not type '<enter>'):

    cd Desktop/algebrasolver<enter>

(Note that if you saved the algebra folder somewhere besides
the desktop, you will need to replace that command with the
correct path. If you don't know what that means, it is best
to just save it in your Desktop.)

---------------------------------------------------------------

## Section 2 | Running the program

1. You are now inside of the application folder. To start the
application type:

    python algebra.py<enter>

2. The app should now be up and running, with a '>>>' prompt
displayed. Read ahead to see how to use the app!

---------------------------------------------------------------

## Section 3 | Navigating around

Now we will look at how to navigate around the program and use
all the awesome functions. Now that the folder is installed in
the Desktop, to use the program from now on, all you have to do
is open the terminal and type:

    cd Desktop/algebrasolver<enter>
    python algebra.py<enter>

(Remember <enter> means hit the 'enter' or 'return' key, do not
type 'enter'!)

The first time the program is started, a prompt asking you to
create a username will pop up. Type a username and hit <enter>
or skip it by typing ! and then <enter>

Everytime the program opens, the following prompt is displayed:

    Algebra Solver 1.0
    Type 'man' for more info
    >>>

Type the word 'man' (short for manual) to open up the user
manual. A short text file will be displayed showing the various
commands you can type in to calculate an equation. Don't worry
about accidentally entering the wrong thing, an error message
will be displayed and then you can continue on. Let's take a
look at using a function on the algebra command line:

    >>> s<enter>
    Enter coordinate one (x,y): 

Typing 's' and hitting enter opens the slope command. The
slope command returns the slope between two points on a line.
Notice that once the command is opened, a prompt is displayed
that says to enter the first set of coordinates in (x,y) format.

    >>>s<enter>
    Enter coordinate one (x,y): (3,4)<enter>
    Enter coordinate two (x,y): (5,6)<enter>
    1

After entering both points, the answer is returned. In this case
the slope is 1. Once a command has been finished the '>>>'
prompt returns, and you can use the same command or a new one.

----------------------------------------------------------------

## Section 4 | Using the manuals

The user manuals are a very important resource. They are short,
(much shorter than this I promise) easy to understand references
for using the various commands in this application. To open the
main manual, type 'man', and a text file will pop up with a list
of all the commands. Type 'q' to exit the manual and return to
the program. 

If you need help with a specific command, type 'man xcmd' where
'xcmd' is replaced by the name of the command you need help with.
There are specific manuals for every command in this application,
so if you're not sure how to use a command or you keep getting
an error message, check out the manual on the command to help
you out.

---------------------------------------------------------------

## Section 5 | Developers

[This section is for developers, you can stop reading if you
just want to use this application and not contribute to the
project.]

### 5.1 | Introduction to file structure

The filesystem of this application is very simple:

    /algebrasolver
        README
        algebra.py
        /config
        /extras
        /manuals

algebra.py is the main app script. It contains the interface
and program startup. Read the docstrings in-script to learn
more about the specifics. 

/config contains the main calculation module, alg.py. If you
want to add more functionality, edit alg.py. Read the doc-
strings to get more info on the manual. /config Also contains
the JSON file userinfo.json, which is updated via userinfo.py
(also located in /config). The userinfo JSON file stores the
user's name and command history. The userinfo Python script edits
the file if the user wants to change their name, or clear the
command history.

/manuals is a directory of all the user manual text files. The
name of the manual must match the name of the command (with the
addition of .txt extension), because the manuals are accessed
via the command name. See method OpenFile in the InputHandler
class in algebra.py for more info.

### 5.2 | Adding a new calculation function

Let's say you want to add a new calculation function to the
program. For the sake of simplicity, the function you want to add
prints the sum of two input values, x and y.

>> Write the function in /config/alg.py:

    def sumxy(x, y):
        """Include a docstring explaining function if necessary"""
        print x + y
        return x + y

>> Add the input handling method in the InputHandler class in
/algebra.py:

    class InputHandler():
        # other methods

        # your method
        def HandleSum(self):
            # handle input
            # call to alg.sumxy(x, y)

>> If the method has options and therefore requires a flag, add
the line

>> `if not self.ValidateFlag('command', flag): return False`

>> To validate the flag, where `'command'` is the name of the
command. Be sure to add a valid flags list to the ValidateFlag
method.

    class InputHandler():
        # other methods

        # your method
        def HandleSum(self, flag=False):
            # validate flag
            if not self.ValidateFlag('command', flag): return False
            # handle input
            # call to alg.sumxy(x, y)
    
Finally, add a user manual with the same name as the command with
a .txt extension and put it in the /manuals directory.

### 5.3 | Formatting

Algebra Solver conforms relatively strictly to [Python PEP8][1]
standards, with the exception of personal preference. The main
styles to adhere to are listed below:

* Multiple word variables and functions are separated with an
underscore (_), not camelCase
* All lines must be less than or equal to 80 characters long
(PEP8 specifies 79, but 80 makes more sense)
* Each word in a method name begins in a capital letter as in
`MethodName(self, args)`
* Docstrings and comments are used liberally
* **All intents must be 4 SPACES, not a tab width of 4**
* All lines of README and user manual files must be less than 50
characters in width

--------------------------------------------------------------

Thank you for using Algebra Solver!
Questions? Check out my contact info on samrapdev.com
Report a bug to: rapaport.sam7@gmail.com

Current version: 1.0


  [1]: http://legacy.python.org/dev/peps/pep-0008/