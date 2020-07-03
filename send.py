import subprocess

#Use a unique prefix here to enable two senders and listeners to operate over the same network
#The prefix must match that used by the listener script
prefix = "1100"

while True:
    data = str(input("Enter a message to send: ")).lower()
    datt = ""
    prevchar = ""
    repeat = False
    for char in data:
        #Send appropriate signal
        if char == prevchar:
            #Due to a time lag after a waitfor receives a signal,
            #an additional signal is needed to handle repeated characters
            datt += " && waitfor /si " + prefix + "REPEAT"
            repeat = True
        elif char == " ":
            datt += " && waitfor /si " + prefix + "SPACE"
        elif char == ".":
            datt += " && waitfor /si " + prefix + "FULLSTOP"
        elif char == ",":
            datt += " && waitfor /si " + prefix + "COMMA"
        elif char == "!":
            datt += " && waitfor /si " + prefix + "EXCLMARK"
        elif char == "?":
            datt += " && waitfor /si " + prefix + "QUESMARK"
        else:
            datt += " && waitfor /si " + prefix + char
        if repeat:
            #Repeat symbol has just been sent, so no need to check for repeated signal
            prevchar = ""
        else:
            prevchar = char
    subprocess.call("cmd /c mode 15,1 && color f7" + datt + " && waitfor /si " + prefix + "END && exit")
    print("Message successfully sent!")
