import re
import errors


########### MATH PROBLEM CLASS ###########
class MathProblem:
    def __init__(self, str_input):
        self.str_Input = str_input
        self.str_Primary = None
        self.str_Secondary = None
        self.str_Operator = None
        self.int_Length = None
        self.str_Result = None
    # def end

    def parse(self):
        str_Error = errors.noError

        self.str_Primary = re.findall('(.*)\s.*\s.*', self.str_Input)[0]
        self.str_Secondary = re.findall('.*\s.*\s(.*)', self.str_Input)[0]
        self.str_Operator = re.findall('.*\s(.*)\s.*', self.str_Input)[0]

        if not self.str_Primary.isdigit() or not self.str_Secondary.isdigit():
            str_Error = errors.numType
        elif self.str_Operator != '+' and self.str_Operator != '-':
            str_Error = errors.operator
        elif len(self.str_Primary) > 4 or len(self.str_Secondary) > 4:
            str_Error = errors.numLength

        return str_Error
    # def end

    def calc(self):
        if self.str_Operator == '+':
            self.str_Result = str(int(self.str_Primary) + int(self.str_Secondary))
        else:
            self.str_Result = str(int(self.str_Primary) - int(self.str_Secondary))

    # def end

    def format(self):
        self.int_Length = len(max(self.str_Primary, self.str_Secondary, key=len)) + 2

        self.str_Primary = (self.int_Length - len(self.str_Primary)) * " " + self.str_Primary
        self.str_Secondary = self.str_Operator + (self.int_Length - len(self.str_Secondary) - 1) * " " + self.str_Secondary
        self.str_Result = (self.int_Length - len(self.str_Result)) * " " + self.str_Result
    # def end

# class end
