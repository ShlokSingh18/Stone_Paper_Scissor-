from django.http import HttpResponse 
from  django.shortcuts  import render , redirect
import random
a = [-1,0,1]
dict1 = {-1:"STONE",0:"PAPER",1:"SCISSOR"}
def home(request):
    return render(request, 'home.html')
def round(request):
    if (request.POST.get('rounds') != None):
        r = int(float(request.POST.get('rounds')))
        request.session["rounds_left"]= r 
        request.session["csscore"]= 0
        request.session["ysscore"]= 0
        return render(request ,'play.html',{"round":request.session["rounds_left"]})
    else:
        return render(request,'select_rounds.html')
def checkroundwinner(request,com_choice,your_choice):
        result = ""
        if(com_choice == your_choice):
            result = "draw"
            return result
        else:
            if(com_choice == -1 and your_choice  == 0):
                result = "you win"
                request.session["ysscore"] += 1
                return result
            elif(com_choice == 0 and  your_choice == 1):
                result = "you win"
                request.session["ysscore"] += 1
                return result
            elif(com_choice == 1 and  your_choice == -1):
                result = "you win"
                request.session["ysscore"] += 1
                return result
            else:
                result="computr wins"
                request.session["csscore"] += 1
                return result
def checkfinalwinner(request):
    if(request.session["ysscore"] > request.session["csscore"]):
        finalresult = "you win"
    elif(request.session["ysscore"] == request.session["csscore"]):
        finalresult = "draw"
    else:
        finalresult = "you lose"
    return finalresult
def result(request):
    finalresult = checkfinalwinner(request)
    return render(request ,'result.html', {"result": finalresult , "yscore": request.session["ysscore"] , "cscore" : request.session["csscore"]})
def play(request ):
    if(request.session["rounds_left"] > 1):
        request.session["rounds_left"] -= 1
        com_choice = random.choice(a)
        your_choice = int(float(request.POST.get('choice')))
        result = checkroundwinner(request,com_choice,your_choice)
        return render(request , 'play.html',{"result": result , "com_choice": dict1[com_choice] , "your_choice": dict1[your_choice] , "yscore": request.session["ysscore"] , "cscore": request.session["csscore"] , "round":request.session["rounds_left"],"finalresult": "" })    
    elif(request.session["rounds_left"] == 1):
        request.session["rounds_left"] -= 1
        com_choice = random.choice(a)
        your_choice = int(float(request.POST.get('choice')))
        result = checkroundwinner(request,com_choice,your_choice)
        return render(request , 'play.html' ,{"result": result ,"com_choice": dict1[com_choice] , "your_choice": dict1[your_choice] ,"yscore": request.session["ysscore"] , "cscore" : request.session["csscore"],"finalresult":"view result" , "round":"finish"})
    else:
        finalresult = checkfinalwinner(request)
        return redirect("result")