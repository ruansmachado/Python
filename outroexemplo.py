import sys
import time
from scapy.all import Ether, IP, TCP, sendp

TARGET_IP = "192.168.X.X" #Mudar para o IP que pretende atingir
INTERFACE = "eth0" #Mudar para sua interface de internet
NUM_PACKETS = 100
DURATION = 5

def send_packets(target_ip, interface, num_packet, duration):
    packet = Ether() / IP(dst=target_ip) / TCP ()
    end_time = time.time() + duration
    packet_count = 0

    while time.time() < end_time and packet_count < NUM_PACKETS:
        sendp(packet, iface=interface)
        packet_count += 1   

if __name__ == "__main__":
    if sys.version_info[0] < 3:
        print("This script requires Python 3.")
        sys.exit(1)

    send_packets(TARGET_IP, INTERFACE, NUM_PACKETS, DURATION)

