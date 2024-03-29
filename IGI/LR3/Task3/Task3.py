def input_string():
    '''This function is the entry point in this module (task 3, variant 30). The function displays comments
             for the user and also calls functions to execute the task.'''
    print("Task 3 (30): \n"
          "В строке, вводимой с клавиатуры, подсчитать \n"
          "количество пробелов и знаков пунктуации\n")
    text = input("Input string: ")

    func_with_decorator = decorator_func(count_paramtrs)
    func_with_decorator(text)

def count_paramtrs(str):
    '''This function counts and outputs the number of all punctuation characters.'''
    spaces = str.count(" ")
    comas = str.count(",")
    periods = str.count(".")
    exclamation_points = str.count("!")
    question_marks = str.count("?")
    colons = str.count(":")
    dashes = str.count("-")
    semicolons = str.count(";")
    amount_of_punctuation_marks = comas + periods + exclamation_points + question_marks + colons + dashes + semicolons

    print(f"Amount of spaces : {spaces}")
    print(f"Amount of comas : {comas}")
    print(f"Amount of periods : {periods}")
    print(f"Amount of exclamation points : {exclamation_points}")
    print(f"Amount of question marks : {question_marks}")
    print(f"Amount of colons : {colons}")
    print(f"Amount of dashes : {dashes}")
    print(f"Amount of semicolons : {semicolons}")

    return amount_of_punctuation_marks

def decorator_func(func):
    '''The function that uses decorator.'''
    def new_func(*args, **kwargs):
        print("String analysis:")
        amount_of_punctuation_marks = count_paramtrs(*args, **kwargs)
        print(f"Total amount of punctuation marks : {amount_of_punctuation_marks}")
        return amount_of_punctuation_marks
    return new_func