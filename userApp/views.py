#from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from orjson import loads
from .models.models import addUser


@csrf_exempt
def userView(request):
    #print(request.body)
    #print(request.POST)

    rslt = {"status":False, "name":"", "email":"", "phonenum":"", "year":""}

    if request.method in ["POST"   ]: #"OPTIONS"
        rqst = request.POST
        #rqst = loads(rqst)
        keys = {"name": "", "email": "", "phonenum": "", "year": ""}
        err = False

        for i in keys:
            if not i in rqst:
                # incomplete form
                rslt[i] = "required field"
                err = True
                break

            keys[i] = rqst[i]

        if not err:
            # process everything
            name = keys["name"]
            email = keys["email"]
            phonenum = keys["phonenum"]
            year = keys["year"]
            #avlbl = keys["avlbl"]

            #err = not User(name, email, phonenum, year, avlbl).create()
            rslt["status"], mssg =  addUser(name, email, phonenum, year)
            for i in mssg:
                rslt[i] = mssg[i]
            

    #return render(request, "userApp/index.html", {})
    #return HttpResponse(dumps(rslt).decode("UTF-8"))
    return JsonResponse(rslt)



