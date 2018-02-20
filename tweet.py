import configparser
import twitter

def tweet(message):
  conf = configparser.ConfigParser()
  conf.read('config')
  tconf = conf['Twitter']

  auth = twitter.OAuth(
    consumer_key    = tconf['consumer_key'],
    consumer_secret = tconf['consumer_secret'],
    token           = tconf['token'],
    token_secret    = tconf['token_secret']
  )

  t = twitter.Twitter(auth = auth)
  t.statuses.update(status = message)

