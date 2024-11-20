Internet, network, routers
• Querying DNS client configuration
• Querying network configuration

Partial list of the used files, terms and utilities
• route, ip route show
• ifconfig, ip addr show
• netstat, ss
• /etc/resolv.conf, /etc/hosts
• IPv4, IPv6
• ping
• host

This topic covers networking your Linux computer. First we learned about the various levels of
networking:
• The link layer which connects devices directly.
• The networking layer which provides routing between networks and a global address space.
• The application layer where applications connect to each other.
We have seen how IPv4 and IPv6 are used to address individual computers, and how TCP and UDP
enumerate sockets used by applications to connect to each other. We also learned how DNS is used to resolve names to IP addresses.
Commands used in the exercises:
dig
Query DNS information and provide verbose information about the DNS queries and
responses.
host
Query DNS information and provide condensed output.
ip
Configure networking on Linux, including network interfaces, addresses and routing.
ping
Test the connectivity to a remote device.
ss
Show information regarding sockets.

- [x] [[Data Sharing]]
	- [ ] Page 24
	- [ ] Page 25
- [x] Network Administration
	- [ ] Page 25
	- [ ] Page 26

Network Administration

	Communication between computers is only possible if the network is working correctly. Normally, the network configuration is done by a set of programs running on the router, responsible for setting up and checking the network availability. In order to achieve this, two basic network services are used: DHCP (Dynamic Host Configuration Protocol) and DNS (Domain Name System).
	
	DHCP is responsible for assigning an IP address to the host when a network cable is connected or when the device enters a wireless network. When connecting to the Internet, the ISP’s DHCP server will provide an IP address to the requesting device. A DHCP server is very useful in local area networks also, to automatically provide IP addresses to all connected devices. If DHCP is not configured or if it’s not working properly, it would be necessary to manually configure the IP address of each device connected to the network. It is not practical to manually set the IP addresses on large networks or even in small networks, that’s why most network routers come with a DHCP server pre-configured by default.
	
	The IP address is required to communicate with another device on an IP network, but domain names like www.lpi.org are much more likely to be remembered than an IP number like 203.0.113.165. The domain name by itself, however, is not enough to establish the
	
	Linux Essentials (Version 1.6) | 1.2 Major Open Source Applications
	
	Version: 2024-04-29 | Licensed under CC BY-NC-ND 4.0. | learning.lpi.org | 25
	
	communication through the network. That is why the domain name needs to be translated to an IP address by a DNS server. The IP address of the DNS server is provided by the ISP’s DHCP server and it’s used by all connected systems to translate domain names to IP addresses.
	
	Both DHCP and DNS settings can be modified by entering the web interface provided by the router. For instance, it is possible to restrict the IP assignment only to known devices or associate a fixed IP address to specific machines. It’s also possible to change the default DNS server provided by the ISP. Some third-party DNS servers, like the ones provided by Google or OpenDNS, can sometimes provide faster responses and extra features.

- [x] Server Programs
	- [ ] Page 23
	- [ ] Page 24

- Server applications
	- Nextcloud
	- ownCloud
	- Apache HTTPD
	- NGINX
	- MariaDB
	- MySQL
	- NFS
	- Samba