#!/usr/local/bin/python
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from thread import MyThread, WebCrawler


  
if __name__ == "__main__":
  while 1:
    print('Welcome to the SEO broken link tool\n')
    print('select an option from the followings :\n')
    print('1/ Scan a single website for dead links\n')  
    print('2/ Crawl the web for broken links\n')
    print('3/ Exit\n ')
    choice = input('select an option:')
    
    if  1 <= int(choice) <=3:
      print(choice)
      if int(choice) == 3 :
        quit()
      elif int(choice) == 1 :
        thread1 = MyThread(name="1")
        thread1.start()
        print('ok')
      elif int(choice) == 2:
         web_crawler = WebCrawler()
    else :
      print('please try again')
    
    #process = CrawlerProcess(get_project_settings())

    #process.crawl('sou')
    #process.start()

