- [x] Office programs
	- [ ] Page 21
- [x] [[web browsers programs]]
	- [ ] Page 22
- [x] multimedia programs
	- [ ] Page 22 ~ 23
- [x] [[Data Sharing]]
	- [ ] Page 24
	- [ ] Page 25
- [x] Network Administration
	- [ ] Page 25
	- [ ] Page 26

• Open source applications that can edit popular file formats
- Multimedia
	- Blender
	- GIMP
	- Inkscape
	- Audacity
	- ImageMagick
	- VLC
- Desktop applications
	- OpenOffice.org
	- LibreOffice
	- Thunderbird
	- [[Firefox]]
	- GIMP
- [[Desktop skills]]
	- Use of common open source applications in presentations and projects
		- Finally, LibreOffice Impress is a very complete open source alternative to Microsoft Powerpoint

Powerpoint but there are Beamer and RevealJS if you prefer to create presentations using code instead of GUIs. 
ProjectLibre and GanttProject can be the right choice if you need a Microsoft Project replacement.

Differences between Windows, OS X and Linux
• Distribution life cycle management

Network Administration

Communication between computers is only possible if the network is working correctly. Normally, the network configuration is done by a set of programs running on the router, responsible for setting up and checking the network availability. In order to achieve this, two basic network services are used: DHCP (Dynamic Host Configuration Protocol) and DNS (Domain Name System).

DHCP is responsible for assigning an IP address to the host when a network cable is connected or when the device enters a wireless network. When connecting to the Internet, the ISP’s DHCP server will provide an IP address to the requesting device. A DHCP server is very useful in local area networks also, to automatically provide IP addresses to all connected devices. If DHCP is not configured or if it’s not working properly, it would be necessary to manually configure the IP address of each device connected to the network. It is not practical to manually set the IP addresses on large networks or even in small networks, that’s why most network routers come with a DHCP server pre-configured by default.

The IP address is required to communicate with another device on an IP network, but domain names like www.lpi.org are much more likely to be remembered than an IP number like 203.0.113.165. The domain name by itself, however, is not enough to establish the communication through the network. That is why the domain name needs to be translated to an IP address by a DNS server. The IP address of the DNS server is provided by the ISP’s DHCP server and it’s used by all connected systems to translate domain names to IP addresses.

Both DHCP and DNS settings can be modified by entering the web interface provided by the router. For instance, it is possible to restrict the IP assignment only to known devices or associate a fixed IP address to specific machines. It’s also possible to change the default DNS server provided by the ISP. Some third-party DNS servers, like the ones provided by Google or OpenDNS, can sometimes provide faster responses and extra features.

[[Make the system accessible and able to connect to other computers on a Local Area Network (LAN)]]

