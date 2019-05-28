#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    bill_amount=0
    #write your logic here
    if food_type=="N":
        if quantity_ordered>0:
            a=quantity_ordered*150
            if distance_in_kms>0:
                if distance_in_kms<=3:
                    bill_amount=a
                elif distance_in_kms<=6 and distance_in_kms>3:
                    bill_amount=a+3
                elif distance_in_kms>6:
                    bill_amount=a+6
            #else:
                #bill_amount=-1
        #else:
            #bill_amount=-1
    elif food_type=="V":
        if quantity_ordered>0:
            a=quantity_ordered*120
            if distance_in_kms>0:
                if distance_in_kms<=3:
                    bill_amount=a
                elif distance_in_kms<=6 and distance_in_kms>3:
                    bill_amount=a+3
                elif distance_in_kms>6:
                    bill_amount=a+6
            #else:
                #bill_amount=-1
        #else:
           # bill_amount=-1

    else:
        bill_amount=-1
        
    return bill_amount

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,5)
print(bill_amount)
