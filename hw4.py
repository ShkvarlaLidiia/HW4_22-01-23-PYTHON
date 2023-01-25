students = [["John", 3232],["Mike", 6000],["Bob", 2323]]
 
# max payment
# total payment
# name of person with min payment


min_payment_person = ""
max_val = students[0][1]
total = 0
 
for student in range(len(students)):    
    payment = students[student][1]
    total += payment
    if students[student][1] > max_val:
        max_val = students[student][1]
    else:
        min_payment_person = students[student][0]

print("max payment = ", max_val)       
print("total payment = ", total)       
print("min_payment_person = ", min_payment_person)       
