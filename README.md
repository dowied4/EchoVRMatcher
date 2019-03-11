# EchoVR Matcher
This is made to connect players faster as the default way of using your friends list is very slow and unreliable. EchoVR Matcher is a way of directly connecting spectators or players to specific matches with no need to way for invites.

### Download:
https://www.mediafire.com/file/o3797ebjcaqotte/EchoVR_Matcher_V1.1.zip/file

## Usage
To be able to get the Match ID the game MUST BE IN HTTP mode. Clicking launch from the matcher will launch echovr with the -http flag. The id will always be visible and to be able to send it to other users you just need to hit the adjacent button to copy to clipboard. To be able to join based off an ID you need to put it into the Target Match ID field and click join(make sure you select if you want to join as a spectator or a player). To change the path click browse and find the echovr.exe and click it then click open. 

### If you want to watch pubs as a spectator
This is not explicitly obvious but if you want a random pub spectator stream you just need to select spectator under "join as" and hit join match

## Installation
To be able to use the package directly you need two external packages using pip:

```bash
pip install PyQt5
pip install pyperclip
pip install echovr-api
```
Credit to Ajedi for making the api: https://github.com/Ajedi32/echovr-api


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
