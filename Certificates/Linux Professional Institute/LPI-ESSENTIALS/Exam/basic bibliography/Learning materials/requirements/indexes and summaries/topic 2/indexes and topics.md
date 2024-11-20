70-168

Concepts of the Linux shell
	• What is the Bash shell
	• The structure of the command line
	• An introduction to quoting
Types of variables
	• How to create variables
	• How to manipulate variables
- Man pages
- Info pages
[[How to get help]]
	• How to use the man command
	• How to navigate the man page
	• Different sections of the man page
	• How to use the info command
	• How to navigate between different nodes
• How to search for files within the system
Files, directories
	• Hidden files and directories
	• Home directories
	• Absolute and relative paths
The fundamentals of the Linux filesystem
• The difference between parent directories and subdirectories
• The difference between absolute file paths and relative file paths
• The special relative paths . and ..
• Navigate the filesystem using cd
• Show your current location using pwd
• List all files and directories using ls -a
that each Linux user will have a home directory,
• the current user’s home directory can be reached by using ~,
• any file path that uses ~ is called a relative-to-home path
Files and directories
• Case sensitivity
• Simple globbing

The Linux command line environment provides tools to manage files. Some commonly used ones are cp, mv, mkdir, rm, and rmdir. These tools, combined with globs, allow users to get a lot of work done very quickly.
Many commands have a -i option, which prompts you before doing anything. Prompting can save you a lot of hassle if you mistyped something.
A lot of commands have a -r option. The -r option usually means recursion. In mathematics and computer science, a recursive function is a function using itself in its definition. 
When it comes to command line tools, it usually means apply the command to a directory and everything in it.

--------

bash
The most popular shell on Linux computers.
echo
Output text on the terminal.
ls
List the contents of a directory.
type
Show how a specific command is executed.
touch
Create an empty file or update an existing file’s modification date.
hostname
Show or change a system’s hostname.
env
Display the current environment.
echo
Output text.
export
Make local variables available to subprocesses.
unset
Remove a variable.
man
• info
• /usr/share/doc/
• locate
man
Display a man page.
info
Display an info page.
locate
Search the locate database for files with a specific name.
find
Search the file system for names matching a set of selection criteria.
updatedb
Update the locate database
Common options for ls
• Recursive listings
• cd
• . and ..
• home and ~
cd
Change the current directory.
pwd
Print the current working directory’s path
ls
List the contents of a directory and display properties of files
mkdir
Create a new directory
tree
Display a hierarchical listing of a directory tree
You also learned about some of the most common ways of modifying the `ls command.
-a (all)
prints all files/directories, including hidden
-d (directories)
list directories, not their contents
-h (human readable)
prints file sizes in human readable format
-l (long list)
provides extra details, one file/directory per line
-r (reverse)
reverses the order of a sort
-R (recursive)
lists every file, including files in each subdirectory
-S (size)
sorts by file size
-t (time)
sorts by modification time
-X (eXtension)
sorts by file extension
mv, cp, rm, touch
• mkdir, rmdir
cat
Read and output the contents of a file.
cp
Copy files or directories.
echo
Output a string.
find
Traverse a file system tree and search for files matching a specific set of criteria.
ls
Show properties of files and directories and list a directory’s contents.
mkdir
Create new directories.
mv
Move or rename files or directories.
pwd
Output the current working directory.
rm
Delete files or directories.
rmdir
Delete directories.
touch
Create new empty files or update an existing file’s modification timestamp.