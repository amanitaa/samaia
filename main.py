from core import system
from core.network import udp_server, receive_command, send_event, accept_connection
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

    client, addr = accept_connection(sock)

    command = receive_command(client)
    action = command["action"]
    intensity = command["intensity"]
    command_mapper[action](intensity)

    # maybe run monitoring in different thread?
    telemetry = collect_telemetry()
    send_event(client, telemetry)
