- [ ] Summary
	- [ ] 298 ~ 299
		- [x] Linux and the Filesystem
			- [ ] Page 283
			- [x] Programs and their configuration files
				- [ ] Page 283
				- [ ] Page 284
				- [ ] Page 285
				- [ ] Page 286
				- [ ] Page 287
			- [x] Kernel and kernel modules
				- [ ] Page 287
				- [ ] Page 288
				- [ ] Page 289
			- [x] /proc, info about hardware, running processes and the kernel
				- [ ] Page 289
			- [x] Hardware devices and Memory
				- [ ] Page 290
				- [ ] Page 291
				- [ ] Page 292
				- [ ] Page 293
				- [ ] Page 294
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
- [x] packages (programs) and package management
	- [ ] Page 15
	- [ ] Page 16
	- [ ] Page 17
	- [ ] Page 18
	- [ ] Page 19
	- [ ] Page 20
- [x] Server Programs
	- [ ] Page 23
	- [ ] Page 24
- [x] [[Data Sharing]]
	- [ ] Page 24
	- [ ] Page 25
- [x] Network Administration
	- [ ] Page 25
	- [ ] Page 26
- [x] Programming Languages
	- [ ] Page 26
	- [ ] Page 27
	- [ ] Page 28
- [x] Linux UI, [[Desktop Environments]]
	- [ ] Page 53
	- [ ] Page 54
- [x] [[Command Line basics]]
	- [ ] Page 54
- [x] FOSS software for presentation and LaTeX code
	- [ ] Page 55
- [x] Command line ([[shell]])
	- [ ] Page 72
	- [ ] Page 73
- [x] [[Structure of a Command Line Query]]
	- [ ] Page 74
- [x] [[Internal and External commands]]
	- [ ] Page 75
- [x] [[Quoting]]
	- [ ] Page 75
	- [ ] Page 76
	- [ ] Page 77
- [x] [[Escape Characters]]
	- [ ] Page 77
	- [ ] Page 78
- [x] Variables
	- [ ] What are variables (Local and ENVIRONMENT)
		- [ ] Page 85
		- [ ] Page 86
	- [ ] Managing Variables
		- [ ] Page 86
		- [ ] Page 87
		- [ ] Page 88
- [x] [[$PATH]]
	- [ ] Page 88
	- [ ] Page 89
	- [ ] Page 90
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
- [x] Drivers and Device Files
	- [ ] Page 274
	- [ ] Page 275
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
- [x] Special Permissions
	- [ ] Page 402
	- [ ] Page 403
	- [ ] Page 404
- [x] [[Globbing]] ***
	- [ ] Page 153
	- [ ] Page 154
	- [ ] Page 155
	- [ ] Page 156
	- [ ] Page 157
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
- [x] Searching within Files with grep
	- [ ] Page 200
	- [ ] Page 201
- [x] Regular expressions (meta-characters usage)
	- [ ] Page 201
	- [ ] Page 202
	- [ ] Page 203
	- [ ] Page 204
- [x] view and manage processes
	- [ ] Page 303
	- [ ] Page 304
	- [ ] Page 305
	- [ ] Page 306
	- [ ] Page 307
- [x] System Load
	- [ ] Page 307
- [x] Seeing logs and rotating it
	- [ ] Page 308
	- [ ] Page 309
	- [ ] Page 310
	- [ ] Page 311
	- [ ] Page 312
- [x] How users and group works
	- [ ] Page 372 ~ Page 373
		- [ ] /etc/passwd
			- [ ] Page 373
		- [ ] /etc/shadow
			- [ ] Page 374
			- [ ] Page 375
		- [ ] /etc/gshadow
			- [ ] Page 375
			- [ ] Page 376
		- [ ] Managing users (useradd)
			- [ ] Page 376
			- [ ] Page 377
			- [ ] Page 378 ([[id]] command)
		- [ ] /etc/skel
			- [ ] Page 378
		- [ ] group managing (groupadd groupdel)
			- [ ] Page 379
		- [ ] passwd
			- [ ] Page 379
			- [ ] Page 380

• Drivers

- Programs and configuration
	• Processes
	• Memory addresses
	• System messaging
	• Logging
Location of programs and their configuration files in a Linux system. Important facts to remember are:
	• Basically, programs are to be found across a three-level directory structure: /, /usr and /usr/local. Each of these levels may contain bin and sbin directories.
	• Configuration files are stored in /etc and ~.
	• Dotfiles are hidden files that start with a dot (.).
