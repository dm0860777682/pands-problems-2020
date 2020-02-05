#Donal Maher 
# Check if one number divides by another

def sleep_in(weekday, vacation):
    if (weekday and vacation == False):
        return False
    else:
        return True

result = sleep_in(False, False)
print("The result is {} ".format(result))