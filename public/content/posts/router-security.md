---
title: "设置路由器时要注意的安全问题"
author: "linna.li"
tags: ["security"]
categories: ["note"]
date: 2021-01-22
---

### 路由器的设置目标和图解

As long as it's all locked inside your home network it's relatively safe.
We want to reject all incoming connections , all the incoming connections are hackers.
Internet to WAN to LAN: All Blocked
LAN to WAN to Internet: All Allowed
LAN to LAN (Server to Server, like Macbook to Server): Allowed
![](/images/router.png)

### 路由器的各种设置

- Be careful of any kind of “cloud setup” where you make an account.
- Don't use tp-link cloud service
- Avoid accessing stuff outside your local network.  For example, here you may see "Method 2: Via a Web Browser", and it says about using http://tplinkwifi.net  don't do this.  just go directly to 192.168.0.1,  maybe their site is just a redirect, but still it's best to stay on the local network.
- and disable UPnP,  UPnP is like an "automatically configured" NAT 転送,  it's designed to make it easier to use some devices that require it,  For example some game consoles like Playstation or Nintendo can require port forwarding for some online games to work. This is why the router comes with UPnP
- Don't use WPS,  WPS is like auto-setup for the wifi , it is some settings that designed to make it easier to discover and connect to the wifi network. it's better to do it manually. there is a special button and also can be disabled from web page.
- Disable NAT forwarding(NAT 転送), NAT forwarding (also "port forwarding(仮想サーバー)") opens a hole in your firewall. it's not needed unless you want to let your friends outside access the server.
- "Port triggering" is similar to "port forwarding(仮想サーバー)"), but not exactly the same. seems to support multiple computers on the LAN or something.
- NAT should be enabled, it is network address translation
- Choose a WiFi SSID which does not include your name, Make a strong WiFi password
- Turn off ゲストネットワーク, start by changing it from "No Security" to "WPA/WPA2" and set a strong password. that way if it's ever turned on somehow a password is still required. "Guest Network" is a separate WiFi network, isolated from the main network.
- For バージョン change from 自動 to WPA2-PSK. and for 暗号化 change to AES. It tells the WiFi to use a stronger encryption standard. (your Wifi traffic is encrypted)
- should not use DMZ, DMZ also lets the people from outside into your home network.
- ALG menu, disable all of those: PPTP, L2TP and IPSec are for VPNs,  SIP is for voice over IP,
- make sure "Remote Management" is OFF. If enable, it will take control of your router from the WAN port. by default you can only manage from inside the LAN
- Disable cwmp,  https://en.wikipedia.org/wiki/TR-069 Also a remote manage thing
- take a back up. バックアップおよび復元

Knowledge:

- DHCP : gives the IP address to your computer automatically. it's good to use DCHP to start. This "DCHP Client List" is important to remember. Later you can use it to find your raspberry pi.
- スマートコネクト it will let you separate 5Ghz and 2Ghz. the more devices that are on the same network, the more the congestion increases so for something like Clova it's probably acceptable to push it to the slower network.
- port forwarding is similar to the load balancer in front of our servers. If disabled it, if the connection gets to the router on port 8080, it doesn't understand which device on the LAN to send the connection to;  If enable it,  In the case of the router use port forwarding to tell the router to send some incoming connection on WAN to HostA on the LAN, then someone can connect to your router on port XXXX and it will connect to HostA running XXXX.  ( In the case of the load balancer, it picks one of the hosts and sends the connection. distributed evenly. )
- the router is like the load balancer in this case, but it does no balancing. just send the request to the same host every time (and you tell it which is the correct destination, if you use port forwarding,  you need to choose the back end host to map the port to.).  If you use port forwarding then,  Internet to WAN to LAN to Server (on port 8080): Allowed,  then your server gets hacked. because you allow the hackers to enter the home network and connect to the server.
- ALG: the router has a firewall in it and the firewall may interfere with certain types of traffic like the ones I mentioned above. so it has these ALG items to like "whitelist" certain types of traffic so that the router doesn't interfere. if you find some network thing is not working you can see if it's one of these protocols but for now maybe you don't need them.
- your router has no logs for the hackers it rejects, but I guarantee you that it's blocking them for you the same way mine is for me.
- keep QoS disabled. Quality of Service, QoS will let you make the network slower, or disable it during some times.  can degrade the network speed and stuff for some users or some times of day.
- User ルーター mode, you only have one networking device so you want "Router" mode,  but not access point, "Access Point" means you have another device for your router and you just use this one to get WiFi and increase the number of ethernet ports.
- by default the wireless technology has like a single queue used and it's first come first serve, so the clients can block each other, MU-MIMO is designed to help with that.
- TxBF seems to be designed to make the signal stronger in certain areas,
- the router is a kind of server, server with many network ports.  That 192.168.0.1 is the address of the router device itself, as seen from the LAN side of the network. Router only listens for 192.168.0.1 on the LAN ports. They are in the private IP address space so they can be used for LAN in any network.  there is also a WAN side IP address, you can't use it for managing the router. unless you turn on "Remote Management"
- Can try set up the guest network and connect your work computers to that. and then if you configured the guest network properly, they will be isolated from your server etc.
