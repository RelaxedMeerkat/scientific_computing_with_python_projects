import budget
from budget import create_spend_chart


# instantiation of categories
food = budget.Category("Food")
entertainment = budget.Category("Entertainment")
business = budget.Category("Business")

# do some living
food.deposit(900, "deposit")
entertainment.deposit(900, "initial deposit")
business.deposit(900, "deposit")
food.withdraw(105.55, "cheese & wine, just the essentials")
food.withdraw(60, "forgot the bread again")
entertainment.withdraw(33.40)
business.withdraw(10.99)
food.transfer(50, entertainment)

# print current balance for a budget category
financial_situation = str(food)
print(financial_situation)
# Prints:
# *************Food*************
# deposit                 900.00
# cheese & wine, just the-105.55
# forgot the bread again  -60.00
# Transfer to Entertainme -50.00
# Total: 684.45

# print a spending chart for all budgets
chart = create_spend_chart([food, entertainment, business])
print(chart)
# Prints:
# Percentage spent by category
# 100|          
#  90|          
#  80| o        
#  70| o        
#  60| o        
#  50| o        
#  40| o        
#  30| o        
#  20| o        
#  10| o  o     
#   0| o  o  o  
#     ----------
#      F  E  B  
#      o  n  u  
#      o  t  s  
#      d  e  i  
#         r  n  
#         t  e  
#         a  s  
#         i  s  
#         n     
#         m     
#         e     
#         n     
#         t     
