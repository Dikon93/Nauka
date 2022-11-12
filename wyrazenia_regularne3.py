import re
# "." uznaje dowolny znak
if re.match("^[A-Z][a-z]*$", "Ala"):
    print("Dopasowano")
else:
    print("niedopasowano")

# plus dopuszcza minimalnie jedno wystąpienie wyrazenia
if re.match("^[A-Z][a-z]+$", "Ala"):
    print("Dopasowano")
else:
    print("niedopasowano")

# znak zapytania uznaje ze moze ale nie musi wystąpić chociaz raz

if re.match("^[A-Z][a-z]?[A-Z]$", "Ala"):
    print("dopasowano")
else:
    print("niedopasowano")

# 2-5 wystąpień danego znaku
if re.match("^[A-Z][a-z]{2,5}$", "Ala"):
    print("dopasowano")
else:
    print("niedopasowano")
