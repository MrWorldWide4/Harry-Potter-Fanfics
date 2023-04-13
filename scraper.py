from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
import time
from selenium.webdriver.common.keys import Keys
import pandas as pd


s = Service(r'C:/Program Files/Google/Chrome/Application/chromedriver.exe')
driver = webdriver.Chrome(service = s)

driver.get('https://archiveofourown.org/works/9146200?view_adult=true&view_full_work=true')
time.sleep(3)
driver.find_element("id", 'tos_agree').click()
driver.find_element("id", 'accept_tos').click()
time.sleep(2)


data = pd.read_csv('blacklinks.csv')
links = list(data['black links'])

new_data = []
c=0

for link in links[280:300]:

	link = link + '?view_adult=true&view_full_work=true'
	driver.get(link)
	ENTIRE_STORY = driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[3]').text[:50000]


	tuppy = (link, ENTIRE_STORY)
	new_data.append(tuppy)
	print(c, len(new_data[c][1]))
	# if len(ENTIRE_STORY) >= 10:
	# 	print('Got it', c, len(ENTIRE_STORY))  

	# if c == 5:
	# 	break
	c+=1

df = pd.DataFrame.from_records(new_data, columns =['link','ENTIRE_STORY'])
df.to_csv('black15.csv')

# print


# #2017
# # driver.get('https://archiveofourown.org/works/search?commit=Search&work_search%5Bquery%5D=Harry+Potter&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=2016&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=_score&work_search%5Bsort_direction%5D=desc')

# #2017
# # driver.get('https://archiveofourown.org/works/search?commit=Search&work_search%5Bquery%5D=Harry+Potter&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=2018&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=_score&work_search%5Bsort_direction%5D=desc')

# #2018
# # driver.get('https://archiveofourown.org/works/search?commit=Search&work_search%5Bquery%5D=Harry+Potter&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=2017&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=_score&work_search%5Bsort_direction%5D=desc')

# # trans
# # driver.get('https://archiveofourown.org/works/search?commit=Search&work_search%5Bquery%5D=Harry+Potter&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D=Trans&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=_score&work_search%5Bsort_direction%5D=desc')

# # link_add = '?view_adult=true&view_full_work=true'
# # driver.get('https://archiveofourown.org/works/37431790'+link_add)




# # #rating
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[1]/ul/li/a').text)

# # #category
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[3]/ul/li/a').text)

# # #relationships
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[5]/ul').text)

# # #characters
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[6]/ul').text)

# # #additional tags
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[7]/ul').text)

# # #language
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[8]').text)

# # #publish date
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[9]/dl/dd[1]').text)

# # #updated date
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[9]/dl/dd[2]').text)

# # #words
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[9]/dl/dd[3]').text)

# # #chapters
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[9]/dl/dd[4]').text)

# # #comments
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[9]/dl/dd[5]').text)

# # #kudos
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[9]/dl/dd[6]').text)

# # #bookmarks
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[9]/dl/dd[7]/a').text)

# # #hits
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[9]/dl/dd[8]').text)

# # #language
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/dl/dd[8]').text)

# # #publish date
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[1]/dl/dd[10]/dl/dd[1]').text)

# # #updated date
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[1]/dl/dd[10]/dl/dd[2]').text)

# # #words
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[1]/dl/dd[10]/dl/dd[3]').text)

# # #chapters
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[1]/dl/dd[10]/dl/dd[4]').text)

# # #comments
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[1]/dl/dd[10]/dl/dd[5]').text)

# # #kudos
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[1]/dl/dd[10]/dl/dd[6]').text)

# # #bookmarks
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[1]/dl/dd[10]/dl/dd[7]/a').text)

# # #hits
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[2]/div[1]/dl/dd[10]/dl/dd[8]').text)

# # #ENTIRE STORY
# # print(driver.find_element('xpath', '/html/body/div[1]/div[2]/div/div[3]/div[2]').text)




##links extractor
# page_num = 1
# link_num = 1
# all_links = []

# while True:

# 	# driver.get('https://archiveofourown.org/tags/Harry%20Potter%20-%20J*d*%20K*d*%20Rowling/works?page='+str(page_num))
	
# 	# driver.get('https://archiveofourown.org/works/search?commit=Search&page='+str(page_num)+'&work_search%5Bbookmarks_count%5D=&work_search%5Bcharacter_names%5D=&work_search%5Bcomments_count%5D=&work_search%5Bcomplete%5D=&work_search%5Bcreators%5D=&work_search%5Bcrossover%5D=&work_search%5Bfandom_names%5D=&work_search%5Bfreeform_names%5D=Trans&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bquery%5D=Harry+Potter&work_search%5Brating_ids%5D=&work_search%5Brelationship_names%5D=&work_search%5Brevised_at%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bsort_column%5D=_score&work_search%5Bsort_direction%5D=desc&work_search%5Btitle%5D=&work_search%5Bword_count%5D=')

# 	# driver.get('https://archiveofourown.org/works/search?commit=Search&page='+str(page_num)+'&work_search%5Bquery%5D=Harry+Potter&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=2014&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=_score&work_search%5Bsort_direction%5D=desc')	
# 	driver.get('https://archiveofourown.org/tags/Black%20Hermione%20Granger/works?page='+	str(page_num))
# 	elems = driver.find_elements('xpath', "//a[@href]")
# 	for elem in elems:
# 		link = elem.get_attribute("href")
# 		if 'https://archiveofourown.org/works/' in  link and link.count('/') == 4 and '?' not in link and 'kudos' not in link and 'search' not in link:
# 			all_links.append(link)
# 			print(link)
# 			link_num+=1
		
# 		# if(len(all_links) > 50):
# 		# 	break

# 	page_num+=1
# 	print("PAGE NUM", page_num	)