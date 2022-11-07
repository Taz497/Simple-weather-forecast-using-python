#Made by Carnefix
#07/11/2022

#NOTE : it won't work for you if you don't change the "User-Agent"(line 13) to your's and make sure to replace the url(Line 11) to the one youre looking for!


from requests_html import HTMLSession

a = HTMLSession()

#weather from dhaka
url = f"https://www.accuweather.com/en/bd/dhaka/28143/current-weather/28143"

#Search for your User agent, then paste it here
b = a.get(url,headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; rv:106.0) Gecko/20100101 Firefox/106.0"})

temp = b.html.find("div.display-temp",first=True).text

print("Today's weather " + temp)