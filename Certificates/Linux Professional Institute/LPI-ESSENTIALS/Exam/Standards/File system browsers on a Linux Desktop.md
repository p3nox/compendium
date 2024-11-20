- [ ] [[File system browsers on a Linux Desktop]]
	- [x] How to search for files on the File System
		- [ ] Page 101
		- [ ] Page 102
		- [ ] Page 103
	- [x] moving inside directories and Absolute path to files
		- [ ] Page 114
		- [ ] Page 115
		- [ ] Page 116
		- [ ] Page 117
		- [ ] Page 118
	- [x] Linux and the Linux Terminal
		- [ ] Page 127
	- [x] Home and $Home
		- [ ] Page 127
		- [ ] Page 128
		- [ ] Page 129
		- [ ] Page 130
		- [ ] Page 131
	- [x] Hidden files and Directories
		- [ ] Page 131
		- [ ] Page 132
	- [x] How to use ls Long List option (-l)
		- [ ] Page 132
		- [ ] Page 133
	- [x] Bash and Recursion
		- [ ] Page 133
		- [ ] Page 134
	- [x] File and Directory definition
		- [ ] Page 143
	- [x] Case Sensivity
		- [ ] Page 144
	- [x] Creating Directories
		- [ ] Page 144
		- [ ] Page 145
		- [ ] Page 146
	- [x] Creating Files
		- [ ] Page 146
		- [ ] Page 147
	- [x] Renaming Files
		- [ ] Page 147
		- [ ] Page 148
	- [x] Moving Files
		- [ ] Page 148
		- [ ] Page 149
	- [x] Deleting Files and Directories
		- [ ] Page 149
		- [ ] Page 150
		- [ ] Page 151
	- [x] Copying Files and Directories
		- [ ] Page 151
		- [ ] Page 152
		- [ ] Page 153
	- [x] Globbing ***
		- [ ] Page 153
		- [ ] Page 154
		- [ ] Page 155
		- [ ] Page 156
		- [ ] Page 157
	- [x] how to read information and permissions of files and directories
		- [ ] Page 391
		- [ ] Page 392
		- [ ] Page 393
		- [ ] Page 394
		- [ ] Page 395
	- [x] Managing permissions to users and groups
		- [ ] Page 395
		- [ ] Page 396
		- [ ] Page 397
		- [ ] Page 398
		- [ ] Page 399
		- [ ] Page 400
		- [ ] Page 401
	- [x] Temporary Files and permissions of them
		- [ ] Page 416
		- [ ] Page 417
		- [ ] Page 418
	- [x] Understanding Soft and Hard links
		- [ ] Page 418
		- [ ] Page 419
		- [ ] Page 420
		- [ ] Page 421
		- [ ] Page 422

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

• How to search for files within the system
• locate
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
Linux Essentials (Version 1.6) | Topic 2: Finding Your Way on a Linux System
138 | learning.lpi.org | Licensed under CC BY-NC-ND 4.0. | Version: 2024-04-29
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
Linux Essentials (Version 1.6) | 2.4 Creating, Moving and Deleting Files
Version: 2024-04-29 | Licensed under CC BY-NC-ND 4.0. | learning.lpi.org | 161
rmdir
Delete directories.
touch
Create new empty files or update an existing file’s modification timestamp.

• User and group commands
 File and directory permissions and ownership
 As a multi-user system, Linux needs a way to track who owns and who can access each file. This is done through a three-level permissions system, and in this lesson we learned all about how this system works.
	In this lesson you have learned how use ls to get information about file permissions, how to control or change who can create, delete or modify a file with [[chmod]], both in numeric and symbolic notation and how to change the ownership of files with [[chown]] and [[chgrp]].
• Using temporary files and directories
• Symbolic links
Where temporary files are stored.
• What is the special permission applied to them.
• What links are.
	• The difference between symbolic and hard links.
	• How to create links.
	• How to move, rename or remove them.

• /etc/passwd, /etc/shadow, /etc/group
• id, last, who, w
• sudo, su

id
List real (or effective) user and group IDs.
su
Switch to another user with a login shell, or run commands as that user, by passing that user’s
password.
sudo
Switch User (or Superuser) Do, if entitled, the current user enters their own password (if
required) to raise privilege.

• chmod, chown

List files, optionally including details such as permissions.
chmod
Change the permissions of a file or directory.
chown
Change the owning user and/or group of a file or directory.
chgrp
Change the owning group of a file or directory.
• /tmp/, /var/tmp/ and Sticky Bit

• ln -s
• ln

ls
• ls -d
• The -i parameter to ls
• ls -l, ls -a