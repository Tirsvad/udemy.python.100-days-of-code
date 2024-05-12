from dataclasses import dataclass


@dataclass
class SettingsModel:
    language_to_learn: str


@dataclass
class LanguagesAvailableModel:
    languages: list[tuple[str, str]]

    def __init__(self):
        self.languages = []
        self.languages.append(('fr', 'French'))

    def get_languages_codes(self) -> list[str]:
        lst = [lst[0] for lst in self.languages]
        return lst

    @staticmethod
    def get_words_file_path(lang_code: str) -> str:
        return f"data/{lang_code}/words.csv"

    @staticmethod
    def get_words_to_learn_file_path(lang_code: str) -> str:
        return f"data/{lang_code}/words_to_learn.csv"

