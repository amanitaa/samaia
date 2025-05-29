import socket
from config import UDP_SERVER_HOST, UDP_SERVER_PORT, SAMAYA_CONTROLLER_IP, SAMAYA_CONTROLLER_PORT
import network
import time
from utils.logger import Logger

log = Logger("WiFi", level="INFO")


def connect_wifi(ssid, password, timeout=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if not wlan.isconnected():
        log.info(f"Connecting to {ssid}...")
        wlan.connect(ssid, password)

        start = time.time()
        while not wlan.isconnected():
            if time.time() - start > timeout:
                log.error("Wi-Fi connection timed out!")
                return None
            time.sleep(0.5)

    log.info(f"Connected! IP: {wlan.ifconfig()[0]}")
    return wlan.ifconfig()[0]


def udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_SERVER_HOST, UDP_SERVER_PORT))
    log.info(f"Listening on UDP port {UDP_SERVER_PORT}")
    return sock


def receive_command(sock):
    data, addr = sock.recvfrom(1024)
    command = data.decode().strip().upper()
    log.info(f"Received: {command}")
    return command


def send_event(sock, event):
    try:
        sock.sendto(event.encode(), (SAMAYA_CONTROLLER_IP, SAMAYA_CONTROLLER_PORT))
    except Exception as e:
        log.error(f"Failed to send event {e}")
