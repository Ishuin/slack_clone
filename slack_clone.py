import slack
from datetime import datetime
import os

# Bot named extractor for slack workspace named "openclones"
bot = slack.WebClient(token=os.environ['SLACK_BOT_TOKEN'])

# Created a request from the bot to access the slack channel information containing the messages sent
# by all the users till date or from the earliest existing message.
response = bot.conversations_history(
    channel='CU3D2JQER'
)
print(response['messages'][::-1])
for i in response['messages']:
    print(i['text'], datetime.fromtimestamp(int(i['ts'].split('.')[0])))

'''
Future work:
- Identifying users based on their ID, i.e., response['messages']['user'].
- Connecting the information to a database that will store the information returned by the response of the bot.
- Deliver information on a GUI with User, content and date specific search options.
- Displaying required information into an excel sheet or some similar data displaying format.
- Identifying multiple uses of this application.
'''
