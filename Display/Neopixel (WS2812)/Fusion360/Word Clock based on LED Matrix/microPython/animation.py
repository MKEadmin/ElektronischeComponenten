ANIMATION = ("/", "-", "\\", "|")
_index = 0
def getNextChar():
    global _index
    if _index >= len(ANIMATION):
        _index = 0
    char = ANIMATION[_index]
    _index += 1
    return char

if __name__ == "__main__":
    from time import sleep
    for x in range(20):
        print(getNextChar()+"\b", end="")
        sleep(.3)