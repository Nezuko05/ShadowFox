# 1. Create a list of your friends' names. The list should have at least 5 names. Create a list of tuples.
#    Each tuple should contain a friend's name and the length of the name.
#    For example, if someone’s name is Aditya, the tuple would be: ('Aditya', 6)

friends=["Riddhi","Sagar","Isha","Tanu","Priya"]
tuple_list=[(name,len(name)) for name in friends]
print(tuple_list)

#--------------------------------------------------------------------------------------------------#

2.You and your partner are planning a trip, and you want to track expenses. 
Create two dictionaries, one for your expenses and one for your partner's expenses. 
Each dictionary should contain at least 5 expense categories and their corresponding amounts.
For example:
Your expenses
your_expenses = {
"Hotel": 1200,
"Food": 800,
"Transportation": 500,
"Attractions": 300,
"Miscellaneous": 200
}
Your partner's expenses
partner_expenses = {
"Hotel": 1000,
"Food": 900,
"Transportation": 600,
"Attractions": 400,
"Miscellaneous": 150
}
Calculate the total expenses for each of you and print the results.
Determine who spent more money overall and print the result.
Find out the expense category where there is a significant difference in spending between you and your partner.
Print the category and the difference.
'''

# Create two dictionaries, one for your expenses and one for your partner's expenses. 

my_expenses={"Hotel":1200,"Food":800,"Transportation":500,"Attractions":300,"Miscellanous":200}

partner_expenses={"Hotel":1000,"Food":900,"Transportation":600,"Attractions":400,"Miscellanous":150}

total_my_expenses= sum(my_expenses.values())
print(total_my_expenses)
total_partner_expenses=sum(partner_expenses.values())
print(total_partner_expenses)


if total_my_expenses > total_partner_expenses:
    print("I have spent more money")
elif total_my_expenses < total_partner_expenses:
    print("partner spent more money")
else:
    print("Both spent same amount of money")   



for category in my_expenses:
    if my_expenses != partner_expenses:
        difference= (my_expenses[category]-partner_expenses[category]) 
        print(difference)    


           