Important facts about Linux and the Kernel:
	• For Linux, everything is a file.
	• The Linux kernel lives in /boot together with other boot-related files.
	• For processes to start executing, the kernel has to first be loaded into a protected area of memory.
	• The kernel job is that of allocating system resources to processes.
	• The /proc virtual (or pseudo) filesystem stores important kernel and system data in a volatile way.

Likewise, we have explored hardware devices and learned the following:
	• The /dev directory stores special files (aka nodes) for all connected hardware devices: block
	devices or character devices. The former transfer data in blocks; the latter, one character at a
	time.
	• The /dev directory also contains other special files such as /dev/zero, /dev/null or
	/dev/urandom.
	• The /sys directory stores information about hardware devices arranged into categories.
	Finally, we touched upon memory. We learned:
	• A program runs when it is loaded into memory.
	• What RAM (Random Access Memory) is.
	• What Swap is.

• ps, top, free
• syslog, dmesg
• /etc/, /var/log/
• /boot/, /proc/, /dev/, /sys/
cat
Concatenate/print file content.
free
Display amount of free and used memory in the system.
ls
List directory contents.
which
Show location of program.
cat
Concatenate/print file content.
dmesg
Print the kernel ring buffer.
echo
Display a line of text or a newline.
file
Determine file type.
grep
Print lines matching a pattern.
last
Show a listing of last logged in users.
less
Display contents of file one page at a time.
ls
List directory contents.
journalctl
Query the systemd journal.
tail
Display the last lines of a file.

• Using temporary files and directories
• Symbolic links
Where temporary files are stored.
• What is the special permission applied to them.
• What links are.
	• The difference between symbolic and hard links.
	• How to create links.
	• How to move, rename or remove them.
• /tmp/, /var/tmp/ and Sticky Bit

• ln -s
• ln

ls
• ls -d
• The -i parameter to ls
• ls -l, ls -a


- Desktop applications
	- OpenOffice.org
	- LibreOffice
	- Thunderbird
	- [[Firefox]]
	- GIMP
- Server applications
	- Nextcloud
	- ownCloud
	- Apache HTTPD
	- NGINX
	- MariaDB
	- MySQL
	- NFS
	- Samba
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

Network Administration

	Communication between computers is only possible if the network is working correctly. Normally, the network configuration is done by a set of programs running on the router, responsible for setting up and checking the network availability. In order to achieve this, two basic network services are used: DHCP (Dynamic Host Configuration Protocol) and DNS (Domain Name System).
	
	DHCP is responsible for assigning an IP address to the host when a network cable is connected or when the device enters a wireless network. When connecting to the Internet, the ISP’s DHCP server will provide an IP address to the requesting device. A DHCP server is very useful in local area networks also, to automatically provide IP addresses to all connected devices. If DHCP is not configured or if it’s not working properly, it would be necessary to manually configure the IP address of each device connected to the network. It is not practical to manually set the IP addresses on large networks or even in small networks, that’s why most network routers come with a DHCP server pre-configured by default.
	
	The IP address is required to communicate with another device on an IP network, but domain names like www.lpi.org are much more likely to be remembered than an IP number like 203.0.113.165. The domain name by itself, however, is not enough to establish the
	
	Linux Essentials (Version 1.6) | 1.2 Major Open Source Applications
	
	Version: 2024-04-29 | Licensed under CC BY-NC-ND 4.0. | learning.lpi.org | 25
	
	communication through the network. That is why the domain name needs to be translated to an IP address by a DNS server. The IP address of the DNS server is provided by the ISP’s DHCP server and it’s used by all connected systems to translate domain names to IP addresses.
	
	Both DHCP and DNS settings can be modified by entering the web interface provided by the router. For instance, it is possible to restrict the IP assignment only to known devices or associate a fixed IP address to specific machines. It’s also possible to change the default DNS server provided by the ISP. Some third-party DNS servers, like the ones provided by Google or OpenDNS, can sometimes provide faster responses and extra features.


The [[terminal]] is a powerful way to interact with the system and there are lots of useful and very mature tools to use in this kind of environment. 
You can get to the terminal by looking for a graphical one at your desktop environment menu or pressing Ctrl + Alt + F# . 

```
But if you prefer code over graphical interfaces, there are a few tools for you to choose. Beamer is a LaTeX class that can create slide presentations from LaTeX code. LaTeX itself is a typesetting system largely used for writing scientific documents at the academy, specially for its capacity to handle complex math symbols, which other softwares have difficulty to deal with. If you are at the university and need to deal with equations and other math related problems, Beamer can save you a lot of time.
```

Concepts of the Linux shell
	• What is the Bash shell
	• The structure of the command line
	• An introduction to quoting

Types of variables
	• How to create variables
	• How to manipulate variables

