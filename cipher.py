data=input("Enter your String:")
swift=int(input("swift with:"))
cipher=''
for char in data:
    if not char.isalpha():
        cipher+=char
        continue
    temp=ord(char)
    data_temp=swift%26
    if temp>=65 and temp<=90:
        temp+=data_temp
        if temp>90:
            temp=65+((temp-90)-1)
            
    if temp>=97 and temp<=122:
        temp+=data_temp
        if temp>122:
            temp=97+((temp-122)-1)
    cipher+=chr(temp)
print("cypher value is:"+cipher);
