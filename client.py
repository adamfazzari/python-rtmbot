from slackclient import SlackClient
import json

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
    api_client.rtm_send_message(channel, message)