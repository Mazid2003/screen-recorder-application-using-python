import cv2
import pyautogui
import numpy as np
import tkinter as tk
from tkinter import filedialog
import threading

# Global Variables
recording = False
output_file = "recorded_video.avi"

# Function to start recording
def start_recording():
    global recording, output_file
    recording = True
    output_file = filedialog.asksaveasfilename(defaultextension=".avi", filetypes=[("AVI files", "*.avi")])
    
    if not output_file:
        return

    screen_size = pyautogui.size()
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter(output_file, fourcc, 20.0, screen_size)

    while recording:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)

    out.release()

# Function to stop recording
def stop_recording():
    global recording
    recording = False

# GUI Setup
root = tk.Tk()
root.title("Screen Recorder")

start_btn = tk.Button(root, text="Start Recording", command=lambda: threading.Thread(target=start_recording).start(), padx=20, pady=10)
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="Stop Recording", command=stop_recording, padx=20, pady=10)
stop_btn.pack(pady=10)

root.mainloop()
