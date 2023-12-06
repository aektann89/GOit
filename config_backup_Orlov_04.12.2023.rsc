# 2023-12-04 10:33:53 by RouterOS 7.11.2
# software id = BAYM-2K65
#
# model = C53UiG+5HPaxD2HPaxD
# serial number = HE708QWGS6M
/interface bridge
add admin-mac=48:A9:8A:78:6C:54 auto-mac=no name=bridge-local
/interface ethernet
set [ find default-name=ether1 ] poe-out=off
set [ find default-name=ether2 ] loop-protect=on loop-protect-disable-time=0s
set [ find default-name=ether3 ] loop-protect=on loop-protect-disable-time=0s
set [ find default-name=ether4 ] loop-protect=on loop-protect-disable-time=0s
set [ find default-name=ether5 ] loop-protect=on loop-protect-disable-time=0s
/interface wifiwave2
set [ find default-name=wifi1 ] channel.skip-dfs-channels=10min-cac \
    configuration.country=Ukraine .mode=ap .ssid=Orlov-5GHz disabled=no \
    security.authentication-types=wpa2-psk,wpa3-psk
set [ find default-name=wifi2 ] channel.skip-dfs-channels=10min-cac \
    configuration.country=Ukraine .mode=ap .ssid=Orlov disabled=no \
    security.authentication-types=wpa2-psk,wpa3-psk
/interface list
add comment=defconf name=WAN
add comment=defconf name=LAN
/ip pool
add name=dhcp ranges=172.16.23.2-172.16.23.254
/ip dhcp-server
add address-pool=dhcp interface=bridge-local lease-time=10m name=dhcp1
/port
set 0 name=serial0
/interface bridge port
add bridge=bridge-local interface=ether2
add bridge=bridge-local interface=ether3
add bridge=bridge-local interface=ether4
add bridge=bridge-local interface=ether5
add bridge=bridge-local interface=wifi1
add bridge=bridge-local interface=wifi2
/ip neighbor discovery-settings
set discover-interface-list=!WAN protocol=mndp
/ipv6 settings
set max-neighbor-entries=15360
/interface list member
add interface=bridge-local list=LAN
add interface=ether1 list=WAN
/ip address
add address=172.16.23.1/24 interface=bridge-local network=172.16.23.0
/ip dhcp-client
add interface=ether1
/ip dhcp-server lease
add address=172.16.23.214 client-id=1:fc:34:97:10:fe:5a mac-address=\
    FC:34:97:10:FE:5A server=dhcp1
add address=172.16.23.198 client-id=1:b8:bc:5b:a5:30:a8 mac-address=\
    B8:BC:5B:A5:30:A8 server=dhcp1
add address=172.16.23.241 client-id=1:e0:2b:96:a9:c2:ac mac-address=\
    E0:2B:96:A9:C2:AC server=dhcp1
add address=172.16.23.151 mac-address=04:CF:8C:48:56:84 server=dhcp1
add address=172.16.23.150 mac-address=54:48:E6:6C:90:1D server=dhcp1
add address=172.16.23.149 mac-address=04:CF:8C:15:91:BF server=dhcp1
add address=172.16.23.140 client-id=1:d6:18:93:14:37:18 mac-address=\
    D6:18:93:14:37:18 server=dhcp1
add address=172.16.23.136 client-id=1:3a:70:18:f9:52:27 mac-address=\
    3A:70:18:F9:52:27 server=dhcp1
add address=172.16.23.123 client-id=1:26:bd:54:6d:ed:a8 mac-address=\
    26:BD:54:6D:ED:A8 server=dhcp1
add address=172.16.23.212 client-id=1:4:d9:f5:f8:9b:7d mac-address=\
    04:D9:F5:F8:9B:7D server=dhcp1
add address=172.16.23.109 client-id=1:90:9:d0:27:a7:f9 mac-address=\
    90:09:D0:27:A7:F9 server=dhcp1
add address=172.16.23.125 client-id=1:d2:75:27:7:ab:53 mac-address=\
    D2:75:27:07:AB:53 server=dhcp1
add address=172.16.23.232 client-id=1:40:b0:76:5b:1c:51 mac-address=\
    40:B0:76:5B:1C:51 server=dhcp1
