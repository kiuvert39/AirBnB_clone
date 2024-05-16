#!/usr/bin/python3
"""
This module defines an class variable called BaseModel, and will be
the base class of all the other classes in this project.

class
======
Basemodel


Methods
==========

...

Attributes
==========

...

"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ defines all common attributes/methods for other classes: """

    def __init__(self, *args, **kwargs) -> None:
        """ takes in all multiple parameters

        args:
            args: multiple none keyword argurments
            kwargs: multiple keywor arguments
        """
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
        """ Returns <class name> <self.id> <self.__dict__> """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """ updates the public instance attribute updated_at """

        '''this method save data to a json file'''
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/value of __dict__
        of instance """
        json = self.__dict__
        json['__class__'] = self.__class__.__name__
        json['created_at'] = json['created_at'].isoformat()
        json['updated_at'] = json['updated_at'].isoformat()

        return json
