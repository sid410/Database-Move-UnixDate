import linecache

# Function to shift time adding 132019200
def shiftUnixTime(current_line):

    list_line = list(current_line)

    timeText = "1566000000"
    timeList = list(timeText)
    iCopy = 0

    for i in range(-11, -2):
        timeList[iCopy] = list_line[i]
        iCopy += 1

    timeText = ''.join(timeList)
    timeShifted = int(timeText) + 132019200
    timeText = str(timeShifted)
    timeList = list(timeText)

    iPlace = 0

    for i in range(-11, -2):
        list_line[i] = timeList[iPlace]
        iPlace += 1

    current_line = ''.join(list_line)

    return current_line

### edit the file line by line
f = open("NOAA_data_timeshift.txt", "w")

for line in range(8):
    edit_line = linecache.getline('NOAA_data.txt', line + 1)
    f.write(edit_line)

for line in range(8, 76298):
    edit_line = linecache.getline('NOAA_data.txt', line + 1)
    edit_line = shiftUnixTime(edit_line)

    f.write(edit_line)

f.close()