from dataclasses import dataclass


@dataclass
class SunsetSunriseModel:
    sunrise: str
    sunset: str
    solar_noon: str
    day_length: int
    civil_twilight_begin: str
    civil_twilight_end: str
    nautical_twilight_begin: str
    nautical_twilight_end: str
    astronomical_twilight_begin: str
    astronomical_twilight_end: str

    # @staticmethod
    # def from_dict(obj: any) -> 'SunsetSunriseModel':
    #     _sunrise = str(obj.get("sunrise"))
    #     _sunset = str(obj.get("sunset"))
    #     _solar_noon = str(obj.get("solar_noon"))
    #     _day_length = int(obj.get("day_length"))
    #     _civil_twilight_begin = str(obj.get("civil_twilight_begin"))
    #     _civil_twilight_end = str(obj.get("civil_twilight_end"))
    #     _nautical_twilight_begin = str(obj.get("nautical_twilight_begin"))
    #     _nautical_twilight_end = str(obj.get("nautical_twilight_end"))
    #     _astronomical_twilight_begin = str(obj.get("astronomical_twilight_begin"))
    #     _astronomical_twilight_end = str(obj.get("astronomical_twilight_end"))
    #     return SunsetSunriseModel(_sunrise, _sunset, _solar_noon, _day_length, _civil_twilight_begin, _civil_twilight_end, _nautical_twilight_begin, _nautical_twilight_end, _astronomical_twilight_begin, _astronomical_twilight_end)
