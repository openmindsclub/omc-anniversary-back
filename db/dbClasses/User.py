from db.dbClasses.Essentials import DbPath, StrFilter, fileExists, writeToJson, openJson

from .CustomValidators import validate_name, validate_phonenum
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def getUsers():
    return DbPath("users").getDb()


def updateUsers(val):
    DbPath("users").writeToDb(val)


class User:
    def __init__(self, name, email, phonenum, year, avlbl):
        self.name = name
        self.email = email
        self.phonenum = phonenum
        self.year = year
        self.avlbl = avlbl

    def exists(self):
        return self.name in getUsers()

    def get(self):
        rslt = [False, "non existing"]

        if self.exists():
            rslt[0] = True
            rslt[1] = getUsers()[self.name]

        return rslt

    def create(self):
        # run the validators
        toValidate = [self.name, self.email, self.phonenum]
        validators = [validate_name, validate_email, validate_phonenum]

        for i in range(toValidate.__len__()):
            try:
                validate_email(validators[i](toValidate[i]))
            except ValidationError as e:
                print(e)
                return False

        if self.exists():
            return False

        users = getUsers()
        users[self.name] = {
            "email": self.email,
            "phonenum": self.phonenum,
            "year": self.year,
            "avlbl": self.avlbl,
        }

        updateUsers(users)

        return True
