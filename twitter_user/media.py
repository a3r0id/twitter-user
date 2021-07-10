from json import dumps

class Media(object):
    def __init__(self, obj):
        
        self.object  = obj['data']['user']['result']['timeline']['timeline']['instructions'][0]['entries']
        
        self.json    = dumps(self.object, indent=4)

        