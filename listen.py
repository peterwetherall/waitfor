import subprocess

#Use a unique prefix here to enable two senders and listeners to operate over the same network
#The prefix must match that used by the listener script
prefix = "1100"

#Attempt to retrieve data from the file
def getData():
    try:
        file = open("story.txt", "r")
        data = file.read().split("\n")
        file.close()
        return data
    except Exception:
        return False
def overRideFile():
    try:
        open("story.txt", "w").close()
        return True
    except Exception:
        return False

#List of all signals that can be sent
signals = ["REPEAT", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "SPACE", "FULLSTOP", "COMMA", "EXCLMARK", "QUESMARK", "END"]
script = ""

# ########## #
# Important! #
# ########## #
#Replace "REDACTED" with a relevant full path here (e.g. C:\\Users\\John\\waitfor\\story.txt)
for i in range(0, len(signals)):
   script += " && start /b \"x\" \"cmd.exe\" /q /c for /l %N in (1,0,2) do (waitfor " + prefix + signals[i] + " ^&^& echo a" + signals[i] + "^>^>REDACTED\\story.txt)"

#Create an instance of command prompt and within call sub-processes to wait for every possible signal
subprocess.call("cmd.exe /c mode 30,2 && title Listener && color f7 " + script + " && exit")

#Instructions
print("Listening for signals ...")
print("When you are finished receiving messages close this IDLE window and keep clicking the cross on the Listener prompt window until it goes away.")

#Receiver loop
prevline = ""
while True:
    data = False
    #Keep retrieving until new data is found
    while data == False:
        data = getData()
    data = [i for i in data if i != ""]
    if len(data) > 0:
        overRide = False
        while overRide == False:
            overRide = overRideFile()
        for line in data:
            line = line[1:]
            #Handle repeated characters
            if line == "REPEAT":
                print(prevline, end="", flush=True)
            #Handle letters or numbers
            elif len(line) == 1:
                print(line, end="", flush=True)
                prevline = line
            #Handle symbols
            else:
                if line == "SPACE":
                    print(" ", end="", flush=True)
                    prevline = " "
                elif line == "FULLSTOP":
                    print(".", end="", flush=True)
                    prevline = "."
                elif line == "COMMA":
                    print(",", end="", flush=True)
                    prevline = ","
                elif line == "EXCLMARK":
                    print("!", end="", flush=True)
                    prevline = "!"
                elif line == "QUESMARK":
                    print("?", end="", flush=True)
                    prevline = "?"
                elif line == "END":
                    print("\n")
                    prevline = ""
