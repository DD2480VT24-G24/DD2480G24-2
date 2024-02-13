# Server setup 
## How To Run
1.  Start tmux by typing `tmux`
2.  Create a new window by `Ctrl + b c`
3.  Start ngrok by starting the `./start_ngrok.sh` script
4.  Switch to another window with tmux by `Ctrl + b n`
5.  Start the server via the `./start_server.sh` script
6.  Server is up and running!

## The server doesn't work, what should I do?
1.  Start by look if tmux windows are open by `tmux ls`
2.  If there none tmux activated then follow "How To Run"-guide. 
3.  Start tmux by `tmux` then `Ctrl + b w` to see each window.
4.  Look if all the windows is correct by enter them. If needed restart with the script.
5.  It should now work again.

## Server dependencies
- tmux
- ngrok
- python enviroment

## Scripts
start_ngrok.sh
```#!/bin/bash
ngrok http --domain=YOUR_DOMAIN PORT
```

start_server.sh 
```
#!/bin/bash
cd YOUR_REPO
if [ ! -f .env ]
then
  export $(cat .env | xargs)
fi
source venv/bin/activate
pip install -r requirements.txt
cd src/
python3 app.py
```

## Our server
The server is hosted via DigitalOcean with a server in Frankfurt. 
### Specs
- 1 Shared CPU
- 1 GB Memory 
- 25 GB Disk 
- OS: Ubuntu 23.10 x64

### Get access
Your SSH key needs to be added to the server. Then connect via ssh root@IPADRESS
