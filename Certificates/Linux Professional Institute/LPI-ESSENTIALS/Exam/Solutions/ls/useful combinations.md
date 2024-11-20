---
title:
  - "[[useful combinations]]"
type: variation
requires:
  - "[[ ls]]"
tags:
  - variation
---
Additional ls Options

Below are some of the ways that we most commonly use the ls command. As you can see, the user can combine many options together to get the desired output.

Linux Essentials (Version 1.6) | Topic 2: Finding Your Way on a Linux System

132 | learning.lpi.org | Licensed under CC BY-NC-ND 4.0. | Version: 2024-04-29

ls -lh

Combining long list with human readable file sizes will give us useful suffixes such as M for megabytes or K for kilobytes.

ls -d */

The -d option will list directories but not their contents. Combining this with */ will show only subdirectories and no files.

ls -lt

Combines long list with the option to sort by modification time. The files with the most recent changes will be at the top, and files with the oldest changes will be at the bottom. But this order can be reversed with:

ls -lrt

Combines long list with sort by (modification) time, combined with -r which reverses the sort. Now files with the most recent changes are at the bottom of the list. In addition to sorting by modification time, files can also be sorted by access time or by status time.

ls -lX

Combines long list with the option to sort by file eXtension. This will, for example, group all files ending with .txt together, all files ending with .jpg together, and so on.

ls -S

The -S sorts by file size, much in the same way as -t and -X sort by time and extension respectively. The largest files will come first, and smallest last. Note that the contents of subdirectories are not included in the sort.

ls -R

The -R option will modify the ls command to display a recursive list. What does this mean?