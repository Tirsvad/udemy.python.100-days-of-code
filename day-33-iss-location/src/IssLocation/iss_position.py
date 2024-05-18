import json

from constants import *
import datetime as dt
import requests
import smtplib
import tkinter as tk
import tkintermapview
from tkintermapview import canvas_position_marker
from PIL import Image, ImageTk


class IssPosition(tk.Tk):
    # param for Iss API
    # parameters: dict[str: float, str: float]
    sunrise: int
    sunset: int
    time_now: dt.datetime
    iss_latitude: float | None = None
    iss_longitude: float | None = None
    map_widget: tkintermapview.TkinterMapView | None = None
    marker_list: list[canvas_position_marker.CanvasPositionMarker] = []
    map_tile_loader: tkintermapview.offline_loading.OfflineLoader | None = None
    # time events id
    after_id_update_map = None
    after_id_seconds_to_midnight = None
    # icons
    icon_satellite: ImageTk.PhotoImage
    icon_satellite_red: ImageTk.PhotoImage
    icon_home: ImageTk.PhotoImage
    # app settings
    settings: dict = {}

    def __init__(self):
        super().__init__()

        # Satellite icons
        self.icon_satellite = ImageTk.PhotoImage(Image.open(ICON_FILE))
        self.icon_satellite_red = ImageTk.PhotoImage(Image.open(ICON_RED_FILE))
        self.icon_home = ImageTk.PhotoImage(Image.open(ICON_HOME_FILE))

        # Offline maps
        self.map_tile_loader = tkintermapview.OfflineLoader(path=DB_FILE)

        self.title("Track ISS space station")

    def destroy(self):
        # self.after_cancel(self.after_id_update_map)
        # self.after_cancel(self.after_id_seconds_to_midnight)
        super().destroy()
        exit()

    def run(self) -> None:
        self.load_config()
        self.get_sunrise_sunset()
        self.create_map()
        self.update_map()
        self.mainloop()

    def load_config(self):
        try:
            with open(CONFIG_FILE, 'r') as f:
                self.settings = json.load(f)
        except FileNotFoundError:
            self.save_config(self.settings)
        else:
            self.sunrise = self.settings['sunrise']
            self.sunset = self.settings['sunset']

    @staticmethod
    def save_config(data: dict):
        with open(CONFIG_FILE, 'w') as f:
            json.dump(data, f)

    def get_sunrise_sunset(self) -> None:
        self.time_now = dt.datetime.now()
        if 'date' in self.settings.keys():
            if self.settings['date'] == str(self.time_now.date()):
                return

        print("Getting sunrise and sunset")
        midnight = dt.datetime.combine(self.time_now.date(), dt.time())
        seconds_to_midnight = 24*60*60 - (self.time_now - midnight).seconds
        self.after_id_seconds_to_midnight = self.after(seconds_to_midnight, func=self.get_sunrise_sunset)

        print(self.time_now.date())
        self.settings.update({'date': self.time_now.date().isoformat()})
        print(self.settings)
        response = requests.get(
            url=SUNRISE_SUNSET_API,
            params={'lat': MY_LATITUDE, 'lng': MY_LONGITUDE, 'formatted': 0})
        response.raise_for_status()
        data = response.json()
        self.settings['sunrise'] = data['results']['sunrise'].split(sep='T')[1].split(':')[0]
        self.settings['sunset'] = data['results']['sunset'].split(sep='T')[1].split(':')[0]
        self.save_config(self.settings)


    def get_iss_position(self) -> tuple[float, float]:
        response = requests.get(ISS_POSITION_API)
        response.raise_for_status()
        data: dict = response.json()
        self.iss_latitude = float(data['iss_position']['latitude'])
        self.iss_longitude = float(data['iss_position']['longitude'])
        return self.iss_latitude, self.iss_longitude

    def can_see_iss(self) -> bool:

        if self.iss_latitude - 5 < MY_LATITUDE < self.iss_latitude + 5 and \
                self.iss_longitude - 5 < MY_LONGITUDE < self.iss_longitude + 5:
            print('ISS is over you now')
            if self.sunrise < self.time_now.hour < self.sunset:
                print("Is day time and you can not see ISS")
                return False
            else:
                print("You may see ISS in the sky")
                print(f"https://www.latlong.net/c/?lat={self.iss_latitude}&long={self.iss_longitude}")
                return True

    def create_map(self) -> None:
        print(f"Info creating map")
        self.map_widget = tkintermapview.TkinterMapView(
            self,
            width=1200,
            height=800,
            corner_radius=0,
            database_path=DB_FILE)
        self.map_widget.set_tile_server(tile_server=TILE_SERVER_API, max_zoom=22)  # google satellite
        self.map_widget.set_zoom(1)
        self.protocol("WM_DELETE_WINDOW", self.destroy)

        self.map_tile_loader.save_offline_tiles(
            (MY_LATITUDE, MY_LONGITUDE),
            (MY_LATITUDE, MY_LONGITUDE),
            0,
            5
        )
        self.map_widget.pack()

        self.map_widget.set_marker(
            deg_x=MY_LATITUDE,
            deg_y=MY_LONGITUDE,
            text="",
            icon=self.icon_home)

    def update_map(self) -> None:
        self.time_now = dt.datetime.now()
        # self.get_sunrise_sunset()
        self.get_iss_position()
        # self.can_see_iss()

        self.map_widget.set_position(deg_x=self.iss_latitude, deg_y=self.iss_longitude)

        if (len(self.marker_list)) > 0:
            # When zoom in and out thi line is needed other ways it will change back to red color
            self.marker_list[-1].icon = self.icon_satellite
            # changing mapview marker icon
            self.map_widget.canvas.itemconfig(self.marker_list[-1].canvas_icon, image=self.icon_satellite)
        self.marker_list.append(self.map_widget.set_marker(
            deg_x=self.iss_latitude,
            deg_y=self.iss_longitude,
            text="",
            icon=self.icon_satellite_red))
        self.after_id_update_map = self.after(60000, func=self.update_map)


app = IssPosition()
app.run()
