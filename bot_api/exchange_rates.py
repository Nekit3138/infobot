import requests
from bs4 import BeautifulSoup


def rate():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    dollar_to_rub = requests.get('https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&aqs=chrome.0.69i59j0j0i395l2j0i20i263i395j0i395j69i61l2.2863j1j9&sourceid=chrome&ie=UTF-8', headers=headers).content
    euro_to_rub = requests.get('https://www.google.com/search?sxsrf=ALeKk00F_IkJtSc54A72OzLhrK8WXCDJeg%3A1611709487673&ei=L7wQYKPFKMTmrgT2z6WIBQ&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQAzIJCCMQJxBGEIICMgIIADICCAAyAggAMgIIADIFCAAQywEyAggAMgIIADICCAAyAggAOgQIABBHOgQIIxAnOgQIABBDOgcIABAUEIcCUPYGWMsNYJkPaABwAngAgAF8iAGSBZIBAzAuNpgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab&ved=0ahUKEwjjmPnb9bruAhVEs4sKHfZnCVEQ4dUDCA0&uact=5', headers=headers).content
    euro_to_dollar = requests.get('https://www.google.com/search?sxsrf=ALeKk02q_6UWJOyyRPzLUtmbRYh7qLxJDQ%3A1611709349731&ei=pbsQYPeRLOSWjgb8o4nQCQ&q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1%83&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B4%D0%BE%D0%BB&gs_lcp=CgZwc3ktYWIQAxgAMgcIABBGEIICMgIIADICCAAyAggAMgUIABDLATIFCAAQywEyAggAMgIIADICCAAyAggAOgQIABBHUM25AViNwgFg5csBaAFwA3gAgAFqiAGDA5IBAzIuMpgBAKABAaoBB2d3cy13aXrIAQjAAQE&sclient=psy-ab', headers=headers).content
    _vals = [dollar_to_rub, euro_to_rub, euro_to_dollar]
    _attrs = {'class': 'DFlfde', 'class': 'SwHCTb', 'data-precision': 2}
    vals = []
    for i in range(3):
        vals.append(BeautifulSoup(_vals[i], 'html.parser').find(attrs=_attrs).text)
    names = ['dollar_to_rub', 'euro_to_rub', 'euro_to_dollar']
    return dict(zip(names, vals))