[[Global Variables]]

env
Display the current environment.
echo
Output text.
export
Make local variables available to subprocesses.
unset
Remove a variable.

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

Types of redirection
	• How to use the redirection operators
	• How to use pipes to filter command output
Regular expressions meta-characters
	• How to create patterns with regular expressions
	• How to search within the files

• Drivers
Important facts about Linux and the Kernel:
	• For Linux, everything is a file.
	• The Linux kernel lives in /boot together with other boot-related files.
	• For processes to start executing, the kernel has to first be loaded into a protected area of memory.
	• The kernel job is that of allocating system resources to processes.
	• The /proc virtual (or pseudo) filesystem stores important kernel and system data in a volatile way.

Likewise, we have explored hardware devices and learned the following:
	• The /dev directory stores special files (aka nodes) for all connected hardware devices: block
	devices or character devices. The former transfer data in blocks; the latter, one character at a
	time.
	• The /dev directory also contains other special files such as /dev/zero, /dev/null or
	/dev/urandom.
	• The /sys directory stores information about hardware devices arranged into categories.
	Finally, we touched upon memory. We learned:
	• A program runs when it is loaded into memory.
	• What RAM (Random Access Memory) is.
	• What Swap is.

• /tmp/, /var/tmp/ and Sticky Bit

• ln -s
• ln

ls
• ls -d
• The -i parameter to ls
• ls -l, ls -a

Change the password of user accounts and control all aspects of password aging.

• chmod, chown

List files, optionally including details such as permissions.
chmod
Change the permissions of a file or directory.
chown
Change the owning user and/or group of a file or directory.
chgrp
Change the owning group of a file or directory.
• /tmp/, /var/tmp/ and Sticky Bit

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

---------------------
• /etc/passwd, /etc/shadow, /etc/group
• id, last, who, w
• sudo, su


- Programs and configuration
	• Processes
	• Memory addresses
	• System messaging
	• Logging
Location of programs and their configuration files in a Linux system. Important facts to remember are:
	• Basically, programs are to be found across a three-level directory structure: /, /usr and /usr/local. Each of these levels may contain bin and sbin directories.
	• Configuration files are stored in /etc and ~.
	• Dotfiles are hidden files that start with a dot (.).

In the context of data storage, the following topics have been discussed in this lesson: process
management and system logging and messaging.
Regarding process management, we have learned the following:
• Programs generate processes and processes exist in a hierarchy.
• Every process has a unique identifier (PID) and a parent process identifier (PPID).
• top is a very useful command to dynamically and interactively explore the running processes of the system.
• ps can be used to obtain a snapshot of the current running processes in the system.
• The /proc directory includes directories for every running process in the system named after their PIDs.
• The concept of system load average — which is very useful to check on CPU
utilization/overloading.


Concerning system logging, we must remember that:
	• A log is a file where system events are recorded. Logs are invaluable when it comes to troubleshooting.
	• Logging has traditionally been handled by special services such as syslog, syslog-ng or rsyslog.
	Nevertheless, some programs use their own logging daemons.
	• Because logs are variable data, they are kept in /var and — sometimes — their names can give you a clue about their content (kern.log, auth.log, etc.)
	• Most logs are written in plain text and can be read with any text editor as long as you have the right permissions. However, a few of them are binary and must be read using special commands.
	• To avoid problems with disk space, log rotation is carried out by the logrotate utility.
	• As for the kernel, it uses a circular data structure — the ring buffer — where boot messages are kept (old messages fade away over time).
	• The system and service manager [[systemd]] replaced [[System V init]] in virtually all distros with [[journald]] becoming the standard logging service.
	• To read systemd’s journal, the [[journalctl]] utility is needed.
	• How to display the use of memory.

Users/groups
	Root and standard users
	• System users
		In this lesson we have discovered the Linux user and group databases. We have learned the most important properties of users and groups, including their names and their numeric IDs. We have	also investigated how password hashing works on Linux and how users are assigned to groups.
All of this information is stored in the following four files, which provide the most basic, local security access controls on a Linux system:
-  /etc/passwd
	All system-local user account POSIX attributes, other than password hash, readable by all.
-	/etc/group
	All system-local group account POSIX attributes, readable by all.
- /etc/shadow
	All system-local user password hashes (and expiration information), unreadable by any (only select processes).
- /etc/sudoers
	All system-local privilege escalation information/allowance by the sudo command
	
• User and group commands
• User IDs
• The fundamentals of user and group management in Linux
• Manage user and group information stored in password and group databases
• Maintain the skeleton directory
• Add and remove user accounts
• Add and remove group accounts
• Change the password of user accounts