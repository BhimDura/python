import requests

class total:
    def __init__(self):
     self.url="https://foodmandu.com/webapi/api/v2/Product/GetVendorProductsBySubCategoryV2?VendorId={venid}&show="

    def scrape(self,venid):
       url = self.url.format(venid=venid)
       r = requests.get(url)
       data = r.json
       data = data[0]['items']
       for i in data:
          print("name:",i['name'], i['price'])
       return data
s=total()
s.scrape(844)
s.scrape(34)