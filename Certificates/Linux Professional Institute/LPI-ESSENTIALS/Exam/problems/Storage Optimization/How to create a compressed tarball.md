Also refer to [[How to create tarball]]

Using [[tar]]

Specify the [[tar -c|-c]] flag to **create** a new file and to define the new [[tarball]] name
Specify the [[tar -f|-f]] flag to input the file(s) to be used

A compression tool also need to be specified

| -j  | bzip2 |
| --- | ----- |
| -J  | xz    |
| -z  | gzip  |
are some examples of [[Compression Filters]]

If you create compressed .tar archives, you should always add a second file extension denoting the algorithm you used. 
They are **.xz**, **.bz**, and **.gz** 
for **xz**, **bzip2**, and **gzip**, respectively. 
Sometimes shortened extensions such as .tgz are used.

Refer to [[Storage Optimization Extensions]] for more details

For example:
To create a new compressed tarball named test.tar.gz using the contents of the directory named test1 inside the current directory the command would be:
```
tar -cfz test.tar.gz ./test1/*
```