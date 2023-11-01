from CLASS_ROMA import Grafo
from Minimize_ROME_Path import solve_Rome
import time

print('## ROME PATH MINIMIZER ##')
print('** Answer < Yes or No > **')
ask=input('Start The Program? ')
if ask=='yes' or ask=='Yes':
    ask=Grafo()
    d=ask.get_node_max()
    print('## This Program Provides Insights on Whether Reach ROMA at a Lower Cost or at a Shortest Time. ## ')
    file=input('Enter File Name With Data About Roads: ')
    try:
        ask.read_file(file)
        print('\nSummary of Roads With Related Data:')
        time.sleep(1)
        print(ask.out_graph())
        solve_Rome()
        print('** Answer < Yes or No > **')
        end = input('Close The Program?')
        if end == 'yes':
            print('\n## Program Closed ##')
            quit()
        else:
            solve_Rome()
            print('\n## Program Closed ##')
    except:
        print('Warning: No Such File Available')



