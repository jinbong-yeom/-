from bs4 import BeautifulSoup
import requests

from crawler_class import Bunjang, Danngn, Joongna


search_word = "노트북"
add_filter = ["노트북"]
sub_filter = ["게이밍"]

#당근마켓 검색
danngn = Danngn()
danngn.crawler_search(search_word, add_filter, sub_filter)
danngn.find_all()
danngn.serve_data()
print("당근")

#번개장터 검색
bunjang = Bunjang()
bunjang.crawler_search(search_word, add_filter, sub_filter)
bunjang.find_all()
bunjang.serve_data()
print("번개")

#중고나라 검색
joongna = Joongna()
joongna.crawler_search(search_word, add_filter, sub_filter)
joongna.find_all()
joongna.serve_data()
print("중고나라")