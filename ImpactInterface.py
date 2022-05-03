import os
from tkinter import *
from PIL import ImageTk, Image
from paramiko import SSHClient

# Establish connection with sensor
client = SSHClient()
client.load_system_host_keys()
#client.set_missing_host_key_policy(AutoAddPolicy()) # Insecure but will allow any connections

client.connect('192.168.254.32', username='pi', password='raspberry')

# Run ImpactSensor.py program remotely
stdin, stdout, stderr = client.exec_command("sudo python ImpactSensor.py", get_pty=True)

# Make sure directory is set to location of script
os.chdir(os.path.dirname(__file__))
# Debug - show current working directory
#print("CWD: " + os.getcwd())

# Initialize interface
root = Tk()
root.geometry("1920x1080")
root.configure(bg="black")

frame = Frame(root, bg="black")

# Add fullscreen toggle functionality
root.attributes("-fullscreen", True)
fullScreenState = False

root.bind("<F11>",
          lambda event: root.attributes("-fullscreen",
                        not root.attributes("-fullscreen")))

root.bind("<Escape>",
          lambda event: root.attributes("-fullscreen",
                        False))

# Create logo
img = ImageTk.PhotoImage(file="Unaffiliated+Athletics-Red.jpg")
#img = ImageTk.PhotoImage(file="UA-Los+Cholo-White.png")
logo = Label(root, image=img, borderwidth=0, highlightthickness=0)

# Create StringVars for dynamic storage of values
gForceVal = StringVar()
gForceVal.set("0")
recentMaxVal = StringVar()
recentMaxVal.set("0")
personalRecordVal = StringVar()
personalRecordVal.set("0")

# Format numeric displays
gForce = Label(frame, textvariable=gForceVal, font=("Impact", 60), foreground="white", background="black").pack()
recentMax = Label(frame, textvariable=recentMaxVal, font=("Impact", 40), foreground="white", background="black").pack()
personalRecord = Label(frame, textvariable=personalRecordVal, font=("Impact", 40), foreground="white", background="black").pack()

# Add elements to GUI
logo.place(relx = 0.5, rely = 0.05, anchor = "n")
frame.place(relx = 0.5, rely = 0.5, anchor = "center")

# Continuously read data from stdout and update display
while True:
    root.update_idletasks()
    root.update()
    line = stdout.readline()
    print(line.split(";"))
    gForceVal.set(line.split(";")[0])
    recentMaxVal.set(line.split(";")[1])
    personalRecordVal.set(line.split(";")[2])

# Terminate data reading and close SSH connection
client.exec_command(chr(3))
stdin.channel.shutdown_write()
stdin.close()
stdout.close()
stderr.close()
client.close()