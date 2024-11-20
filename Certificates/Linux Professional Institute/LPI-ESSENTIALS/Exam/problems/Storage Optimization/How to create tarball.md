Using [[tar]]

Specify the [[tar -c|-c]] flag to **create** a new file and to define the new [[tarball]] name
Specify the [[tar -f|-f]] flag to input the file(s) to be used
For best practice, always use .tar as file extension for tarballs

For example:
To create a new tarball named test.tar using the contents of the directory named test1 inside the current directory and the file test2 on the current directory the command would be:

`tar -cf test.tar ./test1/* ./test2`

![[tar -v]]