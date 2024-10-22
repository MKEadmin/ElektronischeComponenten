import blueTooth as bt
import exampleDataHandler as handler

bt.listen(handler.handle_command)
    