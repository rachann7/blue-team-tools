import datetime
import socket
import os

def system_report():
    print('\033[96mSystem Report\033[0m')
    todays_date = datetime.datetime.now()
    print("Today's Date:   " + todays_date.strftime("%Y-%m-%d"))
    print("Current Time:   " + todays_date.strftime("%H:%M:%S"))
    hostname = socket.gethostname()
    print("Hostname:       " + hostname)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print("IP Address:     " + s.getsockname()[0])

def main():
    system_report()

if __name__ == "__main__":
    main()