from django.core.exceptions import ValidationError


def validate_phonenum(val):
    error = ValidationError("invalid phone number")
    # 07 92 39 79 06 len 10
    # +213 92 39 79 06 len 12

    if val.__len__() not in [10, 12]:
        raise error

    if val.__len__() == 10:
        if not val.isnumeric():
            raise error

        opCodes = ["05", "06", "07"]

        for i in opCodes:
            current = ""
            for j in range(2):
                current += val[j]

            if not current in opCodes:
                raise error

    else:
        current = ""
        for j in range(val.__len__() - 1):
            current[j] = val[j + 1]

        if not current.isnumeric():
            raise error

        ##
        countryCodes = ["+213"]

        for i in countryCodes:
            current = ""
            for j in range(4):
                current += val[j]

            if not current in countryCodes:
                raise error

def validate_name(val):
    error = ValidationError("invalid name")
    if val.__len__()<3:
        raise error
