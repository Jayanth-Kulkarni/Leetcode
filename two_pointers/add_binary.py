def add_binary(str1, str2):
    array = []
    carry = 0
    prefix = ""
    if len(str1)>len(str2):
        str2 = (len(str1)-len(str2))*"0"+str2
    elif len(str1)<len(str2):
        str1 = (len(str2)-len(str1))*"0"+str1
    for i,j in zip(reversed(str1),reversed(str2)):
        array.append(str(int((int(i)+int(j)+carry))%2))
        carry = int((int(i)+int(j)+carry)/2)
    if carry:
        array.append(str(carry))
    return "".join(list(reversed(array)))



a = "111" 
b = "1111"
print(add_binary(a,b))
