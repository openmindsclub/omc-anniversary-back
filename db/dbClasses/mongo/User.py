import pymongo

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
        # run the validators

        user = {
            "name": self.name,
            "email": self.email,
            "phonenum": self.phonenum,
            "year": self.year,
            "avlbl": self.avlbl,
        }

        collection.insert_one(user)
