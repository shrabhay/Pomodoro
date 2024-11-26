# Pomodoro Timer GUI Application
## Description
A simple and intuitive Pomodoro Timer built using Python and Tkinter. This application helps you manage your time efficiently by dividing work into intervals, traditionally 25 minutes in length, separated by short breaks. After four work intervals, a longer break is given.

---

## Features

- **Work Timer**: 25 minutes of focused work time.
- **Short Break**: 5-minute break after each work session.
- **Long Break**: 20-minute break after every 4 work sessions.
- **Visual Timer**: The countdown is displayed in a clear and simple format.
- **Progress Tracker**: Visual feedback (✔) for completed work sessions.
- **Start/Reset Buttons**: Start or reset the timer at any time.

---

## Files

- **`the_pomodoro_gui_application.py`**: The main Python file containing the Pomodoro Timer application using Tkinter for the GUI.

---

## How to Run

1. Ensure you have Python 3 installed. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone this repository:
   ```bash
   git clone https://github.com/shrabhay/Pomodoro.git
   cd pomodoro-timer
   ```

3. Install the necessary dependencies if you don't already have Tkinter:
    ```shell
    pip3 install tk
    ```

4. Run the Python script:
    ```shell
    python3 the_pomodoro_gui_application.py
    ```

    This will open the Pomodoro Timer GUI window.

---

## How It Works
- The Start button begins the countdown for a 25-minute work session.
- After the work session, the app will automatically switch to a short break for 5 minutes.
- After 4 work sessions (i.e., 4 Pomodoros), the app will switch to a longer break for 20 minutes.
- The timer displays the time remaining in a `mm:ss` format.
- Completed work intervals are tracked by checkmarks (`✔`) below the timer.

---

## License
This project is open-source and available under the MIT License.

---

## Credits
Built using Python and Tkinter for creating the graphical user interface.
Tomato image (used for the visual element of the timer) is sourced from a freely available image (e.g., in the repository as `tomato.png`).
