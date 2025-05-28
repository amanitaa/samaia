import gc
import machine
import time
import network

from utils.logger import Logger

log = Logger("System", level="INFO")

wdt = None

def init_system():
    gc.collect()
    log.info("System initialized. Memory cleaned.")


def start_watchdog(timeout_ms=5000):
    global wdt
    wdt = machine.WDT(timeout=timeout_ms)
    log.info("Watchdog started.")


def feed_watchdog():
    if wdt:
        wdt.feed()


def get_free_memory():
    return gc.mem_free()


def get_allocated_memory():
    return gc.mem_alloc()


def log_memory():
    log.info(f"Free: {get_free_memory()} | Allocated: {get_allocated_memory()}")


def soft_reboot():
    log.info("Soft rebooting...")
    machine.reset()


def get_system_status():
    wlan = network.WLAN(network.STA_IF)
    return {
        "uptime_ms": time.ticks_ms(),
        "ip": wlan.ifconfig()[0] if wlan.isconnected() else None,
        "free_memory": get_free_memory()
    }
