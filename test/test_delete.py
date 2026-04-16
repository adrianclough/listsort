import readchar

if __name__ == "__main__":
    while True:
        key = readchar.readkey()
        if key == readchar.key.DELETE:
            print("Delete")
            break
        elif key == readchar.key.BACKSPACE:
            print("Backspace")
            break
        else:
            print("Invalid key. Press DELETE.")