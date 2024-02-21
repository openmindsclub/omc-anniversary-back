from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phonenum = models.CharField(max_length=15)  # 15
    year = models.CharField(max_length=4)


    def __str__(self):
        return self.name

from .CustomValidators import validate_name, validate_phonenum, validate_year
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def addUser(name, email, phonenum, year):
    rslt =  {"name": "", "email": "", "phonenum": "", "year": ""}
    # do some mini checks
    
    # validators
    toValidate =[ name, email, phonenum, year]
    validators = [validate_name, validate_email, validate_phonenum, validate_year]

    cnt = 0
    for i in range(toValidate.__len__()):
        try:
            validators[i](toValidate[i])
        except ValidationError as e:
            #print(e)
            rslt[ list(rslt.keys())[cnt]   ] = e.message
            return [False, rslt]
        cnt += 1
    
    # check existance
    checks = [
        User.objects.filter(name=name),
        User.objects.filter(email=email),
        User.objects.filter(phonenum=phonenum),
    ]

    cnt = 0
    for i in checks:
        if i.__len__():
            rslt[ list(rslt.keys())[cnt]   ] = f"{list(rslt.keys())[cnt]} already in use"
            return [False, rslt]
        cnt += 1
        

    #final we can add
    user = User(name=name, email=email, phonenum=phonenum, year=year)
    user.save()

    return [True, rslt]
