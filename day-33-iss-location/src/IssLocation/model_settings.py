from dataclasses import dataclass, asdict
from model_sunset_sunrise import SunsetSunriseModel


@dataclass
class SettingsModel:
    date: str
    sunset_sunrise: SunsetSunriseModel

    @staticmethod
    def from_dict(obj: any) -> 'SettingsModel':
        _date = str(obj.get("date"))
        # _sunset_sunrise = SunsetSunriseModel.from_dict(obj.get("sunset_sunrise"))
        _sunset_sunrise = SunsetSunriseModel(**obj.get("sunset_sunrise"))
        return SettingsModel(_date, _sunset_sunrise)

    def as_dict(self):
        return asdict(self)
