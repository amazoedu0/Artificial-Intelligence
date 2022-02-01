def test_distinct(data):
    if len(data) == len(set(data)):
     return True
    else:
     return False
if(test_distinct(['a','e','i','o','u','u'])==True):
    print("All numbers are different")
else:
    print("All numbers are not different")
if(test_distinct([2,4,5,5,7,9])==True):
    print("All numbers are different")
else:
    print("All numbers are not different")
