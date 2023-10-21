#Matthew Repecki
# Cyber Defense Techniques, Fall 2023
# Team Bravo
import psutil
import time
bad_programs = ['wireshark','cmd','vim','terminal','bash','cmd']
def check_if_process_running(process_name,kill = False):
    '''
    :param process_name: Takes in process name
    :param kill: Boolean of to kill the process or not
    :return: Returns 0 if process not found and not killed, returns 1 if process is found but not killed, returns 2 if process is found and killed
    '''
    ret = 0
    for process in psutil.process_iter(['name']):
        print(process)
        if process_name in process.info['name'] or process.info['name'] in process_name :
            if kill:
                try:
                    process.kill()
                except:
                    continue
                ret += 1
            ret += 1
    return ret

def kill_bad_programs():
    while True:
        time.sleep(60)
        try:
            for program in bad_programs:
                print(check_if_process_running(program,True))
        except:
            kill_bad_programs()

kill_bad_programs()

