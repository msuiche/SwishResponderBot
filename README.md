# SwishResponderBot
![swishbot](images/swishbot.jpg)

A Discord Incident Response Bot. Protecting Discord communities.
Use this bot after being hacked to collect the required information for your investigation and understand what happened.
## Usage
Add the bot to your server using [this link](https://discord.com/api/oauth2/authorize?client_id=900266608759537727&permissions=536871040&scope=bot).

Make sure the user requested the logs via the command have a role called 'responders' assigned to them. Then just request the logs using the following commands:

### !swish.export logs
Get a copy of the audit logs as a CSV file.
### !swish.export webhooks
Get a copy of the webhooks as a CSV file.

## Permissions
- View Audit Log
- Manage Webhooks (_Personal request to anyone working for Discord for a `View Webhooks` permissions. Plzz_)

## Background Context
Refer to the [CreatureToadz Twitter's thread](https://twitter.com/msuiche/status/1450702711981289472) I wrote on Twitter about how this project was born. 

## Questions or Feedback
- Discord: https://discord.gg/ZRnT6TMPbU
- Twitter: https://www.twitter.com/msuiche
