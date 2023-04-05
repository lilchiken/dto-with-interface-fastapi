from requests import Response
from json import loads


class ResponseDTO:
    """Класс, с помощью которого мы превращаем Response в Data
    Transfer Object.

    Note:\n
    Конструктор класса сам из атрибута _response_json создаёт
    остальные атрибута класса. 

    Атрибуты:\n
    _response_json -- объект requests.Response.content\n
    Остальные атрибуты выходят из вышеупомянутого атрибута.

    Агрументы:\n
    response -- объект requests.Response
    """

    def __init__(self, response: Response) -> None:
        self._response_json = response.content
        self.__dict__ = loads(self._response_json)
