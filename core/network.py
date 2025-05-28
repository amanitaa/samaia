import socket
from config import UDP_SERVER_HOST, UDP_SERVER_PORT
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
