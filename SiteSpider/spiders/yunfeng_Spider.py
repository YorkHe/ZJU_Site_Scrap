from scrapy.spider import Spider
from scrapy.selector import Selector
from SiteSpider.items import siteSpider



class ckcSpider(Spider):
	name = "yunfeng"
	allowed_domains =['zju.edu.cn','zjuckc.com']
	start_urls = ["http://yunfeng.zju.edu.cn/in/news.php?news_catalogId=10066","http://yunfeng.zju.edu.cn/in/news.php?news_catalogId=10067"]

	def parse(self, response):
		sel = Selector(response)
		items = []
		posts = sel.xpath('//div[@class="overflow"]/a/@href').extract()
		items.extend([self.make_requests_from_url("http://yunfeng.zju.edu.cn/in/news.php"+url).replace(callback = self.parse_post) for url in posts])
		#next_page = sel.xpath('//div[@class="cg-page"]/a/@href').extract()[-2]
		#items.append(self.make_requests_from_url("http://ckc.zju.edu.cn/office/"+next_page))
		return items


	def dfs(self,pointer,output):
		children = pointer.xpath('child::*')
		if self.istext(children):
			output.append(pointer.xpath('text()').extract())
		else:
			if children.xpath('text()') != []:
				output.append(children.xpath('text()').extract())
			for child in children:
				self.dfs(child, output)
				if child.extract()[1] != 's':
					output.append('\n')

	def istext(self,children):
		if (children == []):
			return True
		if (children.extract().count('<br>') == len(children.extract())):
			return True

	def parse_post(self, response):
		sel = Selector(response)
		item = siteSpider()
		item['link'] = unicode(response.url)
		item['title'] = sel.xpath('//h3/text()').extract()
		output = []
		contents = sel.xpath('//div[@class="fuk"]//text()')
		#self.dfs(contents, output)
		#print(output)
		output = contents.extract()
		out_string = ''
		continuity = False
		pre = ''
		for items in output:
			if (items == pre):
				if continuity == False:
					out_string = out_string + items
					continuity = True
			else:
				out_string = out_string + ''.join(items)
				continuity = False
				pre = out_string
		print (out_string)

		item['description'] = out_string

		return [item]
