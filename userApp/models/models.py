from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phonenum = models.CharField(max_length=13)  # 13
    year = models.CharField(max_length=4)


from .CustomValidators import validate_name, validate_phonenum, validate_year
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

def addUser(name, email, phonenum, year):
    # do some mini checks
    
    # validators
    toValidate = [name, email, phonenum, year]
    validators = [validate_name, validate_email, validate_phonenum, validate_year]

    for i in range(toValidate.__len__()):
        try:
            validators[i](toValidate[i])
        except ValidationError as e:
            print(e)
            return False
    
    # check existance
    checks = [
        User.objects.filter(name=name),
        User.objects.filter(email=email),
        User.objects.filter(phonenum=phonenum),
    ]

    for i in checks:
        if i.__len__():
            return False


    #final we can add
    user = User(name=name, email=email, phonenum=phonenum, year=year)
    user.save()

    return True
