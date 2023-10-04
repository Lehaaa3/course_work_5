import requests


class Employer:
    """Класс для получения информации о работодателе с помощью HeadHunter API"""

    url: str = 'https://api.hh.ru/employers'

    def __init__(self, url: str = url):
        """
        Инициализация класса Employer.

        :param url: URL для запросов к HeadHunter API.
        """
        self.url = url
        self.employer_id = None
        self.employer_name = None
        self.open_vacancies = None

    def get_employer_info(self, employer_name: str) -> list:
        """
        Поиск необходимой информации о Компании на HeadHunter API.

        :param employer_name: Название Компании для поиска
        :return: self.employer_id, self.employer_name, self.open_vacancies
        """
        params = {
            'text': employer_name,
            'per_page': 1,
            'only_with_vacancies': True
        }

        response = requests.get(url=self.url, params=params)
        response_json = response.json().get("items", [])
        self.employer_id = response_json[0]['id']
        self.employer_name = response_json[0]['name']
        self.open_vacancies = response_json[0]['open_vacancies']

        return self.employer_id, self.employer_name, self.open_vacancies
