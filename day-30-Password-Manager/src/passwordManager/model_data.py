from dataclasses import dataclass
from model_data_approach import DataApproachModel

@dataclass
class DataModel:
    file_data_version: float
    default_username: str
    webpages: list[DataApproachModel]

    def __init__(self):
        self.webpages = []
        self.file_data_version = 1
        self.default_username = ""

    def from_dict(self, obj: dict) -> 'DataModel':
        """
        populate values from obj: dict

        :param obj: dictionary from json or others
        :return: Datafile
        """
        if int(obj.get("file_data_version")) != int(self.file_data_version):
            raise ValueError(f"File version {obj.get('file_data_version')} is not supported")
        self.default_username = str(obj.get("default_username"))
        file_data_version = int(obj.get("file_data_version"))
        self.webpages = [DataApproachModel.from_dict(y) for y in obj.get("webpages")]

        if file_data_version != self.file_data_version:
            print(f"File version is not compatible with this version of application")
            raise ValueError
        return DataModel()
