#!/usr/bin/env python3
#LAB 15 

message = 'Your Grade is '
print('Grading has been completed ')
Grade = float(input())
if Grade >= A 100-90:
    message = message + 'A 100-90.'
elif Grade >= 89-80:
    message = message + 'B.'
elif Grade >= 79-70:
    message = message + 'C.'
elif Grade >= 69-60:
    message = message + 'D.'
elif Grade <= 59:
    message = message + 'F.'
else:
    message = message + 'incomplete.'
print(message)


message = 'The movie is about to begin, we recommend '
print('What is your connection speed in Mbps?')
connection = float(input())
if connection >= 25:
    message = message + 'setting video to 4k.'
elif connection >= 5:
    message = message + 'setting video to 1080p.'
elif connection >= 2:
    message = message + 'setting video to 720p.'
else:
    message = message + 'finding another access network.'
print(message)



