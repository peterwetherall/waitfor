# waitfor
Send data across a Windows network using the waitfor synchronization command.

This is a **proof-of-concept** for a novel data exfiltration technique that *could* be used in a Windows network environment.

### Setup ⚙️

- On the receiving machine, modify the **listen.py** file to contain the full path of its directory, as stated in the comments

- Create a blank text file called **story.txt** in the same directory

- Run the **listen.py** file

- Finally, run the **send.py** file on the sending machine and enter your message
