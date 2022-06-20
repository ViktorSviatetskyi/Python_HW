""" Используя json модуль необходимо сериализовать объект `user`
   и десериализовать из json обратно в инстанс класса User."""

from __future__ import annotations
import pickle
import json
from datetime import datetime
from typing import Optional


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return o.__dict__


class User:
    """Class for storing users."""

    def __init__(self, id_: int,
                 username: str,
                 email: str,
                 address: Address,
                 birthday: datetime,
                 phone: Optional[str] = None):
        self.id = id_
        self.username = username
        self.email = email
        self.address = address
        self.birthday = birthday
        self.phone = phone

    def __str__(self):
        return(f'id = {self.id}, username = {self.username}, email = {self.email}, address = {self.address}, '
               f'birthday = {self.birthday}, phone = {self.phone}')


class Address:
    """Class for storing user addresses."""

    def __init__(self, city: str, street: str, pin: int):
        self.city = city
        self.street = street
        self.pin = pin

    def __str__(self):
        return f'city = {self.city}, street = {self.street}, pin = {self.pin}'


if __name__ == "__main__":
    address = Address(city="Kharkiv", street="Velozavodskaya", pin=12345)
    user = User(
        id_=1,
        username="vlad123",
        email="vlad123@test.com",
        address=address,
        birthday=datetime(2000, 5, 11),
        phone="+380509845333"
    )

# для себе спробував pickle. Працює прикольно!
if __name__ == "__main__":
    print('PICKLE')
    print(f'          user = [{user}]')

    pickled_user = pickle.dumps(user)
    print(f'pickled_user =[{pickled_user}]')

    unpickled_user = pickle.loads(pickled_user)
    print(f'unpickled_user = [{unpickled_user}]\n\n')

# JSON, в цілому також норм, але pickle прикольніше
    print('JSON')
    serialized_user_json = json.dumps(user, cls=CustomJSONEncoder)
    print(f'  serialized_user_json = [{serialized_user_json}]')

    deserialized_user_json = json.loads(serialized_user_json)
    print(f'deserialized_user_json = [{deserialized_user_json}]')
