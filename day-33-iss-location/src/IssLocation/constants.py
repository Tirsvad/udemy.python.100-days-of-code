import os

# Semenyih, Malaysia
MY_LATITUDE = 2.927832
MY_LONGITUDE = 101.897238

ISS_POSITION_API = 'http://api.open-notify.org/iss-now.json'
SUNRISE_SUNSET_API = 'https://api.sunrise-sunset.org/json'
# TILE_SERVER_API = 'https://a.tile.openstreetmap.org/{z}/{x}/{y}.png'  # OpenStreetMap
TILE_SERVER_API = 'https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga'  # google normal
# TILE_SERVER_API = 'https://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}&s=Ga'  # google maps satellite

DB_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'offline_tiles.db')
CONFIG_FILE = os.path.normpath('data/config.json')
ICON_FILE = os.path.normpath('images/32px-FP_Satellite_icon.svg.png')
ICON_RED_FILE = os.path.normpath('images/32px-FP_Satellite_icon_red.png')
ICON_HOME_FILE = os.path.normpath('images/32px-Home_free_icon.svg.png')
