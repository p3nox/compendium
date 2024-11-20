
250-346

#Hardware
A system is the sum of its components. Different components impact cost, performance, and usability in different ways. While there are common configurations for workstations and servers there is no single best configuration.
- Motherboards, processors, power supplies, optical drives, peripherals
-  Hard drives, solid state disks and partitions, /dev/sd*
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


-----------------
