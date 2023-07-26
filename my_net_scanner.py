import scapy.all as scapy
import optparse
def get_user_input():
    opt_object=optparse.OptionParser()
    opt_object.add_option("-r","--range",dest="range",help="Enter ip address")
    (user_input,arguments)=opt_object.parse_args()
    if not user_input:
        print("enter ip address")

    return user_input

def scan_my_network(ip):
    arp_request_packet=scapy.ARP(pdst=ip)
    broadcast_packet=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet=broadcast_packet/arp_request_packet
    (answered_list,unanswered_list)=scapy.srp(combined_packet,timeout=1)
    answered_list.summary()
user_ip_address=get_user_input()
scan_my_network(user_ip_address.range)