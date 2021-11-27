import random
status = ['clean', 'dirty']
location = ['A', 'B']
action = ['suck', 'nothing']

def Reflex_Vacuum_Agent(locat,status,action):
    loc = locat[random.randint(0, 1)]
    stts = status
    while stts != ['clean', 'clean']:
        stts = status
        state_A = stts[random.randint(0, 1)]
        state_B = stts[random.randint(0, 1)]
        if state_A != 'clean':
            act = action[0]
            print(f"\nA is {state_A} Do {act} ")
            state_A = stts[0]
            loc = locat[1]
            act = action[1]
            print(f"\nA is {state_A} Do {act} ")
            print(f"\nNow location is {loc}")
            if state_B == 'clean':
                act = action[1]
                print(f"\nB is {state_B} Do {act} ")
                print('Both rooms are clean now')
                stts=[state_A,state_B]
            else:
                continue
        elif state_A == 'clean':
            act=action[1]
            print(f"\nA is {state_A} Do {act} ")
            loc = locat[1]
            print(f"\nNow location is {loc}")
            if state_B == 'clean':
                act = action[1]
                print(f"\nB is {state_B} Do {act} ")
                print('Both rooms are clean now')
                stts=[state_A,state_B]
            else:
                continue
        elif state_B != 'clean':
            act = action[0]
            print(f"\nB is {state_B} Do {act} ")
            state_B = stts[1]
            loc = locat[0]
            print(f"\nB is {state_B} Do {act} ")
            print(f"\nNow location is {loc}")
            if state_A == 'clean':
                act = action[1]
                print(f"\nA is {state_A} Do {act} ")
                print('Both rooms are clean now')
                stts=[state_A,state_B]
            else:
                continue
        elif state_B == 'clean':
            act = action[1]
            print(f"\nB is {state_B} Do {act} ")
            loc = locat[0]
            print(f"\nNow location is {loc}")
            if state_A == 'clean':
                act = action[1]
                print(f"\nA is {state_A} Do {act} ")
                print('Both rooms are clean now')
                stts=[state_A,state_B]
            else:
                continue
                
Reflex_Vacuum_Agent(location,status,action)