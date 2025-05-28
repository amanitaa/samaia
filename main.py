from core import system
from core.network import udp_server
from utils.logger import Logger
from services.motion import command_mapper

log = Logger("MAIN", level="INFO")

system.init_system()
system.start_watchdog()

sock = udp_server()

while True:
    system.feed_watchdog()
    system.log_memory()

    data, addr = sock.recvfrom(1024)
    command = data.decode().strip().upper()
    log.info(f"Received: {command}")

    command_mapper[command]()
