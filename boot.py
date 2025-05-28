from config import SSID, PASSWORD
from core.network import connect_wifi


ip = connect_wifi(SSID, PASSWORD)
