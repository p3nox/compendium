---
type: topic
requires:
  - compression
  - archiving
---
[[Storage Optimization Index]]
Sometimes files can become so huge it become a problem, or even when moving from one place to another, multiple files can be difficult do deal with

There are some solutions to that:

# Archive files
Often referred as [[tarball]], tape files are a way to pack multiple files/folders together
Be advised using an [[Archiving Tools|Archiving Tool]] as tar does not aways mean to compress a file, and compressed tape files cannot be [[tar -u|updated]] without [[tar -x|extracting]] first

[[Managing Zip Files|Zip]] files are other rather common file type you'll in your system administration path, it's referred interchangeably as Archive File and Compression Tool/Algorithm

# Compression
There are a lot of [[Compression Tools]] available on Linux systems, if needed, tar can use some of them as [[Compression Filters]] to easily create compressed archive files
