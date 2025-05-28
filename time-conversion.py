def timeConversion(s):
    hours = int(s[0] + s[1])
    minutes = s[3] + s[4]
    seconds = s[6] + s[7]
    ampm = s[8]

    if(hours >= 12 and ampm == 'A'):
        hours = hours - 12
    elif(hours < 12 and ampm == 'P'):
        hours = hours + 12
    
    if(hours < 10):
        return(f'0{hours}:{minutes}:{seconds}')
    else:
        return(f'{hours}:{minutes}:{seconds}')

hora = timeConversion("19:05:45AM")
print(hora)