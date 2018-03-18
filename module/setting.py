#coding: UTF-8
import yaml

class Yam:
  def __init__(self):
    self.fileName = "/etc/notifier/kindle.yml"
    self.obj = None

  def __Read(self):
    with open(self.fileName) as f:
      return yaml.load(f)

  def __Write(self, value):
    if value is not None:
      with open(self.fileName, "w") as f:
        yaml.dump(value, f)

  def Get(self):
    if self.obj is None:
      self.obj = self.__Read()

    data = {}
    for user in self.obj["kindle"]:
      name = user["name"]
      data[name] = []
      for item in user["url"]:
        data[name].append({"url": item[0], "sale": item[1]})

    return data

  def Save(self):
    self.__Write(self.obj)

  def Add(self, name, url, sale):
    if self.obj is None:
      self.obj = self.__Read()

    kindle = self.obj["kindle"]
    adduser = None
    for user in kindle:
      if user["name"] == name:
        adduser = user
        break;

    if adduser is None:
      adduser = {}
      adduser["name"] = name
      adduser["url"] = []
      kindle.append(adduser)

    adduser["url"].append([url, sale])
    self.__Write(self.obj)

    
