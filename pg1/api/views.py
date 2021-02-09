from django.shortcuts import render
from .models import DATA
from collections import Counter
from rest_framework.response import Response
import urllib
import requests
from six.moves.urllib.request import urlopen
import requests
import justext
from nltk.corpus import stopwords
import json
import ast 



def frequency(request):
    return render(request, 'frequency.html')


def result(request):
    if request.method=='POST':
        name1= request.POST.get('name', '')
        try:            
            pre=DATA.objects.get(url=name1)
            res = eval(pre.name)  
            return render(request, 'frequency.html',{'names':res.items()})
        except:
            
            str=''
            response = requests.get(name1)
            paragraphs = justext.justext(response.content, justext.get_stoplist("English"))
            for paragraph in paragraphs:
                str=str+paragraph.text    
                
            lst = str.split()
            deli = ['0','1','2','3','4','5','6','7','8','9','\n',';' ,',','.', '-','+','{', '}', '[', ']','/','@', '#','~', '$', '%', '^', '&', '(', ')','_', '=', ':', '!', "*", '<', '>', '\ ','()']
            comman_word = ['and','any','the','is','her','a', 'during', 'among', 'thereafter', 'only', 'hers', 'in', 'none', 'with', 'un', 'put', 'hence', 'each', 'would', 'have', 'to', 'itself', 'that', 'seeming', 'hereupon', 'someone', 'eight', 'she', 'forty', 'much', 'throughout', 'less', 'was', 'interest', 'elsewhere', 'already', 'whatever', 'or', 'seem', 'fire', 'however', 'keep', 'detail', 'both', 'yourselves', 'indeed', 'enough', 'too', 'us', 'wherein', 'himself', 'behind', 'everything', 'part', 'made', 'thereupon', 'for', 'nor', 'before', 'front', 'sincere', 'really', 'than', 'alone', 'doing', 'amongst', 'across', 'him', 'another', 'some', 'whoever', 'four', 'other', 'latterly', 'off', 'sometime', 'above', 'often', 'herein', 'am', 'whereby', 'although', 'who', 'should', 'amount', 'anyway', 'else', 'upon', 'this', 'when', 'we', 'few', 'anywhere', 'will', 'though', 'being', 'fill', 'used', 'full', 'thru', 'call', 'whereafter', 'various', 'has', 'same', 'former', 'whereas', 'what', 'had', 'mostly', 'onto', 'go', 'could', 'yourself', 'meanwhile', 'beyond', 'beside', 'ours', 'side', 'our', 'five', 'nobody', 'herself', 'is', 'ever', 'they', 'here', 'eleven', 'fifty', 'therefore', 'nothing', 'not', 'mill', 'without', 'whence', 'get', 'whither', 'then', 'no', 'own', 'many', 'anything', 'etc', 'make', 'from', 'against', 'ltd', 'next', 'afterwards', 'unless', 'while', 'thin', 'beforehand', 'by', 'amoungst', 'you', 'third', 'as', 'those', 'done', 'becoming', 'say', 'either', 'doesn', 'twenty', 'his', 'yet', 'latter', 'somehow', 'are', 'these', 'mine', 'under', 'take', 'whose', 'others', 'over', 'perhaps', 'thence', 'does', 'where', 'two', 'always', 'your', 'wherever', 'became', 'which', 'about', 'but', 'towards', 'still', 'rather', 'quite', 'whether', 'somewhere', 'might', 'do', 'bottom', 'until', 'km', 'yours', 'serious', 'find', 'please', 'hasnt', 'otherwise', 'six', 'toward', 'sometimes', 'of', 'fifteen', 'eg', 'just', 'a', 'me', 'describe', 'why', 'an', 'and', 'may', 'within', 'kg', 'con', 're', 'nevertheless', 'through', 'very', 'anyhow', 'down', 'nowhere', 'now', 'it', 'cant', 'de', 'move', 'hereby', 'how', 'found', 'whom', 'were', 'together', 'again', 'moreover', 'first', 'never', 'below', 'between', 'computer', 'ten', 'into', 'see', 'everywhere', 'there', 'neither', 'every', 'couldnt', 'up', 'several', 'the', 'i', 'becomes', 'don', 'ie', 'been', 'whereupon', 'seemed', 'most', 'noone', 'whole', 'must', 'cannot', 'per', 'my', 'thereby', 'so', 'he', 'name', 'co', 'its', 'everyone', 'if', 'become', 'thick', 'thus', 'regarding', 'didn', 'give', 'all', 'show', 'any', 'using', 'on', 'further', 'around', 'back', 'least', 'since', 'anyone', 'once', 'can', 'bill', 'hereafter', 'be', 'seems', 'their', 'myself', 'nine', 'also', 'system', 'at', 'more', 'out', 'twelve', 'therein', 'almost', 'except', 'last', 'did', 'something', 'besides', 'via', 'whenever', 'formerly', 'cry', 'one', 'hundred', 'sixty', 'after', 'well', 'them', 'namely', 'empty', 'three', 'even', 'along', 'because', 'ourselves', 'such', 'top', 'due', 'inc', 'themselves']
                
            fre=Counter(lst)
            dict={}
            dict1=[]
            if len(fre)<= 10 :
                for letter, count in fre.most_common(len(fre)):
                    if letter not in deli and letter not in comman_word:
                        dict[letter]=[count]   

                data=DATA(name=dict,
                            url=name1)
                data.save()
                id =DATA.objects.get(url=name1)
                return render(request, 'frequency.html',{'names':dict.items()})
                    
            else:
                k=0
                for letter, count in fre.most_common(len(fre)):
                    if letter not in deli and letter not in comman_word:
                        dict[letter]=count               
                        if k<=9:
                            k+=1
                        else:
                            break
                    
                data=DATA(name=dict, url=name1)
                print(dict)
                data.save()
                id =DATA.objects.get(url=name1)
                return render(request, 'frequency.html',{'names':dict.items()})
            return render(request, 'frequency.html',{'names':dict.items()})
                
