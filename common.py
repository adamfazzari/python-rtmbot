import re

MY_NAME = 'stacey'

def disabled(func):
    """
    Temporarily disable a plugin
    :param func:
    :return:
    """
    def func_wrapper(message):
        pass

    return func_wrapper

def command(command):
    def _command(func):
        """
        Returns the function if the bot's name was mentioned at the start of the message followed by the specified command
        :param func:
        :return: The message text with the salutation removed
        """
        def func_wrapper(message):
            if message['text'].lower().startswith(' '.join([MY_NAME, 'help'])):
                msg = dict(message)
                msg['text'] = re.sub("^{}".format(MY_NAME), '', msg['text']).strip()
                msg['text'] = 'help'
                func(msg)
            elif message['text'].lower().startswith(' '.join([MY_NAME, command])):
                msg = dict(message)
                msg['text'] = re.sub("^{}".format(MY_NAME), '', msg['text']).strip()
                func(msg)
            else:
                pass

        return func_wrapper
    return _command

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

