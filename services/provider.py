from .Iprovider import Abs_Provider_Entity

class Provider(Abs_Provider_Entity):
    _url = None
    _imageUrl = None
    _name = None

    def setUrl(self, url):
        self._url = url
    
    def  setImageUrl(self, imageUrl):
        self._imageUrl = imageUrl
    
    def  setName(self, name):
        self._name = name

    def getUrl(self):
        return self._url

    def getImageUrl(self):
        return self._imageUrl
    
    def getName(self):
        return self._name
