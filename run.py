#!/usr/local/bin/python

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from thread import MyThread, WebCrawler
from config import Config
import time
  
if __name__ == "__main__":
  while 1:
     
    config  = Config()
    config_file = config.getConfigFile()
    print('Welcome to the SEO broken link tool\n')
    print('select an option from the followings :\n')
    print('1/ Scan a single website for dead links\n')  
    print('2/ Crawl the web for broken links\n')
    print('3/ Configuration \n')
    print('4/ Exit\n ')
    choice = input('select an option:')
    
    if  1 <= int(choice) <=4:
      #print(choice)
      if int(choice) == 1 :
        
        while 1 :
          
               
              print('1/add website to the list\n')
              print('2/ run\n')
              print('3/ go back\n ')
              choice = input('select :\t')
              
              
              
              
              if int(choice) ==1 :
                pass
                '''
                if len(starting_urls)<config.getUrlLimit():
                  url = input('enter the website to crawl:\n')
                  starting_urls.append(url)
                  print('you have just added {} \n'.format(starting_urls[-1]))
                else :
                  print('you have reached the limit for one job\n')
                '''
                  
              elif int(choice) == 2 :
                 
                i = 1
                while i > 0 :
                  i+= -1
                  time.sleep(1)
                
                  print('crawling start in {}\n'.format(i))
                process = CrawlerProcess(get_project_settings())

                process.crawl('single_check')
                process.start()
                        
                
              elif int(choice)== 3:
                break
          
      elif int(choice) == 2 :
        #thread1 = MyThread(name="1", args=(config_file))
        #thread1.start()
        print('ok')
      elif int(choice) == 3:
        web_crawler = WebCrawler()
         
     
      elif int(choice) == 4 :
        quit()
          
    else :
      print('incorrect choice ; please try again!\n')
        
 