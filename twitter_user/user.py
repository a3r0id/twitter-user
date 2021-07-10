from .timeline import Timeline
from .media    import Media

class User(object):
    def __init__(self, json, media, tweets):

        # MEDIA CLASS
        self.media                          = Media(media)

        # TIMELINE CLASS
        self.timeline                       = Timeline(tweets)

        # RAW JSON OBJECT - ROOT
        self.json                           = json['data']
        
        # RAW JSON OBJECT - USER
        self.user                           = self.json['user']

        # RAW JSON OBJECT - LEGACY
        self.legacy                         = self.user['legacy']

        # USER ID - STRING (Base64) representation of "User:<User.rest_id>"
        self.id                             = self.user['id']

        # USER ID - STRING
        self.rest_id                        = self.user['rest_id']

        # FAVORITES COUNT - INT
        self.favorites_count                = self.legacy['favourites_count']

        # FOLLOWERS COUNT - INT
        self.followers_count                = self.legacy['followers_count']
        
        # FOLLOWING COUNT - INT
        self.friends_count                  = self.legacy['friends_count']

        # CREATION DATE - UTC DATETIME STRING
        self.created_at                     = self.legacy['created_at']

        # AFFILIATES HIGHLIGHTED LABEL (?) - DICT
        self.affiliates_highlighted_label   = self.user['affiliates_highlighted_label']

        # HAS DEFAULT PROFILE - BOOL
        self.default_profile                = self.legacy['default_profile']

        # HAS DEFAULT PROFILE IMAGE - BOOL
        self.default_profile_image          = self.legacy['default_profile_image']

        # PROFILE DESCRIPTION - STRING
        self.description                    = self.legacy['description']

        # ENTITIES IN DESCRIPTION - DICT
        self.entities                       = self.legacy['entities']

        # "FAST" FOLLOWERS COUNT - INT
        self.fast_followers_count           = self.legacy['fast_followers_count']

        # HAS CUSTOM TIMELINES - BOOL 
        self.has_custom_timelines           = self.legacy['has_custom_timelines']

        # IS TRANSLATOR (?) - BOOL
        self.is_translator                  = self.legacy['is_translator']

        # AMOUNT OF STATUSES ON INITIAL API PULL (?) - INT 
        self.listed_count                   = self.legacy['listed_count']

        # LOCATION - STRING
        self.location                       = self.legacy['location']

        # TIMELINE MEDIA COUNT
        self.media_count                    = self.legacy['media_count']

        # NAME (<this>@screen_name)
        self.name                           = self.legacy['name']

        # NORMAL FOLLOWERS COUNT (?) - INT
        self.normal_followers_count         = self.legacy['normal_followers_count']

        # PINNED TWEETS (LIST OF STATUS IDS) - LIST
        self.pinned_tweet_ids_str           = self.legacy['pinned_tweet_ids_str']

        # PROFILE BANNER EXTENSIONS - DICT 
        self.profile_banner_extensions      = self.legacy['profile_banner_extensions']

        # PROFILE BANNER URL - STRING
        self.profile_banner_url             = self.legacy['profile_banner_url']

        # PROFILE IMAGE EXTENSIONS - DICT 
        self.profile_image_extensions       = self.legacy['profile_image_extensions']

        # PROFILE IMAGE (HTTPS) - STRING
        self.profile_image_url_https        = self.legacy['profile_image_url_https']

        # PROFILE INTERSTITIAL TYPE (?) - STRING
        self.profile_interstitial_type      = self.legacy['profile_interstitial_type']

        # IS PROTECTED - BOOL
        self.protected                      = self.legacy['protected']
        
        # SCREEN NAME (name@<this>) - STRING
        self.screen_name                    = self.legacy['screen_name']
        
        # STATUSES COUNT - INT
        self.statuses_count                 = self.legacy['statuses_count']
        
        # TRANSLATOR TYPE - STRING
        self.translator_type                = self.legacy['translator_type']

        # USERS WEBSITE (URL) - STRING
        self.url                            = self.legacy['url']

        # IS VERIFIED - BOOL
        self.verified                       = self.legacy['verified']

        # COUNTRIES THAT HAVE WITHELD THIS ACCOUNT - LIST 
        self.withheld_in_countries          = self.legacy['withheld_in_countries']
        
        # LEGACY EXTENDED PROFILE - DICT
        self.legacy_extended_profile        = self.user['legacy_extended_profile']
        
        # IS PROFILE TRANSLATABLE - BOOL
        self.is_profile_translatable        = self.user['is_profile_translatable']