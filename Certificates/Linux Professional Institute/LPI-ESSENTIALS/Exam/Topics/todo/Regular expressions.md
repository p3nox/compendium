The following list explains the regular expressions meta-characters that are used to form the patterns.

.

Match any single character (except newline)

[abcABC]

Match any one character within the brackets

[^abcABC]

Match any one character except the ones in the brackets

[a-z]

Match any character in the range

[^a-z]

Match any character except the ones in the range

sun|moon

Find either of the listed strings

^

Start of a line

$

End of a line

All functionalities of the regular expressions can be implemented through grep as well

On top of the previous explained meta-characters, regular expressions also have meta-characters that enable multiplication of the previously specified pattern:

*

Zero or more of the preceding pattern

+

One or more of the preceding pattern

?

Zero or one of the preceding pattern