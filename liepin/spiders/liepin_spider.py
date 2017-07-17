import scrapy
from scrapy import Request
from .make_start_urls import start_request
from ..items import LiepinItem


class MySpider(scrapy.Spider):
    name = 'liepin'
    allowed_domains = ['m.liepin.com']

    def start_requests(self):
        links = start_request()
        for link in links:
            yield Request(link, callback=self.parse_page)

    def parse_page(self, response):
        base_url = 'https://m.liepin.com'
        data = {}
        try:
            industry_chosen = response.xpath('/html/body/div[3]/section[1]/form/div[2]/div/div[2]/a/span/text()').extract()[0]
            data['belong'] = industry_chosen
        except:
            data['belong'] = ''
        job_links = response.xpath('/html/body/div[3]/section[2]/div/div/div[1]/div/dl/dd/ul/li[1]/a/@href').extract()
        for job_link in job_links:
            if len(job_link) <=30:
                continue
            yield Request(job_link, meta=data, callback=self.parse_item)

        if len(response.xpath('/html/body/div[3]/section[2]/div/div/div[2]/p[3]/a/@href').extract()) != 0:
            next_page_url = response.xpath('/html/body/div[3]/section[2]/div/div/div[2]/p[3]/a/@href').extract()[0]
            return Request(base_url+next_page_url,callback=self.parse_page)

    def parse_item(self, response):
        self.logger.info('已抓取到页面 %s,页面大小 %s', response.url, str(len(response.text)))
        item = LiepinItem()
        try:
            item['belong'] = response.meta['belong']
        except:
            item['belong'] = ''
        try:
            item['job'] = response.xpath('/html/body/div[1]/div[2]/section[1]/div[1]/span/text()').extract()[0]
        except:
            item['job'] = ''
        try:
            item['edu'] = response.xpath('/html/body/div[1]/div[2]/section[1]/div[2]/p[3]/text()').extract()[0]
        except:
            item['edu'] = ''
        try:
            item['company'] = response.xpath('/html/body/div[1]/div[2]/section[2]/div[1]/div/h2/text()').extract()[0].replace('\n','').replace('\t','').replace(' ','')
        except:
            item['company'] = ''
        try:
            item['salary'] = response.xpath('/html/body/div[1]/div[2]/section[1]/div[1]/p/text()').extract()[0]
        except:
            item['salary'] = ''
        try:
            item['experience'] = response.xpath('/html/body/div[1]/div[2]/section[1]/div[2]/p[2]/text()').extract()[0]
        except:
            item['experience'] = ''
        try:
            item['address'] = response.xpath('/html/body/div[1]/div[2]/section[1]/div[2]/p[1]/a/text()').extract()[0]
        except:
            item['address'] = ''
        try:
            item['address_detail'] = response.xpath('/html/body/div[1]/div[2]/section[2]/div[2]/@data-address').extract()[0]
        except:
            item['address_detail'] = ''
        # try:
        #     item['description'] = response.xpath('/html/body/div[1]/div[2]/section[3]/div/article[1]').extract().replace('<article class="content-word">','').replace('</article>','').replace('</p>', '').replace('\r', '').replace('\n', '').replace(' ', '').replace('</div>', '').replace('<divclass="about-main">','')
        # except:
        #     item['description'] = ''
        try:
            item['age'] = response.xpath('/html/body/div[1]/div[2]/section[3]/div/article[2]/ul/li[1]/span/text()').extract()[0]
        except:
            item['age'] = ''
        return item