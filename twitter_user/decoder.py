from json import loads, dump
from brotli import decompress

testNum = 0
def encodingMess(data, debug=False):
    global testNum
    parsed = None
    try:
        # IS UTF-8
        parsed        = loads(data.decode('utf-8'))
    except:
        try:
            # IS BROTLI-COMPRESSED
            parsed    = loads(decompress(data))
        except Exception as e:
            print(e)
            print(data)
            return None
    
    # DEBUG UTIL FOR CHECKING RESPONSE INTEGRITY
    if debug:
        with open( str(testNum) + ".json", 'w+' ) as f:
            dump(parsed, f, indent=4)
            testNum += 1
    
    return parsed
