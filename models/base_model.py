import uuid
from datetime import datetime


class BaseModel():

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at":
                    if v is str:
                        setattr(self, k, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, k ,v)
                if k == "updated_at":
                    if v is str:
                        setattr(self, k, datetime.strptime(v, '%Y-%m-%dT%H:%M:%S.%f'))
                    else:
                        setattr(self, k, v)
                if k != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        return("[<{}>] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ save the object with a new updated at date"""
        self.updated_at = datetime.now()

    def to_dict(self):
        my_dict = self.__dict__.copy()

        if "created_at" in my_dict:
            my_dict["created_at"] = self.created_at.isoformat()
        elif "updated_at" in my_dict:
            my_dict["updated_at"] = self.updated_at.isoformat()
        my_dict["__class__"] = self.__class__.__name__
        return my_dict



