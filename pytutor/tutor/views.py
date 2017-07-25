from django.shortcuts import render
from .models import Question, Usr, TestCase, CourseMat
from django.http import JsonResponse
from django.http import HttpResponse
from hackerrank.HackerRankAPI import HackerRankAPI
import os.path
import sys
import webbrowser
from random import randint

import json

try:
    import apiai
except ImportError:
    sys.path.append(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
)


API_KEY = 'hackerrank|1138858-1148|4d580d3cd30003f57c52cd7807193b9e9fd6a6fd'  # Your API-KEY here

CLIENT_ACCESS_TOKEN = '4cae7e86f2534c1fa02529048a4466e8'



def index(request):
    i=0
    
    context = {'display':'Hey! They call me PyTutor! If it is Python that you wish to learn more about (the language and not the reptile), you have come to the'
                'right place!'
                'You can do several things using me as a guide to learning python, including ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::  '
                ' 1.Asking doubts ..................................................................'
                ' 2.Typing programs (see left) and checking their outputs ...................................................................'
                ' 3.Starting a theoretical course ................................................................................'
                ' 4.Asking for a random programming challenge ...........................................................................'
                
                ' Feel free to ask of me whatever you want!'}

    if(request.POST.get("sendmsg")):
        
        
        query = (request.POST.get('rep'))
        ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

        request1 = ai.text_request()

        request1.lang = 'en'  

        request1.query = query

        
        response = request1.getresponse()
        
        responsestr = response.read().decode('utf-8')
        
        response_obj = json.loads(responsestr)

        print(response_obj["result"]["fulfillment"]["speech"])
        
        context = {'display':response_obj["result"]["fulfillment"]["speech"]}

        intentnm = response_obj["result"]["metadata"]["intentName"]
        print(intentnm)

        if(intentnm=="questions"):
            query = response_obj["result"]["parameters"]["concepts"]+" in python"
            
            new=2
            tabUrl="http://google.com/?#q="
            
            webbrowser.open(tabUrl+query,new=new)
        if(intentnm=="coding"):
            q = Question.objects.get(pk=randint(1,len(Question.objects.all())))
            context = {'display':q.question_content}

        if(intentnm=="courseStart"):
            context={'display':'Enter your username'}

        if(intentnm=="Default Fallback Intent"):
            nm = query
            u = Usr.objects.get(name=nm)
            lvl = u.level
            course = CourseMat.objects.get(level=lvl)
            u.level+=1
            u.save()
            context = {'display':course.coursecontent}
        
        return render(request, 'tutor/index.htm',context)

    if(request.POST.get("tryprog")):
        source = (request.POST.get('progcode'))
        testcase = (request.POST.get('testcase'))

        compiler = HackerRankAPI(api_key = API_KEY)
        print('testcase = ',testcase,' program=', source)
        result = compiler.run({'source': source,
                               'lang':'python',
                               'testcases':[testcase]
                               })
        print(result)
        print('testcase = ',testcase,' program=', source)
        reply = result.output[0].strip()
        print(reply)
        
        
        context = {'display':reply}
        return render(request, 'tutor/index.htm',context)
        


        
    return render(request, 'tutor/index.htm',context)




