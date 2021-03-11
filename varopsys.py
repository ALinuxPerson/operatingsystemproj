import os
import time
import platform
from osclasses import *
from osys2alpha import *
import hashlib
import sys
import random

##########Variables Section##########
bios_model = "AMNITY BIOS Version 3.06b"
HDD_installed = 1
cpu_model = "Intel Ultron i56970K"
cpu_speed = "5.6 GHZ OC"
cpu_cores = "32"
sys_mem = "32 GB"
sys_mem_mb = "32768 MB"
sys_mem_mb_no_mb = 32768
os_on_HDD = True
first_boot = "CD/DVD Device"
second_boot = "Harddisk drive"
third_boot = "Removable Device"
fourth_boot = "Network"
is_oobe_finished = True
os_name = "OSys"
os_ver = "1.0"
os_name_ver = "OSys 1.0"
os_edition = "Personal"
osys_1_boot_name = os_name_ver
bootloader = "OSys Def. BTLDR Rev. 1.0.0"
name = ""
password = ""
oobe_name = "user"
#oobe_sha1_hash = hashlib.sha1(b, oobe_name)
#oobe_hash_digest = oobe_sha1_hash.hexdigest()
oobe_user_privilege = 2
oobe_pass = "password"
default_name = "admin"
#default_sha1_hash = hashlib.sha1(b, default_name)
#oobe_hash_digest = default_sha1_hash.hexdigest()
default_user_privilege = -1
default_password = "password"
test_user = "test"
test_password = "password"
rname = "root"
#oobe_hash_digest = "ROOTUSER"
sys_privilege = 0
rpass = "pass"
is_os_fucked = False
is_pc_on = False
do_you_want_pc_on = None
is_debug_options_on = True
user_currently_logged_on = False
is_os_dual_booted = True
how_much_os_installed = 2
os_priority = osys_1_boot_name

host = "Generic PC"
kernel = "OSys New Kernel"
shell = "placeholder"
DE = "-"
WM = "-"
####################

##########Classes Section##########
test_item = StoreItem(float(5.0), "Test Item", "Author") # Test Program
####################

##########Functions Section##########
def update_progress(progress):
    barLength = 10  # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength * progress))
    text = "\rPercent: [{0}] {1}% {2}".format("#" * block + "-" * (barLength - block), progress * 100, status)
    sys.stdout.write(text)
    sys.stdout.flush()


# clsar makes clearing text easier because it is cross-compatible with other operating systems.

def clsar():
    if platform.system() == "Windows":
        os.system('cls')
    elif platform.system() == "Linux" or "Darwin":
        os.system('clear')
    else:
        print("Unrecognized Operating System.")


# prog_bar makes a progress bar. required update_progress function.

def prog_bar(x):
    for i in range(101):
        time.sleep(x)
        update_progress(i / 100.0)


def invalid_input():
    print("ERROR: Invalid Input.")


def shutdown():
    time.sleep(0.5)
    clsar()
    print("Shutting down services...")
    time.sleep(0.25)
    print("Logging off user...")
    time.sleep(0.75)
    print("Shutting down...")
    time.sleep(6)
    is_pc_on = False
    sys.exit()

def logoff():
    time.sleep(1)
    print("Logging off...")
    for i in range(101):
        time.sleep(0.03)
        update_progress(i / 100.0)
    is_os_locked = True
    if user_currently_logged_on == "oobe":
        is_oobe_logged_in = False
    elif user_currently_logged_on == "default":
        is_default_logged_in = False
    else:
        print("Unknown or def null user.")
    clsar()
