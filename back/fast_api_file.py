from first_page_analysis import *
from parse_youtube_search import *

channel_name1 = 'chestniyblog'
channel_name2 = 'nickiminaj'
channel_name3 = 'DontTellComedy'
channel_name4 = 'python228dlapypsikov'
channel_name5 = 'tkhirianov'

keys = general_func(channel_name1)
final_json = general_YT(search_query=keys, quantity=5)
print(final_json)