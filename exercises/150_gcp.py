__author__ = 'syedaali'

'''
Program to provide limited access to GCP for Network Operations Center.
First you must specify project, after that you can use the other commands.
'''
import subprocess
import sys


def error(s):
    print 'Error: ' + s


def show_menu():
    '''
    Shows the main menu
    :return: Numerical choice selected
    '''
    menu_d = {
        '1.': 'Set current project',
        '2.': 'List current project',
        '3.': 'List compute instances',
        '4.': 'List firewall rules',
        '5.': 'List zones',
        '6.': 'List regions',
        '7.': 'List images',
        '8.': 'List target pools',
        'q.': 'Quit'
    }

    print '-' * 80
    for k, v in sorted(menu_d.iteritems()):
        print k, v

    choice = raw_input("Enter your numerical choice: ")
    return choice


def set_project():
    '''
    Asks user for project name
    :return: prints the project name
    '''
    global project
    project = raw_input('Enter project name: ')
    cmd = 'gcloud config set project ' + project
    try:
        o = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError:
        pass
    else:
        print o


def print_project():
    '''
    Prints the project name
    :return:
    '''
    if check_project():
        print 'project is {}'.format(project)
    else:
        print 'Error: project is not defined'


def check_project():
    '''
    Checks if project is defined
    :return: True if project is defined, False otherwise
    '''
    if not project:
        return False
    else:
        return True


def list_compute_instances():
    '''
    Lists compute instances
    :return: Prints the instance names
    '''
    cmd = 'gcloud compute instances list --project ' + project
    try:
        o = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError:
        pass
    else:
        print o


def list_firewall_rules():
    '''
    Prints the firewall rules
    :return:
    '''
    cmd = 'gcloud compute firewall-rules list --project ' + project
    try:
        o = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError:
        pass
    else:
        print o


def list_zones():
    '''
    List project zones
    :return:
    '''
    cmd = 'gcloud compute zones list --project ' + project
    try:
        o = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError:
        pass
    else:
        print o


def list_regions():
    '''
    List project regions
    :return:
    '''
    cmd = 'gcloud compute regions list --project ' + project
    try:
        o = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError:
        pass
    else:
        print o


def list_images():
    '''
    List project images
    :return:
    '''
    cmd = 'gcloud compute images list --project ' + project
    try:
        o = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError:
        pass
    else:
        print o


def list_target_pools():
    '''
    List project target pools
    :return:
    '''
    cmd = ' gcloud compute target-pools list --project ' + project
    try:
        o = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError:
        pass
    else:
        print o


def main():
    '''
    Main point of entry, shows menu and calls functions depending upon choice
    :return:
    '''
    global project
    project = None

    while True:
        choice = show_menu()
        if choice == '1':
            set_project()
        elif choice == '2':
            print_project()
        elif choice == '3':
            if check_project():
                list_compute_instances()
            else:
                error('project is not defined')
        elif choice == '4':
            if check_project():
                list_firewall_rules()
            else:
                error('project is not defined')
        elif choice == '5':
            if check_project():
                list_zones()
            else:
                error('project is not defined')
        elif choice == '6':
            if check_project():
                list_regions()
            else:
                error('project is not defined')
        elif choice == '7':
            if check_project():
                list_images()
            else:
                error('project is not defined')
        elif choice == '8':
            if check_project():
                list_target_pools()
            else:
                error('project is not defined')
        elif choice == 'q':
            sys.exit(0)
        else:
            error("entry invalid")

if __name__ == '__main__':
    main()
