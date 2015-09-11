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

def channel_type(channel_type):
    def _channel_type(func):
        """
        Returns the function if the channel is a direct message to the bot
        :param func:
        :return:
        """
        def func_wrapper(message):
            channel_types = [c.lower()[0] for c in channel_type.split("+")]
            if message['channel'].lower()[0] in channel_types:
                func(message)
            else:
                pass

        return func_wrapper
    return _channel_type