add address=172.16.23.110 client-id=1:b2:93:33:fc:7d:7 mac-address=\
    B2:93:33:FC:7D:07 server=dhcp1
/ip dhcp-server network
add address=172.16.23.0/24 dns-server=109.86.2.2,109.86.2.21,8.8.8.8,8.8.4.4 \
    gateway=172.16.23.1
/ip dns
set allow-remote-requests=yes servers=8.8.8.8,8.8.4.4
/ip dns static
add address=172.16.23.1 comment=defconf name=router.lan
/ip firewall filter
add action=fasttrack-connection chain=forward connection-state=\
    established,related hw-offload=yes protocol=tcp
add action=fasttrack-connection chain=forward connection-state=\
    established,related hw-offload=yes protocol=udp
add action=accept chain=forward comment="FastTrack Connection" \
    connection-state=established,related
add action=accept chain=input comment=\
    "Allow established & related connections" connection-state=\
    established,related,untracked
add action=add-src-to-address-list address-list=BAN_black_list \
    address-list-timeout=30m chain=input comment=\
    "Add Syn Flood IP to the list" connection-limit=30,32 in-interface-list=\
    WAN protocol=tcp tcp-flags=syn
add action=drop chain=input comment="Drop invalid connections" \
    connection-state=invalid
add action=drop chain=input comment="Dropping all blacklisted IP" \
    src-address-list=BAN_black_list
add action=add-src-to-address-list address-list=BAN_black_list \
    address-list-timeout=2w chain=input comment="Port scanners to list " \
    in-interface-list=WAN protocol=tcp psd=21,3s,3,1
add action=add-src-to-address-list address-list=BAN_black_list \
    address-list-timeout=2w chain=input comment="NMAP FIN Stealth scan" \
    in-interface-list=WAN protocol=tcp tcp-flags=fin,!syn,!rst,!psh,!ack,!urg
add action=add-src-to-address-list address-list=BAN_black_list \
    address-list-timeout=2w chain=input comment="SYN/FIN scan" \
    in-interface-list=WAN protocol=tcp tcp-flags=fin,syn
add action=add-src-to-address-list address-list=BAN_black_list \
    address-list-timeout=2w chain=input comment="SYN/RST scan" \
    in-interface-list=WAN protocol=tcp tcp-flags=syn,rst
add action=add-src-to-address-list address-list=BAN_black_list \
    address-list-timeout=2w chain=input comment="FIN/PSH/URG scan" \
    in-interface-list=WAN protocol=tcp tcp-flags=fin,psh,urg,!syn,!rst,!ack
add action=add-src-to-address-list address-list=BAN_black_list \
    address-list-timeout=2w chain=input comment="ALL/ALL scan" \
    in-interface-list=WAN protocol=tcp tcp-flags=fin,syn,rst,psh,ack,urg
add action=add-src-to-address-list address-list=BAN_black_list \
    address-list-timeout=2w chain=input comment="NMAP NULL scan" \
    in-interface-list=WAN protocol=tcp tcp-flags=\
    !fin,!syn,!rst,!psh,!ack,!urg
add action=jump chain=input comment=\
    "All new connection to port 4101 go to chain \"anti-BruteForce\"" \
    connection-state=new dst-port=4101 in-interface-list=WAN jump-target=\
    anti-BruteForce protocol=tcp
add action=accept chain=anti-BruteForce dst-limit=5/1m,1,src-address/1m40s
add action=add-src-to-address-list address-list=BAN-BruteForce \
    address-list-timeout=1w chain=anti-BruteForce comment=\
    "Add to black list \"BAN-BruteForce\""
add action=accept chain=input comment="Ping access" protocol=icmp
add action=accept chain=input comment="allow DNS to local" dst-port=53 \
    in-interface-list=!WAN protocol=udp
add action=accept chain=input comment=WinBox dst-port=4101 protocol=tcp
add action=drop chain=input comment="Drop other connections"
add action=accept chain=forward comment=\
    "Allow established & related connections" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="Drop invalid connections" \
    connection-state=invalid
add action=drop chain=forward comment="Dropping all blacklisted IP" \
    src-address-list=BAN_black_list
