
# checking the value error
def validate_age(age):
    # check is age is less than zero
    if age < 0:
        raise ValueError('Age cannot be less than zero')