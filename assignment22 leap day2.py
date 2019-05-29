#PF-Assgn-22
def find_leap_years(given_year):
    count=0
    list_of_leap_years=[]

    # Write your logic here
    while count<16:
        if given_year%4==0 and given_year%100!=0 and given_year%400==0:
            list_of_leap_years.apppend(given_year)
            count=count+1
        

    return list_of_leap_years

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)
