import re
def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext
class Creation:

    def __init__(self,link):
        self.link=link

    def give_info(link):
        a = open('CreationInfo.txt', 'w')
        i = 0
        listtemp = list()
        tempdict = dict()
        number = 0
        while (i < len(link['items'])):
            # print(link['items'][i]['link'])
            listtemp.append(link['items'][i]['tags'])
            tempdict.update(link['items'][i]['owner'])
            booltemp = (link['items'][i]['is_answered'])
            inttemp = (link['items'][i]['view_count'])
            inttemp2 = (link['items'][i]['score'])
            inttemp3 = (link['items'][i]['last_activity_date'])
            inttemp4 = (link['items'][i]['creation_date'])
            inttemp5 = (link['items'][i]['question_id'])
            strtemp = (link['items'][i]['link'])
            strtemp1 = (link['items'][i]['title'])
            strtemp2 = (link['items'][i]['body'])
            for item in listtemp:
                number +=1
                a.write('====================  Details of Question number ')
                a.write(str(number))
                a.write(': ====================')
                a.write('\n')


                a.write('Tags = ')
                for item2 in item:
                    temptext = str(item2)
                    a.write(temptext)
                    a.write(',')

                a.write('\n')
                a.write('owner\'s info : ')
                a.write('\n')
                a.write('{')
                a.write('\n')

                for k, v in tempdict.items():
                    # print(k, '=', v)
                    dicttext = k + '=' + str(v)
                    a.write(dicttext)
                    a.write('\n')

                a.write('}')
                a.write('\n')
                a.write('is answered =')
                a.write(str(booltemp))
                a.write('\n')
                a.write('views =')
                a.write(str(inttemp))
                a.write('\n')
                a.write('score =')
                a.write(str(inttemp2))
                a.write('\n')
                a.write('last_activity_date =')
                a.write(str(inttemp3))
                a.write('\n')
                a.write('creation_date =')
                a.write(str(inttemp4))
                a.write('\n')
                a.write('question_id =')
                a.write(str(inttemp5))
                a.write('\n')
                a.write('link = ')
                a.write(str(strtemp))
                a.write('\n')
                a.write('title = ')
                a.write(str(strtemp1))
                a.write('\n')
                a.write('body =')
                a.write(str(cleanhtml(strtemp2)))
                a.write('\n')

            listtemp.clear()
            i = i + 1
        a.close()
