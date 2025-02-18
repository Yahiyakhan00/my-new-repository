import socket
import struct

def packet_sniffer():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    while True:
        raw_data, addr = conn.recvfrom(65536)
        dest_mac, src_mac, proto, data = struct.unpack('! 6s 6s H', raw_data[:14])
        print(f'Source MAC: {src_mac} Destination MAC: {dest_mac} Protocol: {proto}')

if __name__ == "__main__":
    print("Projects are implemented as functions. Call them accordingly.")