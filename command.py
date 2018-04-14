import re
from client import send_message

my_name = 'bot'

outputs = []

def help_message(channel, command, help):
    """
    Post a formatted help message to the given channel
    :param channel: channel to post into
    :param command: command pattern
    :param help: descriptive text
    :return:
    """
    if help:
        send_message(channel, " - ".join([command, help]))

def disabled(func):
    """
    Temporarily disable a plugin
    :param func:
    :return:
    """
    def func_wrapper(message):
        pass

    return func_wrapper

def command(command, help=None):
    def _command(func):
        """
        Returns the function if the bot's name was mentioned at the start of the message followed by the specified command
        :param func:
        :return: Calls the command function with the salutation removed from the text
        """
        def func_wrapper(message):
            cmd_pattern = "^{}.*".format(' '.join([my_name, command.lower()]))
            help_pattern = "^{}.*".format(' '.join([my_name,'help']))

            if 'text' not in message:
                message['text'] = message.get('attachments', [{}])[0].get('pretext', '')
            result = re.search(help_pattern, message['text'].lower())
            if result:
                help_message(message['channel'], command, help)
                return

            result = re.search(cmd_pattern, message['text'].lower())
            if result:
                msg = dict(message)
                msg['text'] = re.sub("^{}".format(my_name.lower()), '', msg['text'].lower()).strip()
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
        if my_name.lower() in message['text'].lower():
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

