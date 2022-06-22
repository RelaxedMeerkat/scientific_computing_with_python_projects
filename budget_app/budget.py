import math

class Category:
    def __init__(self, title):
        self.title = title
        self.ledger = []
        self.spending = 0
        self.balance = 0
    # def end


    def deposit(self, amount, note = ""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": note})
    # def end


    def withdraw(self, amount, note = ""):
        withdraw_succesful = False
        if self.check_funds(amount):
            self.balance -= amount
            self.ledger.append(({"amount": -amount, "description": note}))
            self.spending += amount
            withdraw_succesful = True
        return withdraw_succesful
    # def end

    def __str__(self):
      star_length = int((30-len(self.title)) // 2)
      to_return = [star_length * "*" + self.title + star_length * "*"]
      for entry in self.ledger:
        line = 23 * " "
        line = entry["description"][0:23] + line[len(entry["description"]):]
        line_end = format(entry["amount"], '.2f')
        line_end = (7 - len(line_end)) * " " + line_end
        to_return.append(line + line_end)
      to_return.append("Total: " + format(self.balance, '.2f'))

      return_str = to_return[0]
      for line in to_return[1:]:
        return_str += "\n" + line
      return return_str
    # def end
  
    def get_balance(self):
        return self.balance
    # def end


    def transfer(self, amount, category):
        transfer_successful = False

        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.title)
            category.deposit(amount, "Transfer from " + self.title)
            transfer_successful = True
        return transfer_successful
    # def end


    def check_funds(self, amount):
        enough_funds = False
        if amount <= self.balance:
            enough_funds = True
        return enough_funds
    # def end
# class end

barchart_template = [
    "Percentage spent by category",
    "100| ", # line 1
    " 90| ",
    " 80| ",
    " 70| ",
    " 60| ",
    " 50| ",
    " 40| ",
    " 30| ",
    " 20| ",
    " 10| ",
    "  0| ", # line 11
    "    -",
    "     " # line 13 - template line for category names
]

new_category_line_template = [
    "           - ",
    "           - ",
    "           - ",
]

def create_spend_chart(categories):
    to_print = barchart_template.copy()
    new_category_line = new_category_line_template

    spendings = []
    sum_spending = 0
    title_length = 0
    i = 0
    for category in categories:
        spendings.append(category.spending)
        sum_spending += spendings[i]
        if len(category.title) > title_length:
            title_length = len(category.title)
        i += 1

    percentages = []
    for category_spending in spendings:
        percentages.append(int(math.floor((10 / sum_spending) * category_spending) + 1))

    for i in range(0, title_length-1): # prepare templates
        to_print.append(to_print[13])
        new_category_line[0] += " "
        new_category_line[1] += " "
        new_category_line[2] += " "

    vertival_lines = []
    i = 0
    for category in categories:
        vertival_lines.append(new_category_line.copy())
        vertival_lines[i][0] = ((11 - percentages[i]) * " " + percentages[i] * "o" + "-" + category.title).ljust(title_length + 12)
        i += 1

    for element in vertival_lines:
        for i in range(0, title_length + 12):
            to_print[i+1] += element[0][i] + element[1][i] + element[2][i]

    return_str = to_print[0]
    for line in to_print[1:]:
        return_str += "\n" + line
    return return_str
# def end
