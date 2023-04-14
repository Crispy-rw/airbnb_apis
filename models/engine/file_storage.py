import os
import json
from models.base_model import BaseModel


class FileStorage:

    __file_path = "file.json"
    __objects = {}


    def all(self):
        return self.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + "."+ getattr(obj, "id")
        self.__objects[key] = obj

    def save(self):
        try:
            with open(self.__file_path, mode="w", encoding="utf-8") as f:
                my_dict = {}
                for k,v in self.__objects.items():
                    my_dict[k] = v.to_dict()

                f.write(json.dumps(my_dict))
        except Exception as e:
            print(e)
            pass

    def reload(self):
        try:
            if os.stat(self.__file_path).st_size > 0:
                with open(self.__file_path, mode="r") as f:
                    my_json = json.load(f)
                for k , v in my_json.items():
                    cls_name = v["__class__"]
                    obj = eval(cls_name)(**v)
                    self.new(obj)
        except FileNotFoundError:
            pass
