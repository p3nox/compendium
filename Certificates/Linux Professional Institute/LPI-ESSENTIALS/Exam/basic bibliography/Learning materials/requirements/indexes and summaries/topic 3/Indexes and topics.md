168-250
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


tar
Create, update, list and extract tar archives.

unzip
Decompress and extract content from a ZIP file.
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