from core import system
from core.network import udp_server, receive_command, send_event
from core.system import collect_telemetry
from utils.logger import Logger
from services.motion import command_mapper

log = Logger("MAIN", level="INFO")

system.init_system()
system.start_watchdog()

sock = udp_server()

while True:
    system.feed_watchdog()
    system.log_memory()

    command = receive_command(sock)
    command_mapper[command]()

    # maybe run monitoring in different thread?
    telemetry = collect_telemetry()
    send_event(sock, telemetry)
