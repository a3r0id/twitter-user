from twitter_user import TwitterUser
from datetime import datetime

# Initialize the Driver
twitterUser = TwitterUser()




# Testing w/ my profile
me = twitterUser.fetchUser("hostinfodev")

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
jack = twitterUser.fetchUser("hostinfodev")

print(jack.name, "@", jack.screen_name)

print(jack.timeline.json)

print(jack.media.json)
