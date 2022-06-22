from multipledispatch import dispatch
import errors
import mathProblemClass


########### OVERLOADED CALLERS ###########
@dispatch(list)
def arithmetic_arranger(listStr_InputFromUser):
    return arit_main(listStr_InputFromUser, False)
# def end

@dispatch(list, bool)
def arithmetic_arranger(listStr_InputFromUser, bool_PrintResult):
    if bool_PrintResult:
        return arit_main(listStr_InputFromUser, True)
    else:
        return arit_main(listStr_InputFromUser, False)
# def end


########### MAIN ARITHMETIC FUNCTION ###########
def arit_main(list_str_mainInput, bool_printResult):
    if len(list_str_mainInput) > 5:
        return errors.numOfProblems

    listClass_Problems = []

    for i in range(0, len(list_str_mainInput)):
        listClass_Problems.append(mathProblemClass.MathProblem(list_str_mainInput[i]))
        str_ParseError = listClass_Problems[i].parse()
        if str_ParseError != None:
            return str_ParseError
        listClass_Problems[i].calc()
        listClass_Problems[i].format()

    str_Lines = ["", "", "", ""]
    for problem in listClass_Problems:
        str_Lines[0] += problem.str_Primary + "    "
        str_Lines[1] += problem.str_Secondary + "    "
        str_Lines[2] += problem.int_Length * '-' + "    "
        if bool_printResult:
            str_Lines[3] += problem.str_Result + "    "

    length = len(str_Lines[0])

    str_retVal = str_Lines[0][:length-4] + '\n' + str_Lines[1][:length-4] + '\n' + str_Lines[2][:length-4]
    if bool_printResult:
        str_retVal += '\n' + str_Lines[3][:length-4]

    return str_retVal
# def end
