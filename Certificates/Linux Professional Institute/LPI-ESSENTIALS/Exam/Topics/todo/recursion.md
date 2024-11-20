Recursion in Bash

Recursion refers to a situation when “something is defined in terms of itself”. Recursion is a very important concept in computer science, but here its meaning is far simpler. Let’s consider our example from before:

$ ls ~ Documents

We know from before that user has a home directory, and in this directory there is one subdirectory. ls has up until now only shown us the files and subdirectories of a location, but cannot tell us the contents of these subdirectories. In these lessons, we have been using the tree command when we wanted to display the contents of many directories. Unfortunately, tree is not one of the core utilities of Linux and thus is not always available. Compare the output of tree with the output of ls -R in the following examples:
```

$ tree /home/user 
user 
└── Documents

	├── Mission-Statement
	└── Reports 
		└── report2018.txt

$ ls -R ~ 
/home/user/: 
Documents

/home/user/Documents: 
Mission-Statement 
Reports

/home/user/Documents/Reports: 
report2018.txt
```

As you can see, with the recursive option, we get a far longer list of files. In fact, it is as if we ran the ls command in user 's home directory, and encountered one subdirectory. Then, we entered into that subdirectory and ran the ls command again. We encountered the file MissionStatement and another subdirectory called Reports. And again, we entered into the subdirectory, and ran the ls command again. Essentially, running ls -R is like telling Bash: “Run ls here, and repeat the command in every subdirectory that you find.”

Recursion is particularly important in file modification commands such as copying or removing directories. For example, if you wanted to copy the Documents subdirectory, you would need to specify a recursive copy in order to extend this command to all subdirectories.