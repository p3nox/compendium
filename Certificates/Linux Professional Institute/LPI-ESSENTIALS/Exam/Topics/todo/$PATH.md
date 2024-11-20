The PATH Variable

The PATH variable is one of the most important environment variables in a Linux system. It stores a list of directories, separated by a colon, that contain executable programs eligible as commands from the Linux shell.

$ echo $PATH /home/user/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games

Linux Essentials (Version 1.6) | Topic 2: Finding Your Way on a Linux System

88 | learning.lpi.org | Licensed under CC BY-NC-ND 4.0. | Version: 2024-04-29

To append a new directory to the variable, you will need to use the colon sign (:).

$ PATH=$PATH:new_directory

Here an example:

$ echo $PATH

/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin $ PATH=$PATH:/home/user/bin

$ echo $PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/user/bin

As you see, $PATH is used in the new value assigned to PATH. This variable is resolved during the command execution and makes sure that the original content of the variable is preserved. Of course, you can use other variables in the assignment as well:

$ mybin=/opt/bin

$ PATH=$PATH:$mybin

$ echo $PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/home/user/bin:/opt/bin

The PATH variable needs to be handled with caution, as it is crucial for working on the command line. Let’s consider the following PATH variable:

$ echo $PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

To find out how the shell invokes a specific command, which can be run with the command’s name as argument. We can, for example, try to find out where nano is stored:

$ which nano /usr/bin/nano

As it can be seen, the nano executable is located within the /usr/bin directory. Let’s remove the directory from the variable and check to see if the command still works:

$ PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/sbin:/bin:/usr/games $ echo $PATH

Linux Essentials (Version 1.6) | 2.1 Command Line Basics

Version: 2024-04-29 | Licensed under CC BY-NC-ND 4.0. | learning.lpi.org | 89

/usr/local/sbin:/usr/local/bin:/usr/sbin:/sbin:/bin:/usr/games

Let’s look up the nano command again:

$ which nano

which: no nano in (/usr/local/sbin:/usr/local/bin:/usr/sbin:/sbin:/bin:/usr/games)

As it can be seen, the command is not found, therefore not executed. The error message also explains the reason why the command was not found and in what locations it was searched.

Let’s add back the directories and try running the command again.

$ PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin $ which nano

/usr/bin/nano

Now our command works again.

TIP

The order of elements in PATH also defines the lookup order. The first matching executable found while going through the paths is executed.