
import json
import os
class Config(object):



  social_domains = ('buzzfeed.com','facebook.com','vk.com','pinterest.com','twitter.com','instagram.com','tumblr.com')


  def __init__(self):


    with open(os.path.dirname(os.path.realpath(__file__))+'/configs.json') as file:
                # self.config_file = ConfigObj(os.path.dirname(os.path.realpath(__file__))+'/configs.json')'config.json','r') as file :
        self.config_file = json.load(file)

    # self.config_file = {'urls_limit' : 5, 'isIgnoreSocial': True, 'starting_websites':starting_urls}

  def getStartingUrls(self):
      pass
      # return self.config_file['starting_websites']
  def setIgnoreSocial(self,state):
    self.config_file['ignore_social'] = state


  def getIgnoreSocial(self):
    return self.config_file['ignore_social']

  def getConfigFile(self):

    return self.config_file



  def getUrlLimit(self):
      pass
    # return self.config_file['urls_limit']

  def setUrlLimit(self, limit):
      pass
    # self.config_file['urls_limit']  = limit
