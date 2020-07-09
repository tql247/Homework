import scrapy
import os

class vnexpress_spider(scrapy.Spider):
    name = "vnexpress"
    
    start_urls = [
        'https://vnexpress.net/',
    ]

    def parse(self, response):
        if 'https://vnexpress.net/' in response.url:
            if '.html' not in response.url:
                link_list = response.css('a::attr(href)').getall()
                for link in link_list:
                    if link not in self.start_urls and 'https://vnexpress.net/' in link:
                        yield response.follow(link, callback=self.parse)
         
            else:
                # set file name
                page = response.url.split("/")[-1]
                filename = page.replace('html','txt')
                
                try:
                    # get info from web page here!
                    category = response.css('h4 a::text').get()
                    title = response.css('h1::text').get()[1:]
                    date = response.css('span.time::text').get()
                    content = response.css('p.description::text').get() + ''.join(response.css('article p.Normal::text').getall()[:-2])
                    author = response.css('p.Normal strong::text').getall()[-1]
                    # Below are others 
                except:
                    print('An error occur at %s!' %response.url)
                else:
                    try:
                        with open(os.path.join(os.getcwd(),'database', filename), 'wb') as f:
                            f.write(('Category: ' + category).encode('utf8'))
                            f.write(('\nTitle: ' + title).encode('utf8'))
                            f.write(('\nDate: ' + date).encode('utf8'))
                            f.write(('\nContent: ' + content).encode('utf8'))
                            f.write(('\nAuthor: ' + author).encode('utf8'))
                    except:
                        print('An error occur at: %s!' % response.url)
                        
                
                new_page = response.css('a::attr(href)').getall()
                if new_page is not None:
                    for next_page in new_page:
                        if next_page not in self.start_urls:
                            yield response.follow(next_page, callback=self.parse)
                    
