---
requires:
  - "[[Use a basic command line editor]]"
---

- [ ] [[Create and run simple shell scripts]]
	- [x] What defines a Script
		- [ ] Page 233
		- [ ] Page 234
	- [x] Exit Codes
		- [ ] Page 234
		- [ ] Page 235
		- [ ] Page 236
	- [x] Handling Many Arguments
		- [ ] Page 236
		- [ ] Page 237
	- [x] For Loops
		- [ ] Page 237
		- [ ] Page 238
		- [ ] Page 239
	- [x] Error Checking using Regular Expressions
		- [ ] Page 239
		- [ ] Page 240
		- [ ] Page 241
	- [x] Printing Output
		- [ ] Page 213
		- [ ] Page 214
	- [x] Execute permissions and path for execution
		- [ ] Page 214
		- [ ] Page 215
		- [ ] Page 216
	- [x] Common CLI Text Editors
		- [ ] Page 216
		- [ ] Page 217
	- [x] What are **variables** and how to use them(+$PATH)
		- [ ] Page 217
		- [ ] Page 218
		- [ ] Page 219
		- [ ] Page 220
		- [ ] Page 221
	- [x] Arguments and Scripts
		- [ ] Page 220
		- [ ] Page 221
		- [ ] Page 222
	- [x] Conditional Logic (Conditions)
		- [ ] Page 222
		- [ ] Page 223
	- [x] [[Searching within Files with grep]]
		- [ ] Page 200
		- [ ] Page 201
	- [x] Regular expressions (meta-characters usage)
		- [ ] Page 201
		- [ ] Page 202
		- [ ] Page 203
		- [ ] Page 204
	- [x] [[Input-Output of programs and Redirection]]
		- [ ] [[Definition of stdin and stdout]]
			- [ ] Page 187
			- [ ] [[INPUT-OUTPUT Redirection]]
				- [ ] Page 187
					- [ ] Redirecting Standard Output
						- [ ] Page 188
					- [ ] Redirecting Standard Error
						- [ ] Page 189
						- [ ] Page 190
					- [ ] Redirecting Standard Input
						- [ ] Page 190
					- [ ] Here Document (<<)
						- [ ] Page 190
						- [ ] Page 191
			- [ ] [[Combinations for I-O Redirection]]
				- [ ] Page 191
				- [ ] Page 192
		- [ ] [[Input Redirection]]
			- [ ] Page 192
			- [ ] Page 193
	- [x] Hidden files and Directories
		- [ ] Page 131
		- [ ] Page 132
	- [x] How to use ls Long List option (-l)
		- [ ] Page 132
		- [ ] Page 133
	- [x] Bash and Recursion
		- [ ] Page 133
		- [ ] Page 134
	- [x] [[Variables]]
		- [ ] What are variables (Local and ENVIRONMENT)
			- [ ] Page 85
			- [ ] Page 86
		- [ ] Managing Variables
			- [ ] Page 86
			- [ ] Page 87
			- [ ] Page 88
	- [ ] [[Copying Files and Directories]]
		- [ ] Page 151
		- [ ] Page 152
		- [ ] Page 153
	- [x] [[$PATH]]
		- [ ] Page 88
		- [ ] Page 89
		- [ ] Page 90
	- [ ] IMPORTANTE
		- [ ] [[terminal|command line]] ([[shell]])
			- [ ] Page 72
			- [ ] Page 73
		- [ ] [[Structure of a Command Line Query]]
			- [ ] Page 74
		- [ ] [[Internal and External commands]]
			- [ ] Page 75
		- [ ] [[Quoting]]
			- [ ] Page 75
			- [ ] Page 76
			- [ ] Page 77
		- [ ] [[Escape Characters]]
			- [ ] Page 77
			- [ ] Page 78
	- [ ] [[Programming Languages]]
		- [ ] Page 26
		- [ ] Page 27
		- [ ] Page 28


![[Basic shell scripting]]

	- [ ] [[moving inside directories and Absolute path to files]]
		- [ ] Page 114
		- [ ] Page 115
		- [ ] Page 116
		- [ ] Page 117
		- [ ] Page 118

