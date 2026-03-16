import socket

s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)

print("Monitoring Network Traffic...")

while True:
    packet = s.recvfrom(65565)
    print("Packet Captured:", packet[0][:20])