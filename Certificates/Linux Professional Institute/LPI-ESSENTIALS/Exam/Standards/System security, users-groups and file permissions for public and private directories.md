- [x] system security
	- [x] Server Programs
		- [ ] Page 23
		- [ ] Page 24
	- [x] Data Sharing
		- [ ] Page 24
		- [ ] Page 25
	- [x] Network Administration
		- [ ] Page 25
		- [ ] Page 26
	- [x] Privacy on the internet
		- [ ] introduction - Page 57
			- [ ] Cookie Tracking
				- [ ] Page 57
				- [ ] Page 58
			- [ ] Do Not Track (DNT)
				- [ ] Page 58
			- [ ] what incognito doesn't and what it does
				- [ ] Page 58
				- [ ] Page 59
			- [ ] Creating good password
				- [ ] Page 59
				- [ ] Page 60
			- [ ] Encryption basics
				- [ ] Page 60
				- [ ] Page 61
				- [ ] Page 62
	- [x] Managing Processes and Logs
		- [ ] view and manage processes
			- [ ] Page 303
			- [ ] Page 304
			- [ ] Page 305
			- [ ] Page 306
			- [ ] Page 307
		- [ ] System Load
			- [ ] Page 307
		- [ ] Seeing logs and rotating it
			- [ ] Page 308
			- [ ] Page 309
			- [ ] Page 310
			- [ ] Page 311
			- [ ] Page 312
	- [x] DNS (Domain Name System)
		- [ ] Page 336
		- [ ] Page 337
		- [ ] Page 338
		- [ ] Page 339
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
	- [x] Temporary Files and permissions of them
		- [ ] Page 416
		- [ ] Page 417
		- [ ] Page 418
- [x] users/groups
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
	- [x] Access Control
		- [ ] Page 348
			- [ ] Accounts basics
				- [ ] Getting Information About Your Users
					- [ ] Page 352
					- [ ] Page 353
				- [ ] Identifiers (UIDs/GIDs)
					- [ ] Page 349
				- [ ] The Superuser Account
					- [ ] Page 349
				- [ ] Standard User Accounts
					- [ ] Page 349
					- [ ] Page 350
				- [ ] System Accounts
					- [ ] Page 350
				- [ ] Service Accounts
					- [ ] Page 350
					- [ ] Page 351
				- [ ] Login Shells and Home Directories
					- [ ] Page 351
					- [ ] Page 352
			- [ ] Switching users and Escalating Privileges
				- [ ] Page 354
				- [ ] Page 355
			- [ ] Access Control Files
				- [ ] Page 355
				- [ ] Page 356
				- [ ] Page 357
				- [ ] Page 358
				- [ ] Page 359
				- [ ] Page 360
				- [ ] Page 361
- [x] file permissions for public and private directories
	- [x] Execute permissions and path for execution
		- [ ] Page 214
		- [ ] Page 215
		- [ ] Page 216
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


- Server applications
	- Nextcloud
	- ownCloud
	- Apache HTTPD
	- NGINX
	- MariaDB
	- MySQL
	- NFS
	- Samba

- [ ] Privacy on the internet
	- [ ] introduction - Page 57
	The browser is an essential piece of software in computing nowadays, but it’s necessary to understand some things to use it with safety. 
	- DNT is just a way to tell the website that you do not want to be tracked, but there is no guarantee on that. 
	- Private windows are private only to the computer you’re using but this can allow you to escape from cookie tracking exactly because of that. 
	- [[TLS]] is able to encrypt your communication on the Internet, but you have to be able to recognize when it’s in use. 
	- Using strong passwords is also very important to keep you safe, so the best idea is to delegate that responsibility to a password manager and allow the software to create random passwords to every site you log into. 
	- Another way to secure your communication is to sign and encrypt your files folders and emails with [[GnuPG]]. 

[[dm-crypt]] and [[EncFS]] are two alternatives to encrypt whole disks or partitions that use respectively block and stack encryption methods. 

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

-----------------------
UI versus command line, desktop configuration

#distros
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

-----------------------

• The application layer where applications connect to each other.
We have seen how IPv4 and IPv6 are used to address individual computers, and how TCP and UDP
enumerate sockets used by applications to connect to each other. We also learned how DNS is used to resolve names to IP addresses.
Commands used in the exercises:
dig
Query DNS information and provide verbose information about the DNS queries and
responses.
host
Query DNS information and provide condensed output.
ip
Configure networking on Linux, including network interfaces, addresses and routing.
ping
Test the connectivity to a remote device.
ss
Show information regarding sockets.

--------------


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

id
List real (or effective) user and group IDs.
last
List users who logged in last.
who
List users who are currently logged in.
w
Similar to who but with additional context.
su
Switch to another user with a login shell, or run commands as that user, by passing that user’s
password.
sudo
Switch User (or Superuser) Do, if entitled, the current user enters their own password (if
required) to raise privilege.
chsh
Change a user’s shell.
chfn
Change the user’s information on the GECOS field.

• /etc/passwd, /etc/shadow, /etc/group, /etc/skel/
• useradd, groupadd
• passwd

useradd
Create a new user account.
groupadd
Create a new group account.
userdel
Delete a user account.
groupdel
Delete a group account.
passwd
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

• ln -s
• ln

ls
• ls -d
• The -i parameter to ls
• ls -l, ls -a

chmod
Changes permissions of a file.
• How to create and execute simple scripts
env
Prints all environment variables to standard output.
which
Prints the absolute path of a command.