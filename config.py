

class Config(object):
  
  
    
  social_domains = ('buzzfeed.com','facebook.com','vk.com','pinterest.com','twitter.com','instagram.com','tumblr.com')

  
  def __init__(self):
  
      
    with open('websites.txt','r') as file :
          starting_urls = file.readlines()
           
    self.config_file = {'urls_limit' : 5, 'isIgnoreSocial': True, 'starting_websites':starting_urls}
  
  def getStartingUrls(self):
    return self.config_file['starting_websites'] 
  def setIgnoreSocial(self,state):
    self.config_file['isIgnoreSocial'] = state
    
  
  def getIgnoreSocial(self):
    return self.config_file['isIgnoreSocial']
    
  def getConfigFile(self):
   
    return self.config_file
    
    
  def getUrlLimit(self):
    return self.config_file['urls_limit']    
    
  def setUrlLimit(self, limit):
    self.config_file['urls_limit']  = limit