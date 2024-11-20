- [x] Copying Files and Directories
	- [ ] Page 151
	- [ ] Page 152
	- [ ] Page 153
- [x] [[Globbing]] ***
	- [ ] Page 153
	- [ ] Page 154
	- [ ] Page 155
	- [ ] Page 156
	- [ ] Page 157
- [x] Difference between Compression and Archiving tools
	- [ ] Page 170
	- [ ] Page 171
- [x] Compression Tools
	- [ ] Page 171
	- [ ] Page 172
	- [ ] Page 173
- [x] Archiving Tools
	- [ ] Page 174
	- [ ] Page 175
	- [ ] Page 176
	- [ ] Page 177
- [x] Managing Zip Files
	- [ ] Page 177
	- [ ] Page 178


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

Files, directories
• Archives, compression
Linux systems have several compression and archiving tools available. This lesson covered the most common ones. 
The most common archiving tool is tar. 
If interacting with Windows systemsis necessary, zip and unzip can create and extract ZIP files.
The tar command has a few options that are worth memorizing. 
They are x for extract, c for create, t for view contents, and u to add or replace files. The v option lists the files which are processed by tar while creating or extracting an archive.

The typical Linux distribution’s repository has many compression tools. The most common are:
- gzip
- bzip2
- and xz

Compression algorithms often support different levels that allow you to
optimize for speed or file size. 
Files can be decompressed with gunzip, bunzip2, and unxz.
Compression tools commonly have programs that behave like common text file tools, with the difference being they work on compressed files. A few of them are zcat, bzcat, and xzcat.
Compression tools typically ship with programs with the functionality of grep, more, less, diff, and cmp

Types of redirection
	• How to use the redirection operators
	• How to use pipes to filter command output
Regular expressions meta-characters
	• How to create patterns with regular expressions
	• How to search within the files
[[Basic shell scripting]]
	• Awareness of common text editors (vi and nano)
	• How to create and execute simple scripts
	• How to use a shebang to specify an interpreter
	• How to set and use variables inside scripts
	• How to handle arguments in scripts
	• How to construct if statements
	• How to compare numbers using numerical operators
	• What exit codes are, what they mean, and how to implement them
	• How to check the exit code of a command
	• What for loops are, and how to use them with arrays
	• How to use grep, regular expressions and exit codes to check user input in scripts.

-------------

tar
• Common tar options
• gzip, bzip2, xz
• zip, unzip
bunzip2
Decompress a bzip2 compressed file.
bzcat
Output the contents of a bzip compressed file.
bzip2
Compress files using the bzip2 algorithm and format.
gunzip
Decompress a gzip compressed file.
gzip
Compress files using the gzip algorithm and format.
tar
Create, update, list and extract tar archives.
unxz
Decompress a xz compressed file.
unzip
Decompress and extract content from a ZIP file.
xz Compress files using the xz algorithm and format.
zcat
Output the contents of a gzip compressed file.
zip
Create and compress ZIP archives.
ommand line pipes
• I/O redirection
• Basic Regular Expressions using ., [ ], *, and ?
grep
• less
• cat, head, tail
• sort
• cut
• wc
cut
Removes sections from each line of a file.
cat
Displays or concatenates files.
find
Searches for files in a directory hierarchy.
less
Displays a file, allowing the user to scroll one line at the time.
more
Displays a file, a page at the time.
head
Displays the first 10 lines of a file.
tail
Displays the last 10 lines of a file.
sort
Sorts files.
wc
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