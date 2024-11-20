				- [x] [[Kernel and kernel modules]]
					- [ ] Page 287
					- [ ] Page 288
					- [ ] Page 289
Before any process can run, the kernel must be loaded into a protected area of memory. After that, the process with PID 1 (more often than not [[systemd]] nowad]ays) sets off the chain of processes, that is to say, one process starts other(s) and so on. Once the processes are active, the [[Linux kernel]] is in charge of allocating resources to them (keyboard, mouse, disks, memory,
network interfaces, etc).



```
Prior to systemd, /sbin/init was always the first process in a Linux system as
part of the System V Init system manager. In fact, you still find /sbin/init currently but linked to /lib/systemd/systemd.
```

Where Kernels are Stored: [[/boot]]

The kernel resides in /boot — together with other boot-related files. Most of these files include the
kernel version number components in their names (kernel version, major revision, minor
revision and patch number).
The /boot directory includes the following types of files, with names corresponding with the
respective kernel version:

**config-4.9.0-9-amd64**
Configuration settings for the kernel such as options and modules that were compiled along with the kernel.
**initrd.img-4.9.0-9-amd64**
Initial RAM disk image that helps in the startup process by loading a temporary root filesystem into memory.
**System-map-4.9.0-9-amd64**
The System-map (on some systems it will be named System.map) file contains memory
address locations for kernel symbol names. Each time a kernel is rebuilt the file’s contents will change as the memory locations could be different. The kernel uses this file to lookup memory address locations for a particular kernel symbol, or vice-versa.
**vmlinuz-4.9.0-9-amd64**
The kernel proper in a self-extracting, space-saving, compressed format (hence the z in
vmlinuz; vm stands for virtual memory and started to be used when the kernel first got support for virtual memory).
**grub**
Configuration directory for the grub2 bootloader.

```
Because it is a critical feature of the operating system, more than one kernel and its associated files are kept in /boot in case the default one becomes faulty and we have to fall back on a previous version to — at least — be able to boot the system up and fix it.
```

**The /proc Directory**
The /proc directory is one of the so-called virtual or pseudo filesystems since its contents are not written to disk, but loaded in memory. It is dynamically populated every time the computer boots up and constantly reflects the current state of the system. /proc includes information about:

Besides all the data concerning processes that we will see in the next lesson, this directory also stores files with information about the system’s hardware and the kernel’s configuration settings.
Some of these files include:
 - [ ] /proc/cpuinfo
	 -  It stores information about the system’s CPU:
		 ```
		 $ cat /proc/cpuinfo
		processor : 0
		vendor_id : GenuineIntel
		cpu family : 6
		model : 158
		model name : Intel(R) Core(TM) i7-8700K CPU @ 3.70GHz
		stepping : 10
		cpu MHz : 3696.000
		cache size : 12288 KB
		```
 - [ ] /proc/cmdline
	 - It stores the strings passed to the kernel on boot:
		 ```
		$ cat /proc/cmdline
		BOOT_IMAGE=/boot/vmlinuz-4.9.0-9-amd64 root=UUID=5216e1e4-ae0e-441f-b8f5-8061c0034c74 ro
		quiet
		```
 - [ ] /proc/modules
	 - It shows the list of modules loaded into the kernel:
		 ```
			$ cat /proc/modules
			nls_utf8 16384 1 - Live 0xffffffffc0644000
			isofs 40960 1 - Live 0xffffffffc0635000
			udf 90112 0 - Live 0xffffffffc061e000
			crc_itu_t 16384 1 udf, Live 0xffffffffc04be000
			fuse 98304 3 - Live 0xffffffffc0605000
			vboxsf 45056 0 - Live 0xffffffffc05f9000 (O)
			joydev 20480 0 - Live 0xffffffffc056e000
			vboxguest 327680 5 vboxsf, Live 0xffffffffc05a8000 (O)
			hid_generic 16384 0 - Live 0xffffffffc0569000
			(...)
		```

**The /proc/sys Directory**

This directory includes kernel configuration settings in files classified into categories per
subdirectory:
```
		$ ls /proc/sys
		abi debug dev fs kernel net user vm
```
Most of these files act like a switch and — therefore — only contain either of two possible values: 0 or 1 (“on” or “off”). For instance:

**/proc/sys/net/ipv4/ip_forward**
The value that enables or disables our machine to act as a router (be able to forward packets):
```
$ cat /proc/sys/net/ipv4/ip_forward
0
```

There are some exceptions, though:

**/proc/sys/kernel/pid_max**
	The maximum PID allowed:
```
	$ cat /proc/sys/kernel/pid_max
32768
```

%%
**Be extra careful when changing the kernel settings as the wrong value may**
**result in an unstable system.**
%%