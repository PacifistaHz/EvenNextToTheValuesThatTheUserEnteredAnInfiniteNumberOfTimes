array=list()
print("Press the letter Q to exit. Otherwise, keep entering the number.")
while True:
    number=input("Enter a number: ")
    if number.upper()=="Q":
        break
    number=int(number)
    situation=""
    if number%2==0:
        situation="Even"
    else:
        situation="Odd"
    array.append(str(number)+": "+situation)
print(*array,sep="\n")
