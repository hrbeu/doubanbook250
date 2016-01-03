#-*-coding:utf-8-*-
from scrapy.selector import Selector
#from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.spiders import CrawlSpider,Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from doubanbook250.items import Doubanbook250Item
from bs4 import BeautifulSoup
from scrapy.utils.response import get_base_url


class BookSpider(CrawlSpider):
	
	name="doubanbook250"
	allowed_domains=["book.douban.com"]
	start_urls=["http://book.douban.com/top250"]
	#定义爬取URL的规则,并指定回调函数
	rules=[
                #注意:url中的问号前一定加"\"转义;没有callback意味着默认follow=False
                Rule(LinkExtractor(allow=(r'http://book.douban.com/top250\?start=\d+')),follow=True),
                Rule(LinkExtractor(allow=(r'http://book.douban.com/subject/\d+')),follow=False,callback="parse_item"),
	]
        #定义回调函数
	def parse_item(self,response):
#       response.selector.xpath()
                print get_base_url(response)
		sel=Selector(response=response)
		item=Doubanbook250Item()
                item['name']=sel.xpath("//*[@id='wrapper']/h1/span/text()").extract()[0]
		#item['year']=sel.xpath("//*[@id='info']/text()[2]").extract()[0]
                soup=BeautifulSoup(response.body)
                #使用BeautifulSoup提取不在标签内的出版年数据(但是在输出中会报错） 
                #item['year']=soup.find(text=u'出版年:').next
                #也可以用xpath抓取
                item['year']=sel.xpath(u"//span[contains(./text(),'出版年:')]/following::text()[1]").extract()[0]
                #或者不使用conains()函数
                #item['year']=sel.xpath(u"//span[./text()='出版年:')]/following::text()[1]").extract()
		item['author']=sel.xpath("//*[@id='info']/span/a/text()").extract()[0]
#		return item
                print get_base_url(response)+ "********\n"
                print item
		yield item
