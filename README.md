# waitfor
Send data across a Windows network using the waitfor synchronization command.

This is a **proof-of-concept** for a novel data exfiltration technique that *could* be used in a Windows network environment.

### Setup ⚙️

- On the receiving machine, run the **listen.py** file and create a blank text file called **story.txt** in the same directory

- Modify the **listen.py** file to contain the full path of the files' directory, as stated in the comments

- Finally, run the **send.py** file on the sending machine and enter your message
