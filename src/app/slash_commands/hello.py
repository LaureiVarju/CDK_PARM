print("inside hello.py")
def hello(optional_arguments):
    

    message_content = "Hello there!!"
    response_data = {
        "type": 4,
        "data": {"content": message_content},
    }
    print("you invoked hello")
    return response_data

