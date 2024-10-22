from IRQButton import IRQButton

counter = 0
def pressed(data):
    global counter
    print(f"{counter:5} Pressed({data})")
    counter += 1
    
btn = IRQButton(26, pressed, "A", notifyAllChanges = True)
btn = IRQButton(27, pressed, "B", notifyAllChanges = True)

while True:
    machine.idle() # Delay to prevent excessive CPU usage
