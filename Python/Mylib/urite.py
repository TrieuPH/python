def getToday():
    from datetime import date
    today = date.today()
    print(today.strftime("%Y/%m/%d"))

def test():
    # importing the subprocess module
    import subprocess
    
    # using the check_output() for having the network term retrieval
    devices = subprocess.check_output(['netsh','wlan','show','network'])
    
    # decode it to strings
    devices = devices.decode('ascii')
    devices = devices.replace("\r","")
    
    # displaying the information
    print(devices)

if __name__ == '__main__':
    test()