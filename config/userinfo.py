import sys
import json

"""User database module

This module handles read and write functions to the very simple user database
JSON file. The JSON database consists of a username that is printed to the user
during each login, as well as a history of commands that can be printed using
the command 'history'.
"""

class User(object):

    def __init__(self, datafile):
        """Create a new instance of the User object

        The User class contains all of the methods for reading and writing to
        the database. The variable self.datafile is the path to the JSON file.
        self.userdata is a python encoded JSON object of the entire datafile.
        The ReadFile method is immediately called to store the initial values of
        the datafile. The self.rewritten insance variable tracks whether or not
        the datafile has been written to. This is useful because it helps
        reduce the amount of times we open the file for reading, since there is
        no use in re-reading the file if it hasn't been changed since the last
        time we stored the data.
        """
        self.datafile = datafile
        self.userdata = ""
        self.ReadFile(self.datafile)
        self.rewritten = False

    def ReadFile(self, filename):
        with open(filename, 'r') as userinfo:
            self.userdata = json.loads(userinfo.read())
        self.rewritten = False

    def WriteFile(self, filename):
        with open(filename, 'w') as userinfo:
            userinfo.write(json.dumps(self.userdata, sort_keys=True, 
                                                     indent=4,
                                                     separators=(',', ': ')))
        self.rewritten = True

    def PrintHistory(self):
        # Only read the file if it has been re-written
        if self.rewritten:
            self.ReadFile(self.datafile)
    
        history = self.userdata['command_history']

        sys.stdout.write("Command history: ")
        for command in history:
            sys.stdout.write(command + ", ")
        print ''

    def ClearHistory(self):
        # Only read the file if it has been re-written
        if self.rewritten:
            self.ReadFile(self.datafile)

        self.userdata['command_history'] = []
        self.WriteFile(self.datafile)

    def UpdateHistory(self, cmd, flag=""):
        # Only read the file if it has been re-written
        if self.rewritten:
            self.ReadFile(self.datafile)

        # Save the original history items
        history = self.userdata['command_history']
        # Create an updated list which initially contains the newest command
        if flag:
            updated = ["{} -{}".format(cmd, flag)]
        else:
            updated = [cmd]
        # Append all other commands to the updated list
        for command in history:
            updated.append(command)
        self.userdata['command_history'] = updated
        self.WriteFile(self.datafile)

    def CreateUsername(self):
        username = raw_input("Create a username, or type '!' to skip: ")
        if username == '!': return False

        # Only read the file if it has been re-written
        if self.rewritten:
            self.ReadFile(self.datafile)

        self.userdata['username'] = username
        self.WriteFile(self.datafile)
        print "Username changed to %s ! Change it anytime by typing" +\
                "'reset username'." % (username)

    def Login(self):
        if self.rewritten:
            self.ReadFile(self.datafile)

        # If a username has not yet been created
        if not self.userdata['username']:
            self.CreateUsername()
        else:
            print "Welcome, %s!" % (self.userdata['username'])

    def Reset(self, reset_item):
        if reset_item == 'hist' or reset_item == 'history':
            self.ClearHistory()
            print "Command history cleared"
        elif reset_item == 'user' or reset_item == 'username':
            self.CreateUsername()
        else:
            print "Invalid argument to 'reset': reset %s" % reset_item
            print "    Valid arguments are 'history' and 'username'"
            return False
