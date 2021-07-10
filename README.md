# twitter-user

 A light & organized Python module built with the sole purpose of extracting a Twitter user-object while conforming to Tweepy standards, all without using Twitter's authenticated API.

# Examples

## Invoke The API
```python
from twitter_user import TwitterUser

API = TwitterUser()
```

## Fetch A User
```python
user = API.fetchUser("Sethrogen")
```

## Example - Fetch A User-Object
```python
from twitter_user import TwitterUser

API  = TwitterUser()

seth = API.fetchUser("Sethrogen")


print("User's screen appearance is \"%s\"" % seth.name + "@" + seth.screen_name )

print("User's ID is %s" % seth.rest_id )

print("Favorited %s tweets" % seth.favorites_count )

print("Followed by %s users" % seth.followers_count )

print("Following %s users" % seth.friends_count )

print("Account was created %s days ago" % (datetime.now() - datetime.strptime(seth.created_at, "%a %b %d %H:%M:%S +0000 %Y")).days)

print("Account posts an average of %s tweets per day" % round(seth.statuses_count / (datetime.now() - datetime.strptime(seth.created_at, "%a %b %d %H:%M:%S +0000 %Y")).days ))

print("Account has posted a total of %s tweets" % seth.statuses_count)

print("Account Description: \n%s" % seth.description)
```


# Example - Back-To-Back Fetch
```python
from twitter_user import TwitterUser
from datetime import datetime

API = TwitterUser()





# Testing w/ my profile
me = API.fetchUser("hostinfodev")

print("User's screen appearance is \"%s\"" % me.name + "@" + me.screen_name )

print("User's ID is %s" % me.rest_id )

print("Favorited %s tweets" % me.favorites_count )

print("Followed by %s users" % me.followers_count )

print("Following %s users" % me.friends_count )

print("Account was created %s days ago" % (datetime.now() - datetime.strptime(me.created_at, "%a %b %d %H:%M:%S +0000 %Y")).days)

print("Account posts an average of %s tweets per day" % round(me.statuses_count / (datetime.now() - datetime.strptime(me.created_at, "%a %b %d %H:%M:%S +0000 %Y")).days ))

print("Account has posted a total of %s tweets" % me.statuses_count)

print("Account Description: \n%s" % me.description)




# Testing w/ Jack's profile
jack = API.fetchUser("hostinfodev")

print(jack.name, "@", jack.screen_name)

print(jack.timeline.json)

print(jack.media.json)

```

------

# API Documentation

Notes:

> `User` is returned by calling `API.fetchUser(valid_screen_name)`.

> Passing an invalid username will result in `None` being returned by the `fetchUser` method.

## API.User

> `User.user` - (str) - Raw JSON of the User-Object.

> `User.rest_id` - (str) - User's ID.

> `User.id` - (str) - Base64 representation of `"User:<User.rest_id>"`.

> `User.favorites_count` - (int) - User's favorites count.

> `User.followers_count` - (int) - User's follower count.  

> `User.friends_count` - (int) - Amount of users that this user is following.  

> `User.created_at` - (str [utc datetime string]) - The creation date of user's profile, formatted in UTC as `"%a %b %d %H:%M:%S +0000 %Y"`.

> `User.default_profile` - (bool) - User has default profile.

> `User.default_profile_image` - (bool) - User has default profile image.

> `User.description` - (str) - User's profile description.

> `User.entities` - (dict) - Entities contained in user's description.

> `User.fast_followers_count` - (int) - User's fast followers count.

> `User.has_custom_timelines` - (int) - User has custom timelines (?).

> `User.location` - (str) - User's arbitrary location.

> `User.media_count` - (int) - Amount of media contained on user's overall timeline.

> `User.name` - (str) - User's provided name; Ex: `<this>@screen_name`.

> `User.screen_name` - (str) - Users screen name (handle); Ex: `name@<this>`.

> `User.pinned_tweet_ids_str` - (list) - List of IDs of user's pinned tweets. 

> `User.profile_banner_url` - (str) - URL to user's profile banner.

> `User.profile_image_url_https` - (str) - HTTPS version of user's profile image.

> `User.protected` - (bool) - Determines whether or not if user's tweets are protected.

> `User.statuses_count` - (bool) - Amount of overall statuses (Tweets) user has posted, "retweets" included.

> `User.translator_type` - (str) - Type of translation engine to be used (?).

> `User.url` - (str) - User's arbitrarily provided URL/website.

> `User.verified` - (bool) - Determines whether or not user is verified.

> `User.withheld_in_countries` - (list) - List of countries that user is withheld in. 

> `User.is_profile_translatable` - (bool) - Determines whether or not user's profile is translatable.

> `User.affiliates_highlighted_label` - (dict) - [To be determined] (?). 

> `User.legacy_extended_profile` - (dict) - [To be determined] (?).

> `User.profile_interstitial_type` - (str) - [To be determined] (?).

> `User.profile_image_extensions` - (dict) - [To be determined] (?).

> `User.profile_banner_extensions` - (dict) - [To be determined] (?).

> `User.normal_followers_count` - (int) - [To be determined] (?).

> `User.is_translator` - (bool) - [To be determined] (?).

> `User.listed_count` - (int) - [To be determined] (?).


## API.User.Media

> `User.Media.json` - (str) - Raw representation of media displayed on the user's timeline(profile).

> `User.Media.object` - (dict) - Dictionary representation of media displayed on the user's timeline(profile).

## API.User.Timeline

> `User.Timeline.json` - (str) - Raw representation of the recent statuses(Tweets) on the user's timeline(profile).

> `User.Timeline.object` - (dict) - Dictionary representation of the recent statuses(Tweets) on the user's timeline(profile).