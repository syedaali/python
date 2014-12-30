__author__ = 'syedaali'

'''
Program to provide limited access to GCP for Network Operations Center.
First you must specify project, after that you can use the other commands.
'''
import subprocess
import sys
import re
import signal


def error(s):
    print 'ERROR: ' + s


def sig_handler(signum, stack):
    '''
    :param signum:
    :param stack:
    :return:
    '''
    sig_name = next(v for v, k in signal.__dict__.iteritems() if k == signum)
    print '\nReceived {0}, quitting'.format(sig_name)
    sys.exit(0)


def check_version():
    cmd = 'gcloud --version'
    try:
        o = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError:
        error('unable to check Google SDK version')
        sys.exit(1)
    else:
        if re.match('Google Cloud SDK 0.9.40', o):
            print "Found compatible Google SDK version"
            return True
    return False


def show_menu():
    '''
    Shows the main menu
    :return: Numerical choice selected
    '''
    menu_d = {
        'a.': 'Set current project',
        'b.': 'List current project',
        'c.': 'List compute instances',
        'd.': 'List firewall rules',
        'e.': 'List zones',
        'f.': 'List regions',
        'g.': 'List images',
        'h.': 'List target pools',
        'i.': 'Check cloud authentication',
        'j.': 'List addresses',
        'q.': 'Quit'
    }

    print '-' * 80
    print 'SELECT a letter: '
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
        error('Set current project first')


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


def check_cloud_auth():
    '''
    Check users credentials on GCP
    :return:
    '''
    cmd = 'gcloud auth list'
    try:
        o = subprocess.check_output(cmd, shell=True)
    except subprocess.CalledProcessError:
        pass
    else:
        print o


def list_address():
    '''
    Check users credentials on GCP
    :return:
    '''
    cmd = 'gcloud compute addresses list --project ' + project
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

    signal.signal(signal.SIGINT, sig_handler)

    global project
    project = None

    if check_version():
        pass
    else:
        error('Incompatible SDK version, need 0.9.40')
        sys.exit(0)

    while True:
        choice = show_menu()
        if choice == 'a':
            set_project()
        elif choice == 'b':
            print_project()
        elif choice == 'c':
            if check_project():
                list_compute_instances()
            else:
                error(' Set current project first')
        elif choice == 'd':
            if check_project():
                list_firewall_rules()
            else:
                error(' Set current project first')
        elif choice == 'e':
            if check_project():
                list_zones()
            else:
                error(' Set current project first')
        elif choice == 'f':
            if check_project():
                list_regions()
            else:
                error(' Set current project first')
        elif choice == 'g':
            if check_project():
                list_images()
            else:
                error(' Set current project first')
        elif choice == 'h':
            if check_project():
                list_target_pools()
            else:
                error(' Set current project first')
        elif choice == 'i':
            check_cloud_auth()
        elif choice == 'j':
            if check_project():
                list_address()
            else:
                error(' Set current project first')
        elif choice == 'q':
            sys.exit(0)
        else:
            error("entry invalid")

if __name__ == '__main__':
    main()
