![[How to get help]]
- [x] Program usage (man, info)
	- [ ] Page 97
	- [ ] Page 98
	- [ ] Page 99
	- [ ] Page 100
	- [ ] Page 101
- [x] How to search for files on the File System
	- [ ] Page 101
	- [ ] Page 102
	- [ ] Page 103
- [x] [[Searching within Files with grep]]
	- [ ] Page 200
	- [ ] Page 201
- [x] Regular expressions (meta-characters usage)
	- [ ] Page 201
	- [ ] Page 202
	- [ ] Page 203
	- [ ] Page 204
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
- [x] Managing Processes and Logs
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

- Man pages
- Info pages
[[How to get help]]
	• How to use the man command
	• How to navigate the man page
	• Different sections of the man page
	• How to use the info command
	• How to navigate between different nodes
	• How to search for files within the system

Regular expressions meta-characters
	• How to create patterns with regular expressions
	• How to search within the files

• How to use grep, regular expressions and exit codes to check user input in scripts.

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