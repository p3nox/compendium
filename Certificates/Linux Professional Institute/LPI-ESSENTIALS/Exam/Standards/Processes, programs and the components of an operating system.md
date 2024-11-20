- [x] processes
	- [x] Exit Codes
		- [ ] Page 234
		- [ ] Page 235
		- [ ] Page 236
	- [x] Error Checking using Regular Expressions
		- [ ] Page 239
		- [ ] Page 240
		- [ ] Page 241
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
	- [x] Sockets
		- [ ] Page 338
		- [ ] Page 339
- [x] programs
	- [x] packages (programs) and package management
		- [ ] Page 15
		- [ ] Page 16
		- [ ] Page 17
		- [ ] Page 18
		- [ ] Page 19
		- [ ] Page 20
	- [x] [[Structure of a Command Line Query]]
		- [ ] Page 74
	- [x] [[Internal and External commands]]
		- [ ] Page 75
	- [x] Execute permissions and path for execution
		- [ ] Page 214
		- [ ] Page 215
		- [ ] Page 216
	- [x] What are **variables** and how to use them(+$PATH)
		- [ ] Page 217
		- [ ] Page 218
		- [ ] Page 219
		- [ ] Page 220
		- [ ] Page 221
	- [x] Programs and their configuration files
		- [ ] Page 283
		- [ ] Page 284
		- [ ] Page 285
		- [ ] Page 286
		- [ ] Page 287
	- [x] [[Kernel and kernel modules]]
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
- [x] components of an Operating System
	- [x] [[Linux|what is linux]]
		- [ ] Page 2
		- [ ] Page 3
	- [x] [[Distros]]
		- [ ] Page 4
		- [ ] Page 5
	- [x] Android and Embedded Systems
		- [ ]  Page 5
		- [ ] Page 6
	- [x] Cloud
		- [ ] Page 7
	- [x] moving inside directories and Absolute path to files
		- [ ] Page 114
		- [ ] Page 115
		- [ ] Page 116
		- [ ] Page 117
		- [ ] Page 118
	- [x] Regular expressions (meta-characters usage)
		- [ ] Page 201
		- [ ] Page 202
		- [ ] Page 203
		- [ ] Page 204
	- [x] Execute permissions and path for execution
		- [ ] Page 214
		- [ ] Page 215
		- [ ] Page 216
	- [x] Widely used systems and how to choose from
		- [x] What Is as Operating System
			- [ ] Page 251
			- [ ] Page 252
		- [x] What is Linux
			- [ ] Page 252
		- [x] Types of Linux Distributions
			- [ ] Page 253
			- [ ] Page 254
			- [ ] Page 255
		- [x] Usages of Linux Distros
			- [ ] Support Lifecycle
				- [ ] Page 255
			- [ ] Linux Desktop
				- [ ] Page 255
			- [ ] Linux on Servers
				- [ ] Page 256
			- [ ] Linux and Cloud
				- [ ] Page 256
		- [x] Non Linux Operating Systems
			- [ ] Unix
				- [ ] Page 256
				- [ ] Page 257
			- [ ] MacOS
				- [ ] Page 257
			- [ ] Windows
				- [ ] Page 257
	- [x] Linux UI, [[Desktop Environments]]
		- [ ] Page 53
		- [ ] Page 54
	- [x] Programs and their configuration files
		- [ ] Page 283
		- [ ] Page 284
		- [ ] Page 285
		- [ ] Page 286
		- [ ] Page 287
	- [x] [[Kernel and kernel modules]]
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
	- [x] [[Drivers and Device Files]]
		- [ ] Page 274
		- [ ] Page 275


Types of variables
• How to create variables
• How to manipulate variables

Concepts of the Linux shell
	• What is the Bash shell
	• The structure of the command line
	• [[Internal and External commands]]

- What exit codes are, what they mean, and how to implement them
• How to check the exit code of a command

• How to use grep, regular expressions and exit codes to check user input in scripts.

• ps, top, free
• syslog, dmesg

