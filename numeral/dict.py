

class dict:
  def __init__(self):
    self._storage = { }

  # add a key value?  
  def add_pair(self, key, value):
    self[key] = value
    #return {key: value}?
  
  def get_value(self, key, value):
    if key in self:
      print(value)
    


