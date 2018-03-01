import configparser
import twitter
import os

def tweet(message):
  conf = configparser.ConfigParser()
  base = os.path.dirname(os.path.abspath(__file__))
  name = os.path.normpath(os.path.join(base, 'config'))
  conf.read(name)
  tconf = conf['Twitter']

  auth = twitter.OAuth(
    consumer_key    = tconf['consumer_key'],
    consumer_secret = tconf['consumer_secret'],
    token           = tconf['token'],
    token_secret    = tconf['token_secret']
  )

  t = twitter.Twitter(auth = auth)
  t.statuses.update(status = message)

