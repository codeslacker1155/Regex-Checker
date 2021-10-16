import re
emails=['JamesBerkmire7821@yahoo.com','CharlesLongfist2829@gmail.com','BobHanson2347@icloud.com','FrankFogul291@gmail.com','JohnySchwab8291@outlook.com','GlenEarlmire271@icloud.com','DannyRomain1287@protonmail.com','PaulPhantom8723@protonmail.com']
passwords=['JumpingInTheCarAndRunning', 'F3n7&3bs@dBF', 'HavingFunInstallingBlinkerFluidInMyHeadlights', 'L3F^wW35&Fa#$R#1^56j1#1bf2a#rw23a#$@', '#&^@^&#%&!^&@#^&@*&^', '237405982750289762570209872509203598', '3amigos', '234232345']

print('Emails: ')
print('-'*30)

for i in emails:
    print(i)
    
print('\nSafe Passwords: ')
print('-'*30)

for i in passwords:
    search=re.findall('\W*',i)
    if i in search:
        print(i+'  --->  '+emails[passwords.index(i)])
