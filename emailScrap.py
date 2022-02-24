import re
from collections import Counter
import json


with open ('websiteData.txt' , encoding = 'utf-8') as f:
    f_contents = f.read()

    #finding wheather the email is human or non human
    def email_type(contents):
        human_email = re.findall('\S+\S\.\S+@+\S+', contents)  #names separated by .

        emails = re.findall('[a-z0-9\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', contents)

        non_human_emails = []
        for i in emails:
            names = i.split('@')[0]
            if len(names)<8:
                non_human_emails.append(i)
            else:
                human_email.append(i)

        return (human_email , non_human_emails)

     #making it a dictionary
    def make_a_dict(count , nature):
        empty = []
        for key,value in count.items():
                r = (key , 'Occurance' , value , 'Email Type' , nature)
                t = list(r)
                empty.append(t)

        result1 = dict()

        for key, key1 , value1 , key2 ,value2 in empty:
            result1.setdefault(key , {}).update({key1:value1 , key2:value2})
        return (result1)


    types = email_type(f_contents)


    human_email = types[0]
    count1= Counter(human_email)

    nonhuman_email = types[1]
    count2= Counter(nonhuman_email)



    dict1 = make_a_dict(count1 , 'Human')

    dict2 = make_a_dict(count2 , 'Non Human')

    dict1.update(dict2)

    with open('result.json' , 'w') as outfile:
        json.dump(dict1 , outfile)








