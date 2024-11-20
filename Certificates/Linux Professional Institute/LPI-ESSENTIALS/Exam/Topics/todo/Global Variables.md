Working with Global Variables

To make a variable available to subprocesses, turn it from a local into an environment variable. This is done by the command export. When it is invoked with the variable name, this variable is added to the shell’s environment:

Linux Essentials (Version 1.6) | 2.1 Command Line Basics

Version: 2024-04-29 | Licensed under CC BY-NC-ND 4.0. | learning.lpi.org | 87

$ greeting=hello $ export greeting

NOTE

Again, make sure to not use $ when running export as you want to pass the name of the variable instead of its contents.

An easier way to create the environment variable is to combine both of the above methods, by assigning the variable value in the argument part of the command.

$ export greeting=hey

Let’s check again if the variable is accessible to subprocesses:

$ export greeting=hey

$ echo $greeting world hey world

$ bash -c 'echo $greeting world' hey world

Another way to use environment variables is to use them in front of commands. We can test this with the environment variable TZ which holds the timezone. This variable is used by the command date to determine which timezone’s time to display:

$ TZ=EST date

Thu 31 Jan 10:07:35 EST 2019 $ TZ=GMT date

Thu 31 Jan 15:07:35 GMT 2019

You can display all environment variables using the env command.