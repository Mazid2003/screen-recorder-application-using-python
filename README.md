# 🎥 GUI-Based Screen Recorder Using Python

**📌 Project Overview**

This project is a GUI-based screen recorder that captures the screen in real-time and saves it as a video file. Built using Python, Tkinter, OpenCV, and PyAutoGUI, this application allows users to start and stop recording with just a click.

**🎯 Features**

✅ Simple GUI – User-friendly interface built with Tkinter.

✅ Start & Stop Recording – Easy-to-use buttons for control.

✅ High-Quality Screen Capture – Uses PyAutoGUI and OpenCV for smooth recording.

✅ Custom Save Location – Allows users to choose where to save the recorded video.

✅ Pinned for Quick Access – The application can be pinned to the taskbar for easy use.

**🛠 Technologies Used**

🔹 Python – Core programming language.

🔹 Tkinter – For building the graphical user interface.

🔹 OpenCV (cv2) – For saving video output.

🔹 PyAutoGUI – For capturing screen frames.

🔹 NumPy – For efficient image processing.

**📜 How It Works?**

1️⃣ Start the Application – Run the Python script or the converted application.

2️⃣ Click "Start Recording" – Select a save location and begin capturing the screen.

3️⃣ Click "Stop Recording" – The recording is automatically saved as an AVI file.

4️⃣ View the Recorded Video – Open the saved file and playback the screen capture.

**📊 Future Enhancements**

🔹 Add Audio Recording – Capture system or microphone audio along with video.

🔹 Pause/Resume Feature – Allow users to pause and continue recording.

🔹 Save in MP4 Format – Improve compatibility by converting to MP4.

🔹 Frame Rate Adjustment – Optimize performance by allowing users to set FPS.

🚀 How to Clone & Run Your Project

Once you upload your project to GitHub, others can clone and run it easily. Here’s how:

1️⃣ Clone the Repository

Anyone can clone your project using Git by running:

git clone https://github.com/Mazid2003/screen-recorder-application-using-python.git

Or, they can download the ZIP file from GitHub and extract it manually.

2️⃣ Navigate to the Project Directory

After cloning, navigate into the project folder:

cd YourRepositoryName

3️⃣ Install Dependencies

Ensure Python is installed, then install the required package:

pip install pyautogui

4️⃣ Run the Screenshot Script

After setup, they can execute the script:

python screenrecord.py

The screenshot will be stored in the screenshots folder inside the project directory.

📌 Updating the Project

If you make updates, others can pull the latest changes using:

git pull origin main

**Convert to an Executable**

To create a standalone application, use PyInstaller:

pip install pyinstaller

pyinstaller --onefile --windowed --icon=icon(image of you application and it should be in .ico formate).ico screen_recorder.py

**📌 Conclusion**

This Screen Recorder Application provides an efficient way to capture screen activity, making it ideal for tutorials, presentations, and screen-sharing needs. Its simple GUI and real-time recording make it a powerful yet lightweight tool.

**💬 Want to Collaborate?**

Feel free to fork the repo, submit PRs, and give your feedback! 🔥💡

**📜 License**

This project is open-source under the MIT License. Feel free to use and modify it! 🚀
