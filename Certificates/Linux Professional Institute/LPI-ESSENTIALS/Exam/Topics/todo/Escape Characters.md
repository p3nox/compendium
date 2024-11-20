Escape Characters

We can use escape characters to remove special meanings of characters from Bash. Going back to the $USER environment variable:

$ echo $USER carol

We see that by default, the contents of the variable are displayed in the terminal. However, if we were to precede the dollar sign with a backslash character (\) then the special meaning of the dollar sign will be negated. This in turn will not let Bash expand the variable’s value to the username of the person running the command, but will instead interpret the variable name literally:

Linux Essentials (Version 1.6) | 2.1 Command Line Basics

Version: 2024-04-29 | Licensed under CC BY-NC-ND 4.0. | learning.lpi.org | 77

$ echo \$USER $USER

If you recall, we can get similar results to this using the single quote, which prints the literal contents of whatever is between the single quotes. However the escape character works differently by instructing Bash to ignore whatever special meaning the character it precedes may possess.