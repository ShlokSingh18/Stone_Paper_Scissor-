from django.http import HttpResponse 
from  django.shortcuts  import render
import random
a = [-1,0,1]
# dict2 = {"s":-1,"p":0,"sc":1}
dict1 = {-1:"STONE",0:"PAPER",1:"SCISSOR"}
r = 0

# print("USE THESE INITIALS FOR PLAYING :-\n1:['s' For STONE]\n2:['p' For PAPER]\n3:['sc' For SCISSOR]\n")

def home(request):
    return render(request, 'home.html')

def round(request):
   
    if (request.GET.get('rounds') != None):
        r = int(request.GET.get('rounds'))
        request.session["rounds_left"]= r 
        request.session["csscore"]= 0
        request.session["ysscore"]= 0
        return render(request ,'play.html',{"round":request.session["rounds_left"]})
        
    else:
        return render(request,'select_rounds.html')

def play(request ):
    request.session["rounds_left"] -= 1
   
    if(request.session["rounds_left"] > 0):
        com_choice = random.choice(a)
        your_choice = int(request.GET.get('choice'))
        
        
        if(com_choice == your_choice):
            result = "draw"
            return render(request , 'play.html',{"result": result , "com_choice": dict1[com_choice] , "your_choice": dict1[your_choice] , "yscore": request.session["ysscore"] , "cscore": request.session["csscore"] , "round":request.session["rounds_left"] })
        else:
            if(com_choice == -1 and your_choice  == 0):
                result = "you win"
                request.session["ysscore"] += 1
                return render(request , 'play.html',{"result": result , "com_choice": dict1[com_choice] , "your_choice": dict1[your_choice] , "yscore": request.session["ysscore"] , "cscore": request.session["csscore"] , "round":request.session["rounds_left"] })
                
            elif(com_choice == 0 and  your_choice == 1):
                result = "you win"
                request.session["ysscore"] += 1
                return render(request , 'play.html',{"result": result , "com_choice": dict1[com_choice] , "your_choice": dict1[your_choice] , "yscore": request.session["ysscore"] , "cscore": request.session["csscore"] , "round":request.session["rounds_left"] })
                
            elif(com_choice == 1 and  your_choice == -1):
                result = "you win"
                request.session["ysscore"] += 1
                return render(request , 'play.html',{"result": result , "com_choice": dict1[com_choice] , "your_choice": dict1[your_choice] , "yscore": request.session["ysscore"] , "cscore": request.session["csscore"] , "round":request.session["rounds_left"] })
                
            else:
                result="computr wins"
                request.session["csscore"] += 1
                return render(request , 'play.html',{"result": result , "com_choice": dict1[com_choice] , "your_choice": dict1[your_choice] , "yscore": request.session["ysscore"] , "cscore": request.session["csscore"] , "round":request.session["rounds_left"] })
        
    elif(request.session["rounds_left"] == 0):
        com_choice = random.choice(a)
        your_choice = int(request.GET.get('choice'))

        if(com_choice == your_choice):
                if(request.session["ysscore"]>request.session["csscore"]):
                    result = "you win the game"
                elif(request.session["ysscore"]==request.session["csscore"]):
                    result = "draw"
                else:
                    result = "you lose the game"
                return render(request , 'result.html',{"result": result , "com_choice": dict1[com_choice] , "your_choice": dict1[your_choice] , "yscore": request.session["ysscore"] , "cscore": request.session["csscore"] , "round":request.session["rounds_left"] })
        else:
            if(com_choice == -1 and your_choice  == 0):
                request.session["ysscore"] += 1
                if(request.session["ysscore"]>request.session["csscore"]):
                     result = "you win the game"
                elif(request.session["ysscore"]==request.session["csscore"]):
                    result ="draw"
                else:
                    result = "you lose the game"
                return render(request , 'result.html',{"result": result , "com_choice": dict1[com_choice] , "your_choice": dict1[your_choice] , "yscore": request.session["ysscore"] , "cscore": request.session["csscore"] , "round":request.session["rounds_left"] + 1})
                        
            elif(com_choice == 0 and  your_choice == 1):
                request.session["ysscore"] += 1
                if(request.session["ysscore"]>request.session["csscore"]):
                    result = "you win the game"
                elif(request.session["ysscore"]==request.session["csscore"]):
                    result ="draw"
                else:
                    result = "you lose the game"
                return render(request , 'result.html',{"result": result , "com_choice": dict1[com_choice] , "your_choice": dict1[your_choice] , "yscore": request.session["ysscore"] , "cscore": request.session["csscore"] , "round":request.session["rounds_left"] + 1})
                        
            elif(com_choice == 1 and  your_choice == -1):
                request.session["ysscore"] += 1
                if(request.session["ysscore"]>request.session["csscore"]):
                    result = "you win the game"
                elif(request.session["ysscore"]==request.session["csscore"]):
                    result ="draw"
                else:
                    result = "you lose the game"
                return render(request , 'result.html',{"result": result , "com_choice": dict1[com_choice] , "your_choice": dict1[your_choice] , "yscore": request.session["ysscore"] , "cscore": request.session["csscore"] , "round":request.session["rounds_left"] + 1})
                        
            else:
                request.session["csscore"] += 1
                if(request.session["ysscore"]>request.session["csscore"]):
                    result = "you win the game"
                elif(request.session["ysscore"]==request.session["csscore"]):
                    result ="draw"
                else:
                    result = "you lose the game"
                return render(request , 'result.html',{"result": result , "com_choice": dict1[com_choice] , "your_choice": dict1[your_choice] , "yscore": request.session["ysscore"] , "cscore": request.session["csscore"] , "round":request.session["rounds_left"] + 1})


    
# return render(request,'result.html', {"yscore": request.session["ysscore"] , "cscore": request.session["csscore"]})