In the context of data storage, the following topics have been discussed in this lesson: process
management and system logging and messaging.
Regarding process management, we have learned the following:
• Programs generate processes and processes exist in a hierarchy.
• Every process has a unique identifier (PID) and a parent process identifier (PPID).
• top is a very useful command to dynamically and interactively explore the running processes
of the system.
• ps can be used to obtain a snapshot of the current running processes in the system.

• The /proc directory includes directories for every running process in the system named after their PIDs.
• The concept of system load average — which is very useful to check on CPU
utilization/overloading.

## [[Sockets]]

ss
Show information regarding sockets.

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

- Distributions
	- End-user
		- Desbian Based
			- Debian (Testing and Sid)
			- Ubuntu (Non-LTS)
	- Enterprise use
		- Debian Based
			- Debian
			- Ubuntu(LTS)
		- Redhat Family
			- Oracle
			- CentOS
			- Fedora
			- Scientific Linux
		- SUSE Family
			- openSUSE Tumbleweed
			- openSUSE LEAP

Computing Systems

- Embedded Systems
	- Single-Board systems
	- Non-Single-Board Systems
- Single-Board Systems
	- Raspberry Pi
	- Mobile Phones
- Linux for Cloud
	- [[Virtualization Hosts]]
	- [[Linux and the Cloud]]
	- [[Open source business models]]

- Package management tools and repositories
	- dpkg
	- apt-get
	- rpm
	- yum

- What distributions does Linux have

- What are Linux embedded systems

- How are Linux embedded systems used

-  Different applicabilities of Android

Files, directories
	• Hidden files and directories
	• Home directories
	• Absolute and relative paths


Regular expressions meta-characters
	• How to create patterns with regular expressions
	• How to search within the files
	
• How to create and execute simple scripts

chmod
Changes permissions of a file.
	In this lesson you have learned how use ls to get information about file permissions, how to control or change who can create, delete or modify a file with [[chmod]], both in numeric and symbolic notation and how to change the ownership of files with [[chown]] and [[chgrp]].

• Maintenance cycles, beta and stable
In this section you have learned how to differentiate between different operating systems
commonly available. We discussed:
• Linux Based Operating Systems
• UNIX
• macOS
• Windows Based Operation Systems
Within the Linux category we could further break the selection down into distributions with long
term support and those with a shorter support cycle. LTS versions being more suited to the
Enterprise and shorter term support being targeted toward home and hobby users.
• Enterprise Grade Linux Distributions
◦ Red Hat Enterprise Linux
◦ CentOS
◦ SUSE Linux Enterprise Server
◦ Debian GNU/Linux
◦ Ubuntu LTS
• Consumer Grade Linux Distributions
◦ Fedora
◦ Ubuntu non-LTS
◦ openSUSE
• Experimental and Hacker Linux Distributions
◦ Arch
◦ Gentoo

Important facts about Linux and the Kernel:
	• For Linux, everything is a file.
	• The Linux kernel lives in /boot together with other boot-related files.
	• For processes to start executing, the kernel has to first be loaded into a protected area of memory.
	• The kernel job is that of allocating system resources to processes.
	• The /proc virtual (or pseudo) filesystem stores important kernel and system data in a volatile way.

• How to set and use variables inside scripts
• How to handle arguments in scripts
• Variables
• Arguments
env
Prints all environment variables to standard output.
which
Prints the absolute path of a command.
chmod
Changes permissions of a file.
$PATH
Contains the directories that have executables used by the system.

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

- Programs and configuration
	• Processes
	• Memory addresses
	• System messaging
	• Logging
Location of programs and their configuration files in a Linux system. Important facts to remember are:
	• Basically, programs are to be found across a three-level directory structure: /, /usr and /usr/local. Each of these levels may contain bin and sbin directories.
	• Configuration files are stored in /etc and ~.
	• Dotfiles are hidden files that start with a dot (.).

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

journalctl
Query the systemd journal.

• syslog, dmesg
• /etc/, /var/log/


Linux in the Cloud

Another opportunity to become familiar with Linux is to deploy Linux within one of the many public clouds available. Creating an account with one of the many others cloud providers will allow you to quickly deploy many different Linux distributions quickly and easily.