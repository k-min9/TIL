def add_hello(input_string):
    if not input_string:
        return "Please, Enter Your name"
    return input_string + ", hello"
    
if __name__ == "__main__":
    input_str = ''
    if input(''):
        input_str = input('')
    result = add_hello(input_str)
    print("Result:", result)
