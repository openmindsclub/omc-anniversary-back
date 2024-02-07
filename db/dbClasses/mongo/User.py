import pymongo

from ..CustomValidators import validate_name, validate_phonenum
from django.core.exceptions import ValidationError
from django.core.validators import validate_email


"""
we need to store our auth info in venv
"""

client = pymongo.MongoClient(
    "mongodb+srv://username:password@HOSTNAME/DATABASE_NAME?authSource=admin&tls=true&tlsCAFile=<PATH_TO_CA_FILE>"
)
# Define DB Name
dbname = client["admin"]

# Define Collection
collection = dbname["user"]


class User:
    def __init__(self, name, email, phonenum, year, avlbl):
        self.name = name
        self.email = email
        self.phonenum = phonenum
        self.year = year
        self.avlbl = avlbl

    def create(self):
        # we need to run some checks to see if the user doesn't exist
        """
        THIS WAS NOT TESTED YET
        """
        toCheck = {
            "name": self.name,
            "email": self.email,
            "phonenum": self.phonenum,
        }
        for i in toCheck:
            if collection.find_one({i: toCheck[i]}):
                return False

        # run the validators
        toValidate = [self.name, self.email, self.phonenum]
        validators = [validate_name, validate_email, validate_phonenum]

        for i in range(toValidate.__len__()):
            try:
                validate_email(validators[i](toValidate[i]))
            except ValidationError as e:
                #print(e)
                return False


        user = {
            "name": self.name,
            "email": self.email,
            "phonenum": self.phonenum,
            "year": self.year,
            "avlbl": self.avlbl,
        }

        collection.insert_one(user)

        return True