add action=drop chain=forward comment=\
    "Drop All connections except NAT to WAN interface" connection-nat-state=\
    !dstnat in-interface-list=WAN
/ip firewall nat
add action=masquerade chain=srcnat ipsec-policy=out,none out-interface-list=\
    WAN
add action=dst-nat chain=dstnat dst-port=55536-55899 in-interface-list=WAN \
    protocol=tcp to-addresses=172.16.23.109 to-ports=55536-55899
add action=dst-nat chain=dstnat dst-port=1221 in-interface-list=WAN protocol=\
    tcp to-addresses=172.16.23.109 to-ports=1221
/ip firewall raw
add action=drop chain=prerouting dst-port=4101 in-interface-list=WAN \
    protocol=tcp src-address-list=BAN-BruteForce
/ip firewall service-port
set ftp disabled=yes ports=1221
set tftp disabled=yes
set h323 disabled=yes
set sip disabled=yes
set pptp disabled=yes
/ip service
set telnet disabled=yes
set ftp disabled=yes
set www disabled=yes
set ssh disabled=yes
set api disabled=yes
set winbox port=4101
set api-ssl disabled=yes
/ipv6 firewall address-list
add address=::/128 comment="defconf: unspecified address" list=bad_ipv6
add address=::1/128 comment="defconf: lo" list=bad_ipv6
add address=fec0::/10 comment="defconf: site-local" list=bad_ipv6
add address=::ffff:0.0.0.0/96 comment="defconf: ipv4-mapped" list=bad_ipv6
add address=::/96 comment="defconf: ipv4 compat" list=bad_ipv6
add address=100::/64 comment="defconf: discard only " list=bad_ipv6
add address=2001:db8::/32 comment="defconf: documentation" list=bad_ipv6
add address=2001:10::/28 comment="defconf: ORCHID" list=bad_ipv6
add address=3ffe::/16 comment="defconf: 6bone" list=bad_ipv6
/ipv6 firewall filter
add action=accept chain=input comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=input comment="defconf: drop invalid" connection-state=\
    invalid
add action=accept chain=input comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=input comment="defconf: accept UDP traceroute" port=\
    33434-33534 protocol=udp
add action=accept chain=input comment=\
    "defconf: accept DHCPv6-Client prefix delegation." dst-port=546 protocol=\
    udp src-address=fe80::/10
add action=accept chain=input comment="defconf: accept IKE" dst-port=500,4500 \
    protocol=udp
add action=accept chain=input comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=input comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=input comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=input comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
add action=accept chain=forward comment=\
    "defconf: accept established,related,untracked" connection-state=\
    established,related,untracked
add action=drop chain=forward comment="defconf: drop invalid" \
    connection-state=invalid
add action=drop chain=forward comment=\
    "defconf: drop packets with bad src ipv6" src-address-list=bad_ipv6
add action=drop chain=forward comment=\
    "defconf: drop packets with bad dst ipv6" dst-address-list=bad_ipv6
add action=drop chain=forward comment="defconf: rfc4890 drop hop-limit=1" \
    hop-limit=equal:1 protocol=icmpv6
add action=accept chain=forward comment="defconf: accept ICMPv6" protocol=\
    icmpv6
add action=accept chain=forward comment="defconf: accept HIP" protocol=139
add action=accept chain=forward comment="defconf: accept IKE" dst-port=\
    500,4500 protocol=udp
add action=accept chain=forward comment="defconf: accept ipsec AH" protocol=\
    ipsec-ah
add action=accept chain=forward comment="defconf: accept ipsec ESP" protocol=\
    ipsec-esp
add action=accept chain=forward comment=\
    "defconf: accept all that matches ipsec policy" ipsec-policy=in,ipsec
add action=drop chain=forward comment=\
    "defconf: drop everything else not coming from LAN" in-interface-list=\
    !LAN
/system clock
set time-zone-name=Europe/Kyiv
/system note
set show-at-login=no
/system scheduler
add interval=1d name=reboot policy=reboot start-date=2023-10-10 start-time=\
    04:00:00
/tool mac-server
set allowed-interface-list=LAN
/tool mac-server mac-winbox
set allowed-interface-list=LAN
