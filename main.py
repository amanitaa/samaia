from core import system
from utils.logger import Logger


system.init_system()
system.start_watchdog()


while True:
    system.feed_watchdog()
    system.log_memory()
