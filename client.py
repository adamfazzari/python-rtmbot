from slackclient import SlackClient
import json
import os

# instance of API client that can be accessed from other files
api_client = None


# create an instance of the api client and initialize it with a token
def init(token):
    global api_client
    api_client = SlackClient(token)
    return api_client


def slack_token():
    return api_client.token

# get_users() returns a list of users in a Slack organization
def get_users():
    return json.loads(api_client.api_call('users.list'))['members']

def get_users_first_name(user_id):
    """
    Return the first name of the user with user_id
    :param user_id: slack user id
    :return: The user's first name, otherwise blank string if id can't be found
    """
    l = get_users()
    user = [u for u in l if u['id'] == user_id]
    if user:
        return user[0]['profile']['first_name']
    return ''

def get_channels():
    return json.loads(api_client.api_call('channels.list'))['channels']

def get_channel_id(channel_name):
    channel_name.replace("#", '')
    cl = get_channels()
    cl = [c for c in cl if c['name'] == channel_name]
    if cl:
        return cl[0]['id']
    return ''


# get_presence returns if a certain user is active or not in chat
def get_presence(id):
    return json.loads(api_client.api_call('users.getPresence', user=id))

def send_message(channel, message):
    """
    Post a message to a specific channel as the bot user
    :param channel: channel id or name
    :param message: message to post
    :return:
    """
    try:
        api_client.rtm_send_message(channel.replace("#", ''), message)
    except AttributeError:
        api_client.api_call("chat.postMessage", channel=channel, text=message, as_user=True)

def upload_file(channel, file_path):
    name = os.path.split(file_path)
    api_client.api_call("files.upload", channels=channel, filename=name, file=open(file_path, 'r'))