Types of redirection
	• How to use the redirection operators
	• How to use pipes to filter command output
Regular expressions meta-characters
	• How to create patterns with regular expressions
	• How to search within the files

• I/O redirection
• Basic Regular Expressions using ., [ ], *, and ?
[[grep]]
• [[less]]
• [[cat]], [[head]], [[tail]]
• [[sort]]
• [[cut]]
• [[wc]]
[[cut]]
Removes sections from each line of a file.
[[cat]]
Displays or concatenates files.
[[find]]
Searches for files in a directory hierarchy.
[[less]]
Displays a file, allowing the user to scroll one line at the time.
[[more]]
Displays a file, a page at the time.
[[head]]
Displays the first 10 lines of a file.
[[tail]]
Displays the last 10 lines of a file.
[[sort]]
Sorts files.
[[wc]]
Counts by default the lines, words or bytes of a file.
Searches for characters or strings within a file
#! (shebang)
• /bin/bash
• Variables
• Arguments
• for loops
• echo
• Exit status
echo
Print a string to standard output.
env
Prints all environment variables to standard output.
which
Prints the absolute path of a command.
chmod
Changes permissions of a file.
Special variables used in the exercises:
$1, $2, … $9
Contain positional arguments passed to the script.
$#
Contains the number of arguments passed to the script.
$PATH
Contains the directories that have executables used by the system.

Operators used in the exercises:
-ne
Not equal to
-gt
Greater than
-ge
Greater than or equal to
-lt
Less than
-le
Less than or equal to
shift
This will remove the first element of an array.
Special Variables:
$?
Contains the exit code of the last command executed.
$@, $*
Contain all arguments passed to the script, as an array.


## [[$PATH]]

## [[Use a basic command line editor]]


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

## 	- [[Managing file hierarchy]]
		- [ ] [[Creating Directories]]
			- [ ] Page 144
			- [ ] Page 145
			- [ ] Page 146
		- [ ] [[Creating Files]]
			- [ ] Page 146
			- [ ] Page 147
		- [ ] [[Renaming Files]]
			- [ ] Page 147
			- [ ] Page 148
		- [ ] [[Moving Files]]
			- [ ] Page 148
			- [ ] Page 149
		- [ ] [[Deleting Files and Directories]]
			- [ ] Page 149
			- [ ] Page 150
			- [ ] Page 151
		- [ ] [[Copying Files and Directories]]
		- [ ] Page 151
		- [ ] Page 152
		- [ ] Page 153

[[mv]], [[cp]], [[rm]], [[touch]]
• [[mkdir]], [[rmdir]]
[[cat]]
Read and output the contents of a file.
[[cp]]
Copy files or directories.
[[echo]]
Output a string.
[[find]]
Traverse a file system tree and search for files matching a specific set of criteria.
[[ls]]
Show properties of files and directories and list a directory’s contents.
[[mkdir]]
Create new directories.
[[mv]]
Move or rename files or directories.
[[pwd]]
Output the current working directory.
[[rm]]
Delete files or directories.
rmdir
Delete directories.
touch
Create new empty files or update an existing file’s modification timestamp.

• [[How to search for files within the system]]
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

The [[terminal]] is a powerful way to interact with the system and there are lots of useful and very mature tools to use in this kind of environment. 
You can get to the terminal by looking for a graphical one at your desktop environment menu or pressing Ctrl + Alt + F# . 

- Another way to secure your communication is to sign and encrypt your files folders and emails with [[GnuPG]]. 
- [[TLS]] is able to encrypt your communication on the Internet, but you have to be able to recognize when it’s in use. 
- Using strong passwords is also very important to keep you safe, so the best idea is to delegate that responsibility to a password manager and allow the software to create random passwords to every site you log into. 
[[dm-crypt]] and [[EncFS]] are two alternatives to encrypt whole disks or partitions that use respectively block and stack encryption methods. 


- Development languages
	- C
	- Java
	- JavaScript
	- Perl
	- shell
	- Python
	- PHP
- Package management tools and repositories
	- dpkg
	- apt-get
	- rpm
	- yum

- Getting to the command line
	- Terminal and console
	- Password issues
	- Privacy issues and tools