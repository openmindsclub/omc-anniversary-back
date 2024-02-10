from django.shortcuts import render
from .models.models import addUser
# Create your views here.


def userView(request):
    if request.method == "POST":
        rqst = request.POST
        keys = {"name": "", "email": "", "phonenum": "", "year": "", "avlbl": ""}
        err = False

        for i in rqst:
            if not i in rqst:
                # incomplete form
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
            err = not addUser(name, email, phonenum, year)
            

    return render(request, "userApp/form.html", {})
