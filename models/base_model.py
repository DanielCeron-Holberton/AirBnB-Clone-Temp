#!/usr/bin/python3
"""Base class module"""


import uuid
from datetime import datetime
import models


class BaseModel():
    """Base Model class starts"""
    def __init__(self, *args, **kwargs):
        if args is not None:
            pass
        if kwargs and len(kwargs) != 0:
            del kwargs["__class__"]
            for key, value in kwargs.items():
                setattr(self, key, value)
            self.updated_at = datetime.strptime(self.updated_at, "%Y-%m-%dT%H:%M:%S.%f")
            self.created_at = datetime.strptime(self.created_at, "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()
    def __str__(self):
        return "[{s.__class__.__name__}] ({s.id}) {s.__dict__}".format(s=self)
    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()
    def to_dict(self):
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict.update({"created_at": self.created_at.isoformat()})
        new_dict.update({"updated_at": self.updated_at.isoformat()})
        return new_dict

