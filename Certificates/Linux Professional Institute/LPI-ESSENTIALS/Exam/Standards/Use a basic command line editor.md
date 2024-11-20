- [x] Common CLI Text Editors
	- [ ] Page 216
	- [ ] Page 217
- [x] Programs and their configuration files (nanorc)
	- [ ] Page 286
	- [ ] Page 287 

Common Text Editors

Linux users often have to work in an environment where graphical text editors are not available. It is therefore highly recommended to develop at least some familiarity with editing text files from the command line. Two of the most common text editors are vi and nano.

vi

vi is a venerable text editor and is installed by default on almost every Linux system in existence. vi spawned a clone called vi IMproved or vim which adds some functionality but maintains the interface of vi. While working with vi is daunting for a new user, the editor is popular and wellloved by users who learn its many features.

Linux Essentials (Version 1.6) | Topic 3: The Power of the Command Line

216 | learning.lpi.org | Licensed under CC BY-NC-ND 4.0. | Version: 2024-04-29

The most important difference between vi and applications such as Notepad is that vi has three different modes. On startup, the keys H , J , K and L are used to navigate, not to type. In this navigation mode, you can press I to enter insert mode. At this point, you may type normally. To exit insert mode, you press Esc to return to navigation mode. From navigation mode, you can press : to enter command mode. From this mode, you can save, delete, quit or change options.

While vi has a learning curve, the different modes can in time allow a savvy user to become more efficient than with other editors.

nano

nano is a newer tool, built to be simple and easier to use than vi. nano does not have different modes. Instead, a user on startup can begin typing, and uses Ctrl to access the tools printed at the bottom of the screen.

[ Welcome to nano. For basic help, type Ctrl+G. ]

^G Get Help ^O Write Out ^W Where Is ^K Cut Text ^J Justify ^C Cur Pos M-U Undo

^X Exit ^R Read File ^\ Replace ^U Uncut Text ^T To Spell ^_ Go To Line M-E Redo

Text editors are a matter of personal preference, and the editor that you choose to use will have no bearing on this lesson. But becoming familiar and comfortable with one or more text editors will pay off in the future.