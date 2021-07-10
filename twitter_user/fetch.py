from .user    import User
from .decoder import encodingMess


# __FETCH_METHOD 
def fetchUser(self, screen_name):

    # ADD SCREEN NAME TO OBJECT INSTANCE
    self.screen_name = screen_name

    # HOIST A VARIABLE FOR THE RAW DATA
    self.data     = None
    self.media    = None
    self.timeline = None

    # LIMIT SELENIUMWIRE'S STORED REQUESTS TO JUST TWITTER DOMAINS
    self.driver.scopes = [
        '.*twitter.*'
    ]

    # INSTRUCT THE DRIVER TO NAVIGATE TO THE URL
    retries = 0
    while 1:
        
        try:
            self.driver.get("https://twitter.com/" + self.screen_name)
            break
        except Exception as f:
            print("Warning: " + f)
            retries += 1

        if (retries > self.allowed_connection_retries):
            raise RuntimeError('Exceeded retries allowed!')

    foundItems = [0, 0, 0]
    tries = 0
    while 1:

        if tries > self.allowed_parsing_retries:
            raise RuntimeError("Exceeded retries allowed!")

        # SERCH FOR A REQUEST TO TWITTERS GRAPHQL API
        for request in self.driver.requests:

            if request.response:

                if request.response.status_code == 200 and 'graphql/' in request.url:

                    # MAKING USE OF THE "UserByScreenNameWithoutResults" ENDPOINT
                    if '/UserByScreenNameWithoutResults' in request.url:
                        if not foundItems[0]:
                            self.data     = encodingMess(request.response.body)
                            foundItems[0] = 1
                            
                            if not self.data:
                                # FATALLY RETURN NONETYPE AS NO USER DATA WAS FOUND IN REQUESTS
                                raise ValueError("""

                                A valid API request was not found; Couln't fetch User.
                                There can be a number of causes for this including but not limited to:
                                
                                > Network Error

                                > Encoding Error

                                > Rate-Limiting/Anti-Bot Measures Taken By Twitter
                                
                                """)

                    # MAKING USE OF THE "UserTweets" ENDPOINT
                    elif 'UserTweets' in request.url:
                        if not foundItems[1]:
                            self.timeline = encodingMess(request.response.body)
                            foundItems[1] = 1

                    # MAKING USE OF THE "UserMedia" ENDPOINT
                    elif '/UserMedia' in request.url:
                        if not foundItems[2]:
                            self.media    = encodingMess(request.response.body)
                            foundItems[2] = 1

        if (sum(foundItems) == 3):
            break

        tries += 1

    
    # CLEAR THE DRIVERS REQUESTS
    del self.driver.requests

    # EITHER WE DID NOT FIND A VALID USER OR THERE WAS AN ERROR
    if not self.data:
        return None
    
    # SINCE `self.user` IS POPULATED WE CAN ASSUME THAT WE HAVE A VALID USER DATA OBJECT FROM TWITTER,
    # PASS OUR RAW USER-DATA OBJECT TO OUR USER OBJECT SO WE CAN CONVENIENTLY ACCESS THE USERS ATTRIBUTES
    return User(self.data, self.media, self.timeline)
    