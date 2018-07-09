# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html



from scrapy.exceptions import DropItem
import json
import codecs

class TutorialPipeline(object):
    
        
        
    def process_item(self, item, spider):

        with codecs.open('movie.json','a',encoding = 'utf-8') as f:

            line = json.dumps(dict(item),ensure_ascii = False) + '\n'
            f.write(line)
            
        return item

    def open_spider(self,spider):
        pass
    def close_spider(self,spider):
        pass

            
        
        
        
