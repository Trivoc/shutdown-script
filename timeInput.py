import re

def getTime(n) : 
    specTime = re.sub(r'\W+', ' ', n)
    specTime = specTime.split(" ")
    if len(specTime) > 4 or len(specTime) < 1 : 
        print("Faulty input format, try again")
    else : 
        result = 0
        for token in specTime : 
            formatted = getSpecific(re.sub('[^0-9dhmsDHMS]+', '', token))
            try : 
                result += formatted
            except TypeError : 
                print("Format error on token " + token)
        return result

def getSpecific(timeStamp) : 
    if "d" in timeStamp or "D" in timeStamp : 
        timeStamp = timeStamp.replace("d" or "D", "")
        return convert_to_time(timeStamp, (3600*24))
    if "h" in timeStamp or "H" in timeStamp : 
        timeStamp = timeStamp.replace("h" or "H", "")
        return convert_to_time(timeStamp, 3600)
    if "m" in timeStamp or "M" in timeStamp : 
        timeStamp = timeStamp.replace("m" or "M", "")
        return convert_to_time(timeStamp, 60)
    if "s" in timeStamp or "S" in timeStamp : 
        timeStamp = timeStamp.replace("s" or "S", "")

    return convert_to_time(timeStamp, 1)

def convert_to_time(time, multiplier) : 
    try : 
        seconds = int(time)
        return seconds*multiplier
    except ValueError : 
        return 0

#Takes time in seconds, returns formatted string
def formatted_time_string(time) : 
    days = time // (3600 * 24)
    remains = time - days * (3600 * 24)
    hours = remains // 3600
    remains = remains - hours * 3600
    minutes = remains // 60 
    remains = remains - minutes * 60
    seconds = remains
    return (str(days) + " days, " + 
            str(hours) + " hours, " + 
            str(minutes) + " minutes, " + 
            str(seconds) + " seconds")