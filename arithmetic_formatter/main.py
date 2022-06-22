from arithmetic_arranger import arithmetic_arranger

# Arguements:
# input: a list of strings containing the arithmetic problems, max 5 items, max 4 digits per number
# print_result (optional): to also print the results of the addition or subtraction
result = arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

print(result)
