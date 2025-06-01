import socket
import network

from config import UDP_SERVER_HOST, UDP_SERVER_PORT
from utils.logger import Logger

log = Logger("WiFi", level="INFO")


def setup_access_point(ssid, password):
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password)
    log.info("Setting up Access Point...")


def udp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((UDP_SERVER_HOST, UDP_SERVER_PORT))
    sock.listen(1)
    log.info(f"Listening on UDP port {UDP_SERVER_PORT}")
    return sock


def accept_connection(sock):
    data, addr = sock.accept()
    log.info(f"Client connected from: {addr}")
    return data, addr


def receive_command(client):
    data = client.recvfrom(1024)
    if data:
        command = data.decode().strip().upper()
        log.info(f"Received: {command}")
    return


def send_event(client, event):
    try:
        client.send(event.encode())
    except Exception as e:
        log.error(f"Failed to send event {e}")
