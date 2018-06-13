

class Config(object):
  
  
    
  social_domains = ('buzzfeed.com','facebook.com','vk.com','pinterest.com','twitter.com','instagram.com','tumblr.com')
  isIgnoreSocial = True
  google_api_key = ''
  
  def __init__():
    pass
    
  
 
  def setIgnoreSocial(self,state):
    self.isIgnoreSocial = state
    
  
  def getIgnoreSocial(self):
    return self.isIgnoreSocial
    
  def getConfigFile(self):
    config_file = {}
    return config_file
    
    
  def setApiKey(self, key):
    self.google_api_key = key