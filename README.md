# cmd-line-chat
Simple, easy-to-use, command-line chat

## Usage

### LAN
A Local Area Network (LAN) is definitely the easiest way to use this tool. Just download the repository and then run the server.py by 
running `python (or python3 depending on your os) server.py [port]`. Port should be a decently high number to avoid interference with
other programs -- 7777 or 25565 are my go-tos.

That will start the server and print out the server's IP.

On another computer (or the same computer, I guess) connected to the same network, run `python client.py [IP] [Port]` to connect to the server, with the IP being the IP of
the server and the port being the aforementioned port for the server.

### Remote Connection
First, choose the port you're going to run the server on, and then [port forward](https://www.noip.com/support/knowledgebase/general-port-forwarding-guide/) that port. Doing this will allow computers on other networks to connect to your computer by connecting to your router over the port you chose. Then, start the server the same way as in the LAN tutorial, but start the client by connecting to the server's public IP (so search "what's my IP" on the server machine).
