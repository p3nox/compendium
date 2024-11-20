Using [[tar]]

Cannot add files to compressed tarballs
It is possible to add files to already existing uncompressed tar archives. Use the u option to do this.

Specify the [[tar -u|-u]] flag to **update** a tarball
Specify the [[tar -f|-f]] flag to input the file(s) to be used

For example:
To update the tarball named plain.tar adding the file test1 in the current directory

```
tar -uf plain.tar ./test1
```