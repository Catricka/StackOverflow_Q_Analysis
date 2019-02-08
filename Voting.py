class Voting:
    def __init__(self, link):
        self.link = link

    def give_info(link):

        a2 = open('VotingInfo.txt', 'w')
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
                number += 1
                a2.write('====================  Details of Question number ')
                a2.write(str(number))
                a2.write(': ==================== ')
                a2.write('\n')

                a2.write('Tags = ')
                for item2 in item:
                    temptext = str(item2)

                    a2.write(temptext)
                    a2.write(',')

                a2.write('\n')
                a2.write('owner\'s info : ')
                a2.write('\n')
                a2.write('{')
                a2.write('\n')
                for k, v in tempdict.items():
                    # print(k, '=', v)
                    dicttext = k + '=' + str(v)

                    a2.write(dicttext)
                    a2.write('\n')

                a2.write('}')
                a2.write('\n')
                a2.write('is answered =')
                a2.write(str(booltemp))
                a2.write('\n')
                a2.write('views =')
                a2.write(str(inttemp))
                a2.write('\n')
                a2.write('score =')
                a2.write(str(inttemp2))
                a2.write('\n')
                a2.write('last_activity_date =')
                a2.write(str(inttemp3))
                a2.write('\n')
                a2.write('creation_date =')
                a2.write(str(inttemp4))
                a2.write('\n')
                a2.write('question_id =')
                a2.write(str(inttemp5))
                a2.write('\n')
                a2.write('link = ')
                a2.write(str(strtemp))
                a2.write('\n')
                a2.write('title = ')
                a2.write(str(strtemp1))
                a2.write('\n')
                a2.write('body =')
                a2.write(str(strtemp2))
                a2.write('\n')
            listtemp.clear()
            i = i + 1

        a2.close()