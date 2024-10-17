import exampleActions as action

ACTIONS = ("CMD", "TXT", "COL")
CMD_ACTIONS = {'LED_ON': action.ledOn,
               'LED_OFF': action.ledOff,
               'LED_BLINK': action.blinkLed
               }


def handle_command(action, data):
    print(action, data)
    if action == ACTIONS[0]:
        CMD_ACTIONS[data]()
    elif action == [1]:
        print("TXT = ", data)
    elif action == ACTIONS[2]:
        print("Color = ", data)
