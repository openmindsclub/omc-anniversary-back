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


def addUser(
    name,
    email,
    phonenum,
    year,
    avlbl,
):
    #we need to run some checks to see if the user doesn't exist
    #run the validators


    user = {
        "name": name,
        "email": email,
        "phonenum": phonenum,
        "year": year,
        "avlbl": avlbl,
    }

    collection.insert_one(user)

