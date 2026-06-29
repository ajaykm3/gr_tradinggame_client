from gr_tradinggame.coding.client import Client
from solution import play
from config import TEAM_NAME, PASSWORD, SERVER

if TEAM_NAME or not PASSWORD or not SERVER:
    raise SystemExit("ERROR: Edit config.py with your team name, password, and server


# Password is set on first submission and required for all future submissions.
# Choose any password you like on your first submit. Don't forget it.
client = Client('YourTeamName', password='YourPassword', server='ec2-3-254-122-192.eu-west-1.compute.amazonaws.com:5000')
client.test(play)
client.submit(play)
