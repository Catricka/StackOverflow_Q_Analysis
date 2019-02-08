import requests
import json
import webbrowser
import Creation as cr
import Voting as vo
import sys
tag=input("Please Enter the Keyword:")
if tag == "":
    print("Enter valid tag")
else:
    api_url = "https://api.stackexchange.com/2.2/questions?order=desc&pagesize=10&sort=creation&tagged={}&filter=withbody&site=stackoverflow".format(
        tag)
    api_url2 = "https://api.stackexchange.com/2.2/questions?order=desc&pagesize=10&sort=votes&tagged={}&filter=withbody&site=stackoverflow".format(
        tag)
    r = requests.get(api_url).json()
    r2 = requests.get(api_url2).json()
    i = 0
    c = open('CreationTitles.txt', 'w')
    numberc = 0
    numberd = 0
    while (i < len(r['items'])):
        numberc+=1
        links = (r['items'][i]['title'])
        c.write(str(numberc))
        c.write(": ")
        c.write(links)
        c.write('\n')
        i = i + 1
    c.close()
    j = 0
    d = open('VotingTitles.txt', 'w')
    while (j < len(r2['items'])):
        numberd+=1
        links2 = (r2['items'][j]['title'])
        d.write(str(numberd))
        d.write(": ")
        d.write(links2)
        d.write('\n')
        j = j + 1
    d.close()
    if (len(r['items']) == 0 or r is None):
        print("Nothing found")
    else:
        cr.Creation.give_info(r)
        vo.Voting.give_info(r2)
webbrowser.open_new_tab('index.html')
