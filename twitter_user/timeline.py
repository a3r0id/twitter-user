from json import dumps

class Timeline(object):
    def __init__(self, obj):

        self.object  = obj['data']['user']['result']['timeline']['timeline']
        
        self.json    = dumps(self.object, indent=4)







        

        