import requests
from selectorlib import Extractor
config= {"temp": {"xpath": "/html/body/div[5]/main/article/section[1]/div[1]/div[2]"}}

class Temperature:

    def __init__(self,country,city):
        self.country=country.strip()
        self.city=city.strip()

    def build_url(self):
        country= self.country.replace(" ", "-")
        city= self.city.replace(" ", "-")
        return f"https://www.timeanddate.com/weather/{country}/{city}"

    def get_data(self,url):
        return requests.get(url=url).text

    def get_temperature(self):
        url= self.build_url()
        data= self.get_data(url=url)
        extractor = Extractor(config)
        value = extractor.extract(data)
        return float(value["temp"].replace(" °C", ""))
