import uuid
from datetime import datetime
import models




class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            for k, v in kwargs.items():
                if k != "__class__":
                    if k in ["created_at", "updated_at"]:
                        v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)


    def save(self):
        self.updated_at = datetime.utcnow()
        models.storage.save()



    def __str__(self):
        """String representation of this class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def to_dict(self):
        """Dictionarry representation of a class"""
        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")
        my_dict["updated_at"] = my_dict["updated_at"].strftime("%Y-%m-%dT%H:%M:%S.%f")

        return my_dict
