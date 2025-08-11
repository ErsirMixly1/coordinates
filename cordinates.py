import pyautogui
import time

print("Move your mouse to the target position. Ctrl+C to stop.")

try:
    while True:
        x, y = pyautogui.position()
        print(f"Mouse at ({x}, {y})", end="\r")  # prints current mouse pos, overwrites same line
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nDone.")

```bash
pip install pyautogui

pip install time
