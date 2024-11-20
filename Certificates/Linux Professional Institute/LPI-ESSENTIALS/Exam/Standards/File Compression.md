---
type: standard
origin: lpi0
tags:
  - standard
Total: 15
Completed: 15
Todo: 15
---
`$= const File Compression = dv.current();const value = Math.round(Page.Completed / Page.Total * 100);"<progress value='" + value + "' max='100'></progress> " + value + "%" `

- [x] Difference between Compression and Archiving tools
	- [x] Page 170
	- [x] Page 171
- [x] Compression Tools
	- [x] Page 171
	- [x] Page 172
	- [x] Page 173
- [ ] Archiving Tools
	- [ ] Page 174
	- [ ] Page 175
	- [ ] Page 176
	- [ ] Page 177
- [ ] Managing Zip Files
	- [ ] Page 177
	- [ ] Page 178

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

tar
• Common tar options
• gzip, bzip2, xz
• zip, unzip
bunzip2
Decompress a bzip2 compressed file.
bzcat
Output the contents of a bzip compressed file.
bzip2
Compress files using the bzip2 algorithm and format.
gunzip
Decompress a gzip compressed file.
gzip
Compress files using the gzip algorithm and format.
tar
Create, update, list and extract tar archives.
unxz
Decompress a xz compressed file.
unzip
Decompress and extract content from a ZIP file.
xz Compress files using the xz algorithm and format.
zcat
Output the contents of a gzip compressed file.
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