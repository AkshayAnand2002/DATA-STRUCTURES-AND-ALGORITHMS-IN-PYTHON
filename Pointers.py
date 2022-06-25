num1 = 11

num2 = num1

print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

print("\nnum1 points to:", id(num1))##id gives address of variable.
print("num2 points to:", id(num2)) 
#above will give same address for num1 and num2 as both are equal.
num2 = 22 

print("\nAfter num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2) 

print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))
#since num2 value is changed so it will not point to same address as num1.
#so in the output we get different ids.


#####################################


dict1 = {
         'value': 11
        }

dict2 = dict1 

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
#Above steps same as that of integers gives same id as dict2 points to dict1
#as they are equal.

dict2['value'] = 22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2) 

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
#HERE WE GET OUTPUT I.E. DIFFERENT FROM THAT OF INTEGERS.
#THE ABOVE LINES WILL GIVE SAME IDS AGAIN FOR DICT1 AND DICT2
#UNLIKE INTEGERS WHICH GIVE DIFFERENT IDS.
#ALSO THE PRINTED VALUES FOR BOTH DICT HAVE BEEN UPDATED TO 22.
#SO UNKIKE INTEGERS DICTIONARY I.E. dict1 and dict2 CONTINUE
#POINTING TO THE SAME PLACE OR ADDRESS.

