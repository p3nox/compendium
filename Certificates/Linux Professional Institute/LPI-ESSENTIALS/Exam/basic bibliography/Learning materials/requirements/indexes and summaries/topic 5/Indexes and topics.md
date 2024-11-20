346-442
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