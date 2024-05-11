from dataclasses import dataclass


@dataclass
class DataApproachModel:
    webpage: str
    username: str
    password: str

    @staticmethod
    def from_dict(obj: dict) -> 'DataApproachModel':
        """
        populate values from obj: dict

        :param obj: convert dictionary to DataModel
        :return:
        """
        webpage = str(obj.get("webpage"))
        username = str(obj.get("username"))
        password = str(obj.get("password"))
        return DataApproachModel(webpage=webpage, username=username, password=password)
