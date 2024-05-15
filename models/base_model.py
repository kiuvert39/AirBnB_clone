from uuid import uuid4
from datetime import datetime


class BaseModel:

    def __init__(self, *args, **kwargs) -> None:
        time_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for k, v in kwargs.items():
                if k == '__class__':
                    continue
                elif k == 'created_at' or k == 'updated_at':
                    setattr(self, k, datetime.strptime(v, time_format))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        '''this method save data to a json file'''
        self.updated_at = datetime.now()

    def to_dict(self):
        json = self.__dict__
        json['__class__'] = self.__class__.__name__
        json['created_at'] = json['created_at'].isoformat()
        json['updated_at'] = json['updated_at'].isoformat()

        return json
