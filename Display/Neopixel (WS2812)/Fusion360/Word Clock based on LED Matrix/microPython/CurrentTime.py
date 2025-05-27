import time

class CurrentTime:    
    OFFSET_GMT = 1 # dordrecht + 1
    
    def __init__(self, gmtOffset = 1, compensateDST = True):
        """
            gmtOffset, dordrecht + 1
        """
        self._gmtOffset = gmtOffset
        self._daylightSavings = 0
        self._compensateDST = compensateDST
        
    def updateDaylightSavings(self, dateTime):
        if not self._compensateDST:
            return
        
        year      = dateTime[0]
        HHMarch   = time.mktime((year,3 ,(31-(int(5*year/4+4))%7),1,0,0,0,0,0)) #Time of March change to CEST
        HHOctober = time.mktime((year,10,(31-(int(5*year/4+1))%7),1,0,0,0,0,0)) #Time of October change to CET
        now = time.mktime(dateTime)
        if HHMarch < now < HHOctober:               # we are before last sunday of march
            self._daylightSavings = 1
        else:
            self._daylightSavings = 0
            
    def getTime(self):        
        dt = time.localtime()
        
        self.updateDaylightSavings(dt)
        
        hours   = (dt[3] + self._gmtOffset + self._daylightSavings)%24
        minutes = dt[4]
        seconds = dt[5]
        return hours, minutes, seconds
    
    def getFormattedTime(self):
        dt = time.localtime()
        self.updateDaylightSavings(dt)
        hours   = (dt[3] + self._gmtOffset + self._daylightSavings)%24
        minutes = dt[4]
        seconds = dt[5]
        return f"{hours:02}:{minutes:02}:{seconds:02}"
    
if __name__ == "__main__":
    print(">> Start all tests <CurrentTime>")
    
    #when running on comuter OS will compensate the DST en timeZone
    timeInternal = CurrentTime(0, False)
    print(f"Time internal  : {timeInternal.getFormattedTime()}")
    
    timeDordrecht = CurrentTime(1, True)
    print(f"Time Dordrecht : {timeDordrecht.getFormattedTime()}")
    
    print(">> OK")    