MY_NAME = 'stacey'

def for_me(func):
    """
    Returns the function if the bot's name was mentioned at the start of the message
    :param func:
    :return:
    """
    def func_wrapper(message):
        if message['text'].lower().startswith(MY_NAME):
            func(message)
        else:
            pass

    return func_wrapper

def mentioned(func):
    """
    Returns the function if the bot's name was mentioned anywhere in the message
    :param func:
    :return:
    """
    def func_wrapper(message):
        if MY_NAME.lower() in message['text'].lower():
            func(message)
        else:
            pass

    return func_wrapper

