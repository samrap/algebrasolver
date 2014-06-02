import os
import sys
import ast
import json
import itertools
import subprocess

sys.path.append('./config')
sys.path.append('./extras')
import alg
import userinfo
import games

"""Interface/main app module

This module contains the command line interface of the program.
It handles prompts, takes input regarding that prompt, and sends
that input to the alg.py module for processing, printing of the
output.
"""

# Day and night
# The lonely global seems to free his mind at night
# He's all alone, some things will never change
# The lonely global seems to free his mind at night (at, at, at night)
user = userinfo.User('./config/userinfo.json')

class InputHandler(object):
    """Input handler class does just that - handle input

    The only method that should be called outside of this class is
    the MainLoop method. It controls the entire program, creating an
    infinite loop of input prompts until the user specifies the quitting
    of the program. MainLoop does two simple things: Print a prompt and
    respond to the input.

    Each command has its own method handler that will take the necessary
    arguments as input, process them for validity, and send them to the
    alg.py module for calculation. Once calculated, the MainLoop loop is
    continued.
    """

    def __init__(self):
        self.cmdErr = "'%s' is an invalid command. Type 'man' for more info."
        self.flagErr = "A valid flag is required for the '%s' command." +\
                        " Type 'man %s' for more info."
        # Avoid a jungle of if/elifs with a dictionary of command keys referring
        # to each command's method handler.
        self.commands = {
            'q': self.HandleQuadratic,
            's': self.HandleSlope,
            'dv': self.HandleDirectVar,
            'sq': self.HandleSequence,
            'sr': self.HandleSeries,
            'man': self.OpenFile,
            'root': self.HandleRoot,
            'clear': self.ClearScreen,
            'numtype': self.HandleNumtype,
            'hangman': games.hang,
            'tictactoe': games.tictactoe,
            'history': user.PrintHistory
        }

    def HandleNumtype(self):
        n = ast.literal_eval(raw_input("Enter a number: "))
        # Since values are checked in the alg module, there is no need for
        # error checking here
        alg.numtype(n)

    def HandleDirectVar(self):
        """Direct variation checking method.

        Take input in the form of two data sets, an x column, and a y
        column. Make sure the values were entered correctly and then process
        in alg
        """

        try:
            x = tuple(ast.literal_eval(raw_input("Enter 'x' values (1,2,3): ")))
            y = tuple(ast.literal_eval(raw_input("Enter 'y' values (4,5,6): ")))
            print x
            # Raise error if any values are not numeric
            test = [int(float(n)) for n in itertools.chain(x, y)]
            alg.direct_variation(x, y)
        except:
            print "An input error occurred. Type 'man dv' for more info."
            return False

    def HandleSlope(self):
        """Slope calculation method.

        Take input for the x,y coordinates, make sure each input has two
        values, and then return the slope of the points.
        """

        try:
            set_one = ast.literal_eval(raw_input("Enter coordinate one (x,y): "))
            set_two = ast.literal_eval(raw_input("Enter coordinate two (x,y): "))
            # make sure input has two values
            test_one, test_two = set_one[0:2], set_two[0:2]
            alg.find_slope(set_one, set_two)
        except:
            print "Coordinates were entered incorrectly." +\
                  " Type 'man slope' for more info."
            return False

    def HandleSequence(self, flag=False):
        """Sequence checking method.

        Insure the given sequence input is iterable, and that it contains
        only numerical values. Set the nthterm variable if 'n' was specified in
        the flag, then create a functions dictionary and make a call to the
        proper flag-function. A flag is required for this method.
        """

        # Check for any invalid flags
        if not self.ValidateFlag('sq', flag): return False
        try:
            sequence = tuple(ast.literal_eval(
                                raw_input("Enter the sequence (1,2,3): ")
            ))
            # Raise error if any values are not numeric
            test = [int(float(n)) for n in sequence]
            if 'n' in flag:
                nthterm = int(raw_input("Enter the desired ntherm: "))
            else:
                nthterm = False
        except:
            print "An input error occurred. Type 'man sq' for more info."
            return False

        functions = {
            'a': alg.check_arithmetic_sequence,
            'an': alg.check_arithmetic_sequence,
            'g': alg.check_geometric_sequence,
            'gn': alg.check_geometric_sequence
        }
        functions[flag](sequence, nthterm)

    def HandleSeries(self, flag=False):
        """Series calculation method.

        A flag is required for this method. Similar in concept to HandleSequence,
        HandleSeries has a few differences.

        Unlike checking for a sequence, getting the series of a sequence
        requires different variables which depend on whether the sequence is
        arithmetic or geometric. If the character 'a' is in flag, the user has
        specified an arithmetic sequence, so the variables for those are prompted
        and set if the input is valid. If the character 'g' is in flag or, in
        other words 'a' is not in flag, the user has specified a geometric
        series, so the variables for those are prompted and set if the input is
        valid. Finally, the proper function calls to alg are made.
        """

        # Check for any invalid flags
        if not self.ValidateFlag('sr', flag): return False
        if 'a' in flag:
            try:
                fterm = alg.atod(
                            raw_input("Enter the first term of the series: ")
                )
                if fterm is False: raise ValueError
                nterm = alg.atod(
                            raw_input("Enter the nth term of the series: ")
                )
                if nterm is False: raise ValueError
                n = int(raw_input("Enter n, the number of terms: "))

                alg.arithmetic_series(fterm, nterm, n)
            except:
                print "An input error occured. Type 'man sr' for more info."
                return False
        else:
            try:
                fterm = alg.atod(raw_input("Enter the first term of the series: "))
                if fterm is False: raise ValueError
                nterm = alg.atod(raw_input("Enter the nth term of the series : "))
                if nterm is False: raise ValueError
                ratio = alg.atod(raw_input("Enter the common ratio: "))
                if ratio is False: raise ValueError

                alg.geometric_series(fterm, nterm, ratio)
            except:
                print "An input error occured. Type 'man sr' for more info."
                return False

    def HandleQuadratic(self, flag=False):
        """Quadratic calculation method.

        A flag is required for this method. If no flag is specified or the flag
        is invalid, an error message is printed in the ValidateFlag method. If
        the flag is valid the a,b,c values are taken and the quadratic class is
        initialized. The functions dictionary makes it easy to call the proper
        quadratic calculation method.
        """

        # Check for any invalid flags
        if not self.ValidateFlag('q', flag): return False
        try:
            a = int(float(raw_input("Enter the 'a' value of the quadratic: ")))
            b = int(float(raw_input("Enter the 'b' value of the quadratic: ")))
            c = int(float(raw_input("Enter the 'c' value of the quadratic: ")))
        except ValueError:
                print "You must enter a number. Type 'man q' for more info."
                return False

        quadratic = alg.Quadratic(a, b, c)
        functions = {
            'f': quadratic.FactorizeQuadratic,
            'd': quadratic.Discriminant,
            'v': quadratic.FindVertex,
            'vfm': quadratic.VertexForm
        }
        functions[flag]()

    def HandleRoot(self, flag=False):

        try:
            rad = float(raw_input("Enter the radical: "))
        except:
            print "You must enter a numerical radical." +\
                  "Type 'man root' for more info."
            return False

        try:
            root = int(raw_input("Enter the root: "))
        except:
            print "You must enter a numerical root." +\
                  " Type 'man root' for more info."
            return False

        radical = alg.Radical(rad, root)
        radical.FindRoot()

    def ValidateFlag(self, cmd, flag):
        """Validate the flag of a given command. Valid flags vary based on the
        given command, so each command has its own valid list. If the flag is
        equal to any of the flags in the valid list, this method exits True.
        If the flag is invalid, an error message is printed and the method
        exits False.
        """

        valid = []
        if cmd == 'q':
            valid = ['f','d','v','vfm']
        elif cmd == 'sq':
            valid = ['a','an','g','gn']
        elif cmd == 'sr':
            valid = ['a','g']

        if any([flag == f for f in valid]): return True

        # Flag-Error message gets printed if flag is invalid
        print self.flagErr % (cmd, cmd)
        return False

    def OpenFile(self, helpfile):
        """Open the help file relevant to the user's input. If the input is
        simply 'man', the full manual is printed, otherwise the following
        characters correspond to the name of the help file, so they are used
        to squeeze many conditionals to one conditional.
        """

        if helpfile == '':
            subprocess.call(['less', './manuals/man.txt'])
        else:
            manfile = './manuals/%s.txt' % helpfile
            manual = subprocess.Popen(
                                ['less', manfile],
                                stderr=subprocess.PIPE
            )
            error = manual.communicate()
            # If there is an error in opening the file, print an error message
            if len(error[1]) > 0:
                print "No manual is available for %s." % helpfile
                return False
        return True

    def ClearScreen(numlines=100):
        """Clear the screen of all output.
        numlines is an optional fallback parameter.
        Credit to Jon Cage on SO for answering someone's
        question about this.
        """

        # Unix, OSX, Linux
        if os.name == 'posix':
            os.system('clear')

        # DOS/Windows
        elif os.name in ('nt', 'dos', 'ce'):
            os.system('CLS')

        # Fallback
        else:
            print '\n' * numlines

    def MainLoop(self):
        """Initiate the main loop in the program.

        This is the only method that should be called outside of the
        InputHandler class. It takes user input and calls the commands.
        If the command doesn't exist, an error message is printed and the
        loop continues back to the main prompt.
        """

        while True:
            usrin = raw_input(">>> ").replace(' ', '')

            # Handler for special commands
            if usrin == 'quit':
                print "Goodbye"
                quit()
            if usrin[0:3] == 'man':
                self.OpenFile(usrin[3:])
                continue
            if usrin[0:5] == 'reset':
                # Pass the argument to the Reset method
                user.Reset(usrin[5:])
                continue

            # Handler for 'normal' commands
            if '-' in usrin:
                cmd, flag = usrin.split('-')
                try:
                    self.commands[cmd](flag)
                    user.UpdateHistory(cmd, flag)
                except:
                    print self.cmdErr % usrin
            else:
                cmd = usrin
                try:
                    self.commands[cmd]()
                    user.UpdateHistory(cmd)
                except:
                    print self.cmdErr % usrin


if __name__=='__main__':
    interface = InputHandler()
    interface.ClearScreen()
    user.Login()
    print "Algebra Solver Version 1.0"
    print "Type 'man' for more info"
    interface.MainLoop()
