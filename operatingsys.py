#################################
#NOTE: This program is basically#
#a bunch of if statements, while#
#loops and variables. It really #
#needs some improvement.        #
#################################

# NOTE: If I can't solve this problem in time, then it looks like
# I have to fucking get this stupid shit out of my life. Besides,
# i'm just self-learning. I can quit anytime. Also, quit this
# project. Not quitting learning python. Python is like your
# frenemy.

from varopsys import *

clsar()
do_you_want_pc_on = True
is_pc_on = True
while is_pc_on is True:
    a = input("Press the enter key to boot from cd or dvd, or if you have an OS installed i...")
    if a == "":
        time.sleep(2)
        clsar()
        setup_box_1 = input("Welcome to setup!\n"
                            "The operating system you are trying to install is OSys 1.0.\n" 
                            "Press the enter key if you want to select a harddrive.")
        if_invalid_input = False # By default, once you go to the first setup screen, this is automatically false.
        HDD_format_chosen = False
        while HDD_format_chosen is False:
            if setup_box_1 == "":
                HDD_format_chosen = True
                time.sleep(0.5)
                HDD_format1 = input("ERROR: No harddrives are formatted. Do you want to format one?: ")
                if HDD_format1 == "yes":
                    is_hdd_formatted = False
                    while is_hdd_formatted is False:
                        time.sleep(0.5)
                        fdisk_box = input("1. Create a logical HDdrive\n"
                                        "2. Set a partition as active\n"
                                        "3. Delete a logical HDdrive\n"
                                        ""
                                        "Type the number you want.: ")
                        if fdisk_box == "1":
                            if HDD_installed == 1:
                                is_hdd_formatted = True
                                print("Create a logical HDdrive\n"
                                    "Curent Fixed Drive: " + str(HDD_installed) + " \nFormatting Drive...")
                                for i in range(101):
                                    time.sleep(0.1)
                                    update_progress(i / 100.0) # Once it reaches 100, it is 10 seconds long.
                                reboot = input("Do you want to reboot?: ")
                                if reboot == "yes":
                                    print("OK, rebooting...")
                                    os_on_HDD = True
                                    time.sleep(10)
                            elif HDD_installed > 1:
                                print("Create a logical HDdrive\n"
                                    "Curent Fixed Drive: " + str(HDD_installed))
                                while True:
                                    hdd_selection = input("There are " + str(HDD_installed) + " hard drives in this computer.\n"
                                                                                            "What hard drive would you like to format?: ")
                                    print("Formatting drive " + hdd_selection + "...")
                                    time.sleep(10)
                                    print("100%")
                                    reboot = input("Do you want to reboot?: ")
                                    if reboot == "yes":
                                        print("OK, rebooting...")
                                        os_on_HDD = True
                                        time.sleep(10)

                elif HDD_format1 == "no":
                    print("You cannot continue without formatting your hard drive.\nSetup will now halt.")  # TODO: While loops.
                else:
                    print("Command not recognized.\nSetup will now halt.") # Broken else statement.
            elif if_invalid_input == False:
                print("Command Not Recognized.\nSetup will now halt.")
                break
            else:
                if_invalid_input = True # Apparently this doesn't print it.
                print("ERROR: Invalid Input.")
    elif a == "9":
        BIOS_settings = input("Welcome to the BIOS settings. what would you like to do?>")
        if BIOS_settings == "goto Main":
            BIOS_settings == input("##########\nMain Screen\n##########\n"
                                   "#####BIOS Model#####\n"
                                   + bios_model + "\n#####Processor#####\n"
                                   + cpu_model +"\n"
                                   + cpu_speed + "\n"
                                   + cpu_cores + "#####System Memory#####\n"
                                   + sys_mem +
                                   "\nWhat would you like to do?>")  # Main Menu Screen
        elif BIOS_settings == "goto Advanced":
            BIOS_settings == input("#####\nIntel Advanced Configuration\n"
                                "matt leave options here pls\n"
                                "What would you like to do?>") # Advanced Menu Screen
        elif BIOS_settings == "goto Boot":
            BIOS_settings == input("First boot device: " + first_boot +
                                "\nSecond boot device: " + second_boot +
                                "\nThird boot device: " + third_boot +
                                "\nFourth boot device: " + fourth_boot +
                                "\nWhat would you like to do?>")
    elif a == "i":
        if os_on_HDD is True and is_oobe_finished is False:
            print("Please wait while "+ os_name_ver +" is preparing for the out of box experience...")
            time.sleep(1)
            clsar()
            print("Welcome to " + os_name_ver + "!")
            print("This setup will guide you to configuring your machine and setting it up for personal use.")
            print("First of all, state your name.")
            name = input("Enter your name: ")
            password = input("Enter your password: ")
            time.sleep(1)
            auto_updates = input("Do you want to recieve automatic updates?: ")
            if auto_updates == "yes":
                print("You will now recieve automatic updates.")
            elif auto_updates == "no":
                sure = input("Are you sure? This will expose your computer to security vulnerabilities.\n"
                            "Are you sure you want to continue?")
                if sure == "yes":
                    print("You will no longer be recieving automatic updates.")
                elif sure == "no":
                    print("You will now recieve automatic updates.")
                else:
                    print("ERROR: Command not recognized.")
            else:
                print("ERROR: Command not recognized.")
            input("You have now configured your computer for personal use. This computer will now reboot.")
            is_oobe_finished = True
            time.sleep(1)
            pass
        elif is_os_dual_booted is True and os_priority == osys_1_boot_name:
            if os_on_HDD == True and is_oobe_finished == True:
                user_currently_logged_on = "oobe"
                clsar()
                print("Please wait while " + os_name_ver + " is starting up...")
                boot_up_time = random.randint(1, 5)
                time.sleep(boot_up_time)
                is_os_locked = True
                while is_os_locked is True:
                    print("#####" + os_name_ver + " Log In#####")
                    print("Please input your credentials.")
                    name = input("Name: ")
                    password = input("Password: ")
                    if name == oobe_name and password == oobe_pass:
                        clsar()
                        print("Logging in to " + os_name_ver + "...")
                        clsar()
                        is_os_locked = False
                        time.sleep(5)
                        print("OSys Command Line")
                        is_oobe_logged_in = True
                        while is_oobe_logged_in is True:
                            console = input("~:\>")
                            if console == "cls":
                                clsar()
                            elif console == "mkdir":
                                print("placeholder")  # I really don't know how to implement this without rewriting this OS.
                            elif console == "help":
                                print("####Help Menu####\n" # The ones that have ### aren't implemented yet.
                                      "NOTE: The ones that have // require privileges lower than 2.\n"  
                                      "mkdir: Makes a directory.\n"  ###
                                      "help: Displays this menu.\n"
                                      "rm: Deletes a directory.\n"  ###
                                      "ren: Renames a directory.\n"  ###
                                      "whoami: Prints the current user.\n"
                                      "sysinfo: Displays info about your PC.\n"
                                      "ram: Displays how many RAM you have.\n"
                                      "debug: Computer debugging purposes only. //\n"
                                      "switch: Enables you to switch from inside to outside OS. //\n"
                                      "cls: Clears screen.\n"
                                      "calc: Calculator.\n"
                                      "install: Allows you to install programs. //")
                            elif console == "rm -rf / --no-preserve-root":
                                print("Deleting Recursively OBJ-NAME%/23653 of files...")
                                time.sleep(60)
                                print("ERROR: Unable to delete all files.")
                                print("ERROR: Unable to retrieve file or directory.\n"
                                      "RFP_ERR: Several critical files were either damaged or deleted\n."
                                      "Please check this installation against your os_name_ver os_edition CD.\n"
                                      ""
                                      "WARNING: Syntax error in one or more files.\n"
                                      "WARNING: Current System Process has become unstable.\n"
                                      "os_name_ver may not work correctly unless you restart your computer.\n"
                                      "Unknown Error in file ///.")
                                break
                            elif console == "sysinfo":
                                print("OS: " + os_name_ver + "\nHost: " + host + "\nKernel: " + kernel)
                            elif console == "":
                                print("")
                            elif console == "whoami":
                                print("You are user " + default_name + ".")
                            elif console == "ram":
                                if sys_mem_mb_no_mb > 32769:
                                    print("ERROR: Local System Buffer Error on Adress 0x0019CBD.\n"
                                          "There may be not enough ram in your PC.\n"
                                          "STP_CODE: LOCAL_SYS_BUFFR_OVRFLW")
                                    time.sleep(5)
                                    clsar()
                                    print(
                                        os_name_ver + " has not recovered from the following system buffer protection error."
                                                      "The System Process cannot continue.\n"
                                                      "System Halted.")
                                    break
                                elif sys_mem_mb_no_mb <= 32768:
                                    print(sys_mem)
                            elif console == "debug":
                                if oobe_user_privilege <= 1:
                                    is_debug_program_active = True
                                    print("Tool for debugging operating system.")
                                    while is_debug_program_active is True:
                                        debug_console = input("DEBUG>")
                                        if debug_console == "crash":
                                            time.sleep(5)
                                            print("KERNL_FAILUR_ERR: A CRASH_INTENTIONAL stop error has ocurred.\n"
                                                  "Due to this, " + os_name_ver + " cannot continue.\nSystem Halted.")
                                            is_pc_on = False
                                            is_debug_program_active = False
                                        elif debug_console == "boottime":
                                            if boot_up_time > 1:
                                                print(str(boot_up_time) + " seconds.")
                                            elif boot_up_time < 1:
                                                print(str(boot_up_time) + " seconds.")
                                            elif boot_up_time is 1:
                                                print(str(boot_up_time) + " second.")
                                        elif debug_console == "exit":
                                            is_debug_program_active = False
                                        elif debug_console == "list process":
                                            print("===List of currently running processes===\n"
                                                  "debug\n"
                                                  "kernel\n"
                                                  "list[args(process)]\n"
                                                  "console")
                                        elif debug_console == "enable debug_options":
                                            print(
                                                "WARNING: Do not enable debug options unless you know what you're doing.\n"
                                                ""
                                                "Debug Options Enabled.")
                                            is_debug_options_on = True
                                        elif debug_console == "disable debug_options":
                                            print("Debug Options Disabled.")
                                            is_debug_options_on = False
                                        elif debug_console == "help":
                                            print("===Help Menu===\n"
                                                  "crash: Crashes your system.\n"
                                                  "Do not try to crash your system as it could result to unsaved data.\n"
                                                  "boottime: Tells how many seconds did it take to boot up your pc.\n"
                                                  "exit: Exits debug.\n"
                                                  "list: Requires argument.\n"
                                                  "    process: lists the processes.\n"
                                                  "enable: Enables certain tools in your os. Requires argument.\n"
                                                  "    debug_options: Enables true administrative privileges.\n"
                                                  "disable: Opposite of the above command. Required argument.\n"
                                                  "    debug_options: Opposite of the above argument.\n"
                                                  "attach: Enables you to attach to a process in order to debug it.\n")
                                        elif debug_console == "attach":
                                            is_attach_subprocess_active = True
                                            print("What process would you like to attach to?")
                                            while is_attach_subprocess_active:
                                                attach_console = input("DEBUG\ATTACH>")
                                                if attach_console == "list process":
                                                    print("===List of currently running processes===\n"
                                                          "debug\n"
                                                          "kernel\n"
                                                          "list[args(process)]\n"
                                                          "console\n"
                                                          "attach")
                                                elif attach_console == "break":
                                                    print("Exiting...")
                                                    is_attach_subprocess_active = False
                                                elif attach_console == "debug" or "kernel" or "console" or "attach":
                                                    print("Attached to process " + attach_console + ".")
                                                else:
                                                    print("ERROR: Invalid Input.")
                                        else:
                                            print("ERROR: Invalid Input.")
                                else:
                                    print("ERROR: Privileges not applicable for this user.")
                            elif console == "switch --realuser":
                                if oobe_user_privilege <= 1:
                                    time.sleep(0.5)
                                    print("Please wait...")
                                    time.sleep(3.75)
                                    clsar()
                                    print("Real User Mode is a mode where you access\n"
                                          "commands outside of the operating system\n"
                                          "you are using. The inside OS is " + os_name_ver + ".\n"
                                          "The outside OS is " + platform.system() + ".\n")
                                    while True:
                                        rum = input("RUM:\>")
                                        os.system(rum)
                                else:
                                    print("ERROR: Privileges not applicable for this user.")
                            elif console == "osfirsttimerpython":
                                print("Decided to take a 'challenge'.")
                                osftname = input("Input your name: ")
                                osftage = input("Input your age: ")
                                osftbrosis = input("How many brothers or sisters do you have?: ")
                                print(
                                    "Your name is " + osftname + ". Your age is " + osftage + ". You have " + osftbrosis + " brothers or sisters.")
                            elif console == "listprogram":
                                is_list_program_active = True
                                print("This is a list program. This program is used to test the\n"
                                      "list feature in python.")
                                while is_list_program_active is True:
                                    list_input = input("LIST>")
                                    if list_input == "exit":
                                        print("Program is no longer active.")
                                        is_list_program_active = False
                                    else:
                                        print("ERROR: Invalid Input.")
                            elif console == "address_book":
                                print("===" + os_name + " Address Book===\n"
                                      "Revision 1.0.0\n"
                                      "\n"
                                      "Address book for storing contacts. Can store 3 contacts at a time.")
                                is_address_book_program_active = True
                                while is_address_book_program_active is True:
                                    addr_book_console = input("CONTACTS>")
                                    if addr_book_console == "create":
                                        is_create_contact_active = True
                                        while is_create_contact_active is True:
                                            print("Insert first name.")
                                            addr_book_first1 = input("CONTACTS\CREATE>")
                                            print("Insert middle initial.")
                                            addr_book_middle1 = input("CONTACTS\CREATE>")
                                            print("Insert last name.")
                                            addr_book_last1 = input("CONTACTS\CREATE>")
                                            print(addr_book_first1 + addr_book_middle1 + addr_book_last1)
                                            addr_book_console = input("Is this correct?>")
                                            if addr_book_console == "y" or "Y" or "yes":
                                                print("Insert phone number.")
                                                addr_book_phone = input("CONTACTS\CREATE>")
                                                print("Insert email.")
                                                addr_book_email = input("CONTACTS\CREATE>")
                                                addr_book_person1 = Person(addr_book_first1, addr_book_middle1, addr_book_last1, "", addr_book_phone, addr_book_email)
                                                addr_book_person1.contact_introduce()
                                                addr_book_confirm = input("Is the following info correct?>")
                                                if addr_book_confirm == "y" or "Y" or "yes":
                                                    print("Contact successfully created.")
                                                    is_create_contact_active = False
                                                elif addr_book_confirm == "n" or "N" or "no":
                                                    print("Placeholder")
                                                else:
                                                    invalid_input()
                                            else:
                                                invalid_input()
                                    elif addr_book_console == "exit":
                                        break
                                    else:
                                        invalid_input()
                            elif console == "install":
                                if oobe_user_privilege <= 1:
                                    is_install_program_active = True
                                    print("What program would you like to install?\n"
                                          "NOTE: Requires CD/DVD Media.")
                                    install_program_console = input("INSTALL>")
                                    if install_program_console == "list programs":
                                        print("===List of programs installed===\n"
                                              "No programs are installed.\n"
                                              "::RESTRICTED ACCESS::\n"
                                              "OSys New Kernel\n"
                                              "OSys Console\n"
                                              "OSys Internal Programs ::")
                                    elif install_program_console == "install osys_program_unlabeled":
                                        print("You are trying to install osys_program_unlabeled.\n"
                                              "Are you sure you want to continue?")
                                        yes_no_input = input("Y/N>")
                                        if yes_no_input == "y" or "Y":
                                            print("Installing program...")
                                            print("A reboot is required. Would you like to reboot now?")
                                            yes_no_input = input("Y/N>")
                                            if yes_no_input == "y" or "Y":
                                                clsar()
                                                print("Rebooting...")
                                                time.sleep(5)
                                                is_pc_on = False
                                                is_default_logged_in = False
                                                is_install_program_active = False
                                    elif install_program_console == "osinstall":
                                        print("===OS Installer===\n"
                                              "Bootloader: " + bootloader)
                                        print("\n"
                                              "Allows you to install different operating systems.")
                                        is_os_install_subprocess_active = True
                                        while is_os_install_subprocess_active is True:
                                            os_install_console = input("OSINSTALL>")
                                            if os_install_console == "osys_ver_2.0":
                                                print("======================\n"
                                                      "Select revision of os.\n"
                                                      "======================\n"
                                                      "VER_2.0_ALPHA_REV_2.04\n"
                                                      ""
                                                      "Use numbers 1 thru 10 for\n"
                                                      "selection.")
                                                os_install_console = input("REVSELECT>")
                                                if os_install_console == "1":
                                                    clsar()
                                                    time.sleep(1)
                                                    print("You are going to install OSYS_VER_2.0_ALPHA_REV_2.04.\n"
                                                          "Are you sure you want to continue?")
                                                    os_install_console = input("Y/N>")
                                                    if os_install_console == "Y":
                                                        print("Dual boot or wipe drive?\n"
                                                              "Use numbers 1 thru 2 for selection.")
                                                        os_inst_type = input("1/2>")
                                                        if os_inst_type == 1:
                                                            clsar()
                                                            print("Please wait while " + os_name_ver + "\n"
                                                                  "sets up your computer for dual boot config\n"
                                                                  "and dual os install...")
                                                            time.sleep(5)
                                                            clsar()
                                                            print("Please wait while we grab os install iso for\n"
                                                                  "download and installation...")
                                                            random_dl = random.uniform(0.4, 0.9)
                                                            clsar()
                                                            time.sleep(1)
                                                            print("Size: 110 MB")
                                                            print("During download and installation, using your computer\n"
                                                                  "is as of yet not possible. Please be patient.")
                                                            prog_bar(random_dl)
                                                            time.sleep(1)
                                                            clsar()
                                                            print("Installing os...")
                                                            prog_bar(0.6)

                                else:
                                    print("ERROR: Privileges not applicable for this user.")
                            elif console == "calc":
                                is_calc_program_active = True
                                print("===CALCULATOR ANSWERER===")
                                is_operator_chosen = False
                                while is_operator_chosen is False and is_calc_program_active is True:
                                    oprtn = input("What operator would you like to choose: ")
                                    if oprtn == "multiply":
                                        is_operator_chosen = True
                                        try:
                                            print("You chose multiplication.")
                                            num1 = float(input("Pick a number:"))
                                            num2 = float(input("Pick another number:"))
                                            print(num1 * num2)
                                            is_calc_program_active = False
                                        except:
                                            print("ERROR: Not a number.")
                                    elif oprtn == "subtract":
                                        is_operator_chosen = True
                                        try:
                                            print("You chose subtraction.")
                                            num1 = float(input("Pick a number:"))
                                            num2 = float(input("Pick another number:"))
                                            print(num1 - num2)
                                            is_calc_program_active = False
                                        except:
                                            print("ERROR: Not a number.")
                                    elif oprtn == "add":
                                        try:
                                            print("You chose addition.")
                                            num1 = float(input("Pick a number:"))
                                            num2 = float(input("Pick another number:"))
                                            print(num1 + num2)
                                            is_calc_program_active = False
                                        except:
                                            print("ERROR: Not a number.")
                                    elif oprtn == "divide":
                                        try:
                                            print("You chose division.")
                                            num1 = float(input("Pick a number:"))
                                            num2 = float(input("Pick another number:"))
                                            print(num1 / num2)
                                            is_calc_program_active = False
                                        except ZeroDivisionError:
                                            print("ERROR: Division by zero is not allowed.")
                                        except:
                                            print("ERROR: Not a number.")
                                    else:
                                        print("ERROR: Invalid Input. You can only do multiply, subtract, add or divide.")
                            elif console == "logoff":
                                time.sleep(1)
                                print("Logging off...")
                                prog_bar(0.03)
                                is_os_locked = True
                                is_default_logged_in = False
                                clsar()
                            elif console == "shutdown":
                                time.sleep(0.5)
                                clsar()
                                print("Shutting down services...")
                                time.sleep(0.25)
                                print("Logging off user...")
                                time.sleep(0.75)
                                print("Shutting down...")
                                time.sleep(6)
                                is_power_supply_on = False
                                break
                            else:
                                print("ERROR: Invalid Input.")
                    elif name == default_name and password == default_password:
                        user_currently_logged_on = "default"
                        clsar()
                        print("Logging in to " + os_name_ver + "...")
                        is_os_locked = False
                        time.sleep(5)
                        print("NOTE: Administrative Privileges Enabled.")
                        print("OSys Command Line")
                        is_default_logged_in = True
                        while is_default_logged_in is True:
                            console = input("~:\>")
                            if console == "cls":
                                clsar()
                            elif console == "mkdir":
                                print("placeholder") # I really don't know how to implement this without rewriting this OS.
                            elif console == "help":
                                print("####Help Menu####\n"
                                      "NOTE: The ones that have //"  # The ones that have 3 # aren't implemented yet.
                                      "mkdir: Makes a directory.\n" ###
                                      "help: Displays this menu.\n"
                                      "rm: Deletes a directory.\n" ###
                                      "ren: Renames a directory.\n" ###
                                      "whoami: Prints the current user.\n"
                                      "sysinfo: Displays info about your PC.\n"
                                      "ram: Displays how many RAM you have.\n"
                                      "debug: Computer debugging purposes only.\n"
                                      "switch: Enables you to switch from inside to outside OS.\n"
                                      "cls: Clears screen.\n"
                                      "calc: Calculator.")
                            elif console == "rm -rf / --no-preserve-root":
                                print("Deleting Recursively OBJ-NAME%/23653 of files...")
                                time.sleep(60)
                                print("ERROR: Unable to delete all files.")
                                print("ERROR: Unable to retrieve file or directory.\n"
                                    "RFP_ERR: Several critical files were either damaged or deleted\n."
                                    "Please check this installation against your os_name_ver os_edition CD.\n"
                                    ""
                                    "WARNING: Syntax error in one or more files.\n"
                                    "WARNING: Current System Process has become unstable.\n"
                                    "os_name_ver may not work correctly unless you restart your computer.\n"
                                    "Unknown Error in file ///.")
                                break
                            elif console == "sysinfo":
                                print("OS: " + os_name_ver + "\nHost: " + host + "\nKernel: " + kernel)
                            elif console == "address_book":
                                print("===" + os_name + " Address Book===\n"
                                      "Revision 1.0.0\n"
                                      "\n"
                                      "Address book for storing contacts. Can store 3 contacts at a time.")
                                is_address_book_program_active = True
                                while is_address_book_program_active is True:
                                    addr_book_console = input("CONTACTS>")
                                    if addr_book_console == "create":
                                        is_create_contact_active = True
                                        while is_create_contact_active is True:
                                            print("Insert first name.")
                                            addr_book_first1 = input("CONTACTS\CREATE>")
                                            print("Insert middle initial.")
                                            addr_book_middle1 = input("CONTACTS\CREATE>")
                                            print("Insert last name.")
                                            addr_book_last1 = input("CONTACTS\CREATE>")
                                            print(addr_book_first1 + addr_book_middle1 + addr_book_last1)
                                            addr_book_console = input("Is this correct?>")
                                            if addr_book_console == "y" or "Y" or "yes":
                                                print("Insert phone number.")
                                                addr_book_phone = input("CONTACTS\CREATE>")
                                                print("Insert email.")
                                                addr_book_email = input("CONTACTS\CREATE>")
                                                addr_book_person1 = Person(addr_book_first1, addr_book_middle1, addr_book_last1, "", addr_book_phone, addr_book_email)
                                                addr_book_person1.contact_introduce()
                                                addr_book_confirm = input("Is the following info correct?>")
                                                if addr_book_confirm == "y" or "Y" or "yes":
                                                    print("Contact successfully created.")
                                                    is_create_contact_active = False
                                                elif addr_book_confirm == "n" or "N" or "no":
                                                    print("Placeholder")
                                                else:
                                                    invalid_input()
                                            else:
                                                invalid_input()
                                    elif addr_book_console == "exit":
                                        break
                                    else:
                                        invalid_input()
                            elif console == "":
                                print("")
                            elif console == "whoami":
                                print("You are user " + default_name + ".")
                            elif console == "ram":
                                if sys_mem_mb_no_mb > 32769:
                                    print("ERROR: Local System Buffer Error on Adress 0x0019CBD.\n"
                                        "There may be not enough ram in your PC.\n"
                                        "STP_CODE: LOCAL_SYS_BUFFR_OVRFLW")
                                    time.sleep(5)
                                    clsar()
                                    print(os_name_ver + " has not recovered from the following system buffer protection error."
                                                        "The System Process cannot continue.\n"
                                                        "System Halted.")
                                    break
                                elif sys_mem_mb_no_mb <= 32768:
                                    print(sys_mem)
                            elif console == "debug":
                                if default_user_privilege <= 1:
                                    is_debug_program_active = True
                                    print("Tool for debugging operating system.")
                                    while is_debug_program_active is True:
                                        debug_console = input("DEBUG>")
                                        if debug_console == "crash":
                                            time.sleep(5)
                                            print("KERNL_FAILUR_ERR: A CRASH_INTENTIONAL stop error has ocurred.\n"
                                                "Due to this, " + os_name_ver + " cannot continue.\nSystem Halted.")
                                            is_pc_on = False
                                            is_debug_program_active = False
                                        elif debug_console == "boottime":
                                            if boot_up_time > 1:
                                                print(str(boot_up_time) + " seconds.")
                                            elif boot_up_time <1:
                                                print(str(boot_up_time) + " seconds.")
                                            elif boot_up_time is 1:
                                                print(str(boot_up_time) + " second.")
                                        elif debug_console == "exit":
                                            is_debug_program_active = False
                                        elif debug_console == "list process":
                                            print("===List of currently running processes===\n"
                                                  "debug\n"
                                                  "kernel\n"
                                                  "list[args(process)]\n"
                                                  "console")
                                        elif debug_console == "enable debug_options":
                                            print("WARNING: Do not enable debug options unless you know what you're doing.\n"
                                                  ""
                                                  "Debug Options Enabled.")
                                            is_debug_options_on = True
                                        elif debug_console == "disable debug_options":
                                            print("Debug Options Disabled.")
                                            is_debug_options_on = False
                                        elif debug_console == "help":
                                            print("===Help Menu===\n"
                                                  "crash: Crashes your system.\n"
                                                  "Do not try to crash your system as it could result to unsaved data.\n"
                                                  "boottime: Tells how many seconds did it take to boot up your pc.\n"
                                                  "exit: Exits debug.\n"
                                                  "list: Requires argument.\n"
                                                  "    process: lists the processes.\n"
                                                  "enable: Enables certain tools in your os. Requires argument.\n"
                                                  "    debug_options: Enables true administrative privileges.\n"
                                                  "disable: Opposite of the above command. Required argument.\n"
                                                  "    debug_options: Opposite of the above argument.\n"
                                                  "attach: Enables you to attach to a process in order to debug it.\n")
                                        elif debug_console == "attach":
                                            is_attach_subprocess_active = True
                                            print("What process would you like to attach to?")
                                            while is_attach_subprocess_active:
                                                attach_console = input("DEBUG\ATTACH>")
                                                if attach_console == "list process":
                                                    print("===List of currently running processes===\n"
                                                        "debug\n"
                                                        "kernel\n"
                                                        "list[args(process)]\n"
                                                        "console\n"
                                                        "attach")
                                                elif attach_console == "break":
                                                    print("Exiting...")
                                                    is_attach_subprocess_active = False
                                                elif attach_console == "debug" or "kernel" or "console" or "attach":
                                                    print("Attached to process " + attach_console + ".")
                                                else:
                                                    print("ERROR: Invalid Input.")
                                        else:
                                            print("ERROR: Invalid Input.")
                                else:
                                    print("ERROR: Privileges not applicable for this user.")
                            elif console == "switch --realuser":
                                if default_user_privilege <= 1:
                                    time.sleep(0.5)
                                    print("Please wait...")
                                    time.sleep(3.75)
                                    clsar()
                                    print("Real User Mode is a mode where you access\n"
                                        "commands outside of the operating system\n"
                                        "you are using. The inside OS is " + os_name_ver + ".\n"
                                        "The outside OS is " + platform.system() + ".\n")
                                    while True:
                                        rum = input("RUM:\>")
                                        os.system(rum)
                                else:
                                    print("ERROR: Privileges not applicable for this user.")
                            elif console == "osfirsttimerpython":
                                print("Decided to take a 'challenge'.")
                                osftname = input("Input your name: ")
                                osftage = input("Input your age: ")
                                osftbrosis = input("How many brothers or sisters do you have?: ")
                                print("Your name is " + osftname + ". Your age is " + osftage + ". You have " + osftbrosis + " brothers or sisters.")
                            elif console == "listprogram":
                                is_list_program_active = True
                                print("This is a list program. This program is used to test the\n"
                                      "list feature in python.")
                                while is_list_program_active is True:
                                    list_input = input("LIST>")
                                    if list_input == "exit":
                                        print("Program is no longer active.")
                                        is_list_program_active = False
                                    else:
                                        print("ERROR: Invalid Input.")
                            elif console == "textedit": # Do not know what i should do
                                is_textedit_program_active = True
                                text_name = {}
                                print("Text Editor")
                                while is_textedit_program_active is True:
                                    text_name_console = input("TXTEDIT>")
                                    if text_name_console == "create":
                                        print("Name of text file?")
                                        txtnmcon_sub_dict_name = input("TXTEDIT\CREATE>")
                                        break
                            elif console == "install":
                                if default_user_privilege <= 1:
                                    is_install_program_active = True
                                    print("What program would you like to install?\n"
                                          "NOTE: Requires CD/DVD Media.")
                                    install_program_console = input("INSTALL>")
                                    if install_program_console == "list programs":
                                        print("===List of programs installed===\n"
                                              "No programs are installed.\n"
                                              "::RESTRICTED ACCESS::\n"
                                              "OSys New Kernel\n"
                                              "OSys Console\n"
                                              "OSys Internal Programs ::")
                                    elif install_program_console == "install osys_program_unlabeled":
                                        print("You are trying to install osys_program_unlabeled.\n"
                                          "Are you sure you want to continue?")
                                        yes_no_input = input("Y/N>")
                                        if yes_no_input == "y" or "Y":
                                            print("Installing program...")
                                            print("A reboot is required. Would you like to reboot now?")
                                            yes_no_input = input("Y/N>")
                                            if yes_no_input == "y" or "Y":
                                                clsar()
                                                print("Rebooting...")
                                                time.sleep(5)
                                                is_pc_on = False
                                                is_default_logged_in = False
                                                is_install_program_active = False
                                    elif install_program_console == "osinstall":
                                        print("===OS Installer===\n"
                                              "Bootloader: " + bootloader)
                                        print("\n"
                                              "Allows you to install different operating systems.")
                                        is_os_install_subprocess_active = True
                                        while is_os_install_subprocess_active is True:
                                            os_install_console = input("OSINSTALL>")
                                            if os_install_console == "osys_ver_2.0":
                                                print("======================\n"
                                                      "Select revision of os.\n"
                                                      "======================\n"
                                                      "VER_2.0_ALPHA_REV_2.04\n"
                                                      ""
                                                      "Use numbers 1 thru 10 for\n"
                                                      "selection.")
                                                is_revselect_subprocess_active = True
                                                while is_revselect_subprocess_active is True:
                                                    os_install_console = input("REVSELECT>")
                                                    if os_install_console == "1":
                                                        clsar()
                                                        time.sleep(1)
                                                        print("You are going to install OSYS_VER_2.0_ALPHA_REV_2.04.\n"
                                                              "Are you sure you want to continue?")
                                                        os_install_console = input("Y/N>")
                                                        if os_install_console == "Y" or "y":
                                                            print("Dual boot or wipe drive?\n"
                                                                  "Use numbers 1 thru 2 for selection.")
                                                            is_os_inst_type_subprocess_active = True
                                                            while is_os_inst_type_subprocess_active:
                                                                os_inst_type = input("1/2>")
                                                                if os_inst_type == "1":
                                                                    clsar()
                                                                    print("Please wait while " + os_name_ver + "\n"
                                                                          "sets up your computer for dual boot config\n"
                                                                          "and dual os install...")
                                                                    time.sleep(5)
                                                                    clsar()
                                                                    print("Please wait while we grab os install iso for\n"
                                                                          "download and installation...")
                                                                    random_dl = random.uniform(0.4, 0.9)
                                                                    clsar()
                                                                    time.sleep(1)
                                                                    print("Size: 110 MB")
                                                                    print("During download and install, using your PC\n"
                                                                          "is as of yet not possible. Please be patient.")
                                                                    prog_bar(random_dl)
                                                                    time.sleep(1)
                                                                    clsar()
                                                                    print("Installing os...")
                                                                    prog_bar(0.6)
                                                                    clsar()
                                                                    print("===OOBE Setup===")
                                                                    osys_20_user = input("Please input a username: ")
                                                                    osys_20_password = input("Please input a password: ")
                                                                    osys_20_oobe_console = input("Do you want automatic\n"
                                                                                                 "updates enabled?> ")
                                                                    if osys_20_oobe_console == "y":
                                                                        print("Automatic Updates are now enabled.")
                                                                        osys_20_is_autoupdates_enabled = True
                                                                    elif osys_20_oobe_console == "n":
                                                                        osys_20_autoupdates_sure = input("Are you sure?> ")
                                                                        if osys_20_autoupdates_sure == "y":
                                                                            print("Automatic updates are now disabled.")
                                                                            osys_20_is_autoupdates_enabled = False
                                                                        elif osys_20_autoupdates_sure == "n":
                                                                            print("Automatic updates are now enabled.")
                                                                            osys_20_is_autoupdates_enabled = True
                                                                    elif osys_20_user == "def" & osys_20_password == "def":
                                                                        print("Using default...")
                                                                        osys_20_user = "user"
                                                                        osys_20_password = "password"
                                                                        osys_20_is_autoupdates_enabled = True
                                                                    print("A reboot is required. Do you want to reboot?")
                                                                    osys_20_reboot_sure = input("Y/N>")
                                                                    if osys_20_reboot_sure == "y":
                                                                        is_os_dual_booted = True
                                                                        how_much_os_installed += 1
                                                                        shutdown()
                                                                    elif osys_20_reboot_sure == "n":
                                                                        print("' null value. You must reboot.")

                                                    else:
                                                        invalid_input()
                                            else:
                                                print("Invalid operating system.")
                                else:
                                    print("ERROR: Privileges not applicable for this user.")
                            elif console == "calc":
                                is_calc_program_active = True
                                print("===CALCULATOR ANSWERER===")
                                is_operator_chosen = False
                                while is_operator_chosen is False and is_calc_program_active is True:
                                    oprtn = input("What operator would you like to choose: ")
                                    if oprtn == "multiply":
                                        is_operator_chosen = True
                                        try:
                                            print("You chose multiplication.")
                                            num1 = float(input("Pick a number:"))
                                            num2 = float(input("Pick another number:"))
                                            print(num1 * num2)
                                            is_calc_program_active = False
                                        except:
                                            print("ERROR: Not a number.")
                                    elif oprtn == "subtract":
                                        is_operator_chosen = True
                                        try:
                                            print("You chose subtraction.")
                                            num1 = float(input("Pick a number:"))
                                            num2 = float(input("Pick another number:"))
                                            print(num1 - num2)
                                            is_calc_program_active = False
                                        except:
                                            print("ERROR: Not a number.")
                                    elif oprtn == "add":
                                        try:
                                            print("You chose addition.")
                                            num1 = float(input("Pick a number:"))
                                            num2 = float(input("Pick another number:"))
                                            print(num1 + num2)
                                            is_calc_program_active = False
                                        except:
                                            print("ERROR: Not a number.")
                                    elif oprtn == "divide":
                                        try:
                                            print("You chose division.")
                                            num1 = float(input("Pick a number:"))
                                            num2 = float(input("Pick another number:"))
                                            print(num1 / num2)
                                            is_calc_program_active = False
                                        except ZeroDivisionError:
                                            print("ERROR: Division by zero is not allowed.")
                                        except:
                                            print("ERROR: Not a number.")
                                    else:
                                        print("ERROR: Invalid Input. You can only do multiply, subtract, add or divide.")
                            elif console == "logoff":
                                time.sleep(1)
                                print("Logging off...")
                                for i in range(101):
                                    time.sleep(0.03)
                                    update_progress(i / 100.0)
                                is_os_locked = True
                                is_default_logged_in = False
                                clsar()
                            elif console == "shutdown":
                                time.sleep(0.5)
                                clsar()
                                print("Shutting down services...")
                                time.sleep(0.25)
                                print("Logging off user...")
                                time.sleep(0.75)
                                print("Shutting down...")
                                time.sleep(6)
                                is_pc_on = False
                                is_default_logged_in = False
                                break
                            else:
                                print("ERROR: Invalid Input.")
                    elif name == test_user and password == test_password:
                        print("Logging in to " + os_name_ver + "...")
                        is_os_locked = False
                        time.sleep(5)
                        print("OSys Command Line")
                        print("WARNING: Experimental User for Testing!\n"
                              "First Implementation of Classes.\n")
                        import osclasses
                        console = input("~:/>")

                    elif name == rname and password == rpass:
                        if sys_privilege == 0:
                            print("NOTE: Root Access is enabled.")
                            print("Logging in to " + os_name_ver + " Debug Mode...")
                            is_os_locked = False
                            print(os_name_ver + " Internal Debug User\n" + os_name + " Debug Command Line")
                            while True:
                                console = input("1:\>")
                        elif sys_privilege > 0:
                            print("ERROR: Privileges for " + name + " are not low enough.")
                            print("ERROR: Cannot log on to " + name + " user. Privileges need to be 0.")
                            time.sleep(1)
                            print("Connecting to fallback...")
                            time.sleep(1)
                            while True:
                                console = input("???/>")
                                print(name + " is not a recognized user.")
                    elif name == "ACCcreate" and password == "DEBUG_OPTIONS_IS_ENABLED" and is_debug_options_on is True:
                        clsar()
                        print("Please wait...")
                        time.sleep(3)
                        clsar()
                        is_account_creator_active = True
                        while is_account_creator_active is True:
                            print("===" + os_name_ver + " Account Creator===")
                            print("This is only intended to appear if you have\n"
                                 "debug options enabled or during OEM Setup.\n"
                                 "If you are in neither of these situations\n"
                                 "please type cancel in the name and password\n"
                                 "dialogs.")
                            new_name = input("Please type a name: ")
                            print("Privilege types are:\n"
                                  "0: Root Access ==DENIED==\n"
                                  "1: Administrative Access\n"
                                  "2: User Access")
                            new_name_privilege = input("Privilege Type: ")
                            new_password = input("Please type a password: ")
                            print("Account Successfully Created.")
                            is_account_creator_active = False
                    elif name == "new_name" and password == "new_password":
                        if new_name_privilege == 0:
                            print("Root access enabled.\n0")
                            time.sleep(5)
                            print("Logging off...")
                            time.sleep(1)
                            break
                        elif new_name_privilege == 1:
                            print("Administrative access enabled.\n1")
                            time.sleep(5)
                            print("Logging off...")
                            time.sleep(1)
                            break
                        elif new_name_privilege == 2:
                            print("Normal access.\n" + new_name_privilege)
                            time.sleep(5)
                            print("Logging off...")
                            time.sleep(1)
                            break
                        else:
                            print("Invalid Privilege ID.")
                            time.sleep(1)
                            print("Logging off...")
                            break
                    elif name == "ACCcreate" and password == "DEBUG_OPTIONS_IS_ENABLED" and is_debug_options_on is False:
                        clsar()
                        print("Debug Options is not on.\n"
                              "Access is denied.")
                        time.sleep(1)
                        clsar()
                    elif name == "shutdown" and password == "now":
                        time.sleep(0.5)
                        clsar()
                        print("Shutting down services...")
                        time.sleep(0.25)
                        print("Logging off user...")
                        time.sleep(0.75)
                        print("Shutting down...")
                        time.sleep(6)
                        is_pc_on = False
                        break
                    elif name == "boolean" and password == "options":
                        clsar()
                        if is_debug_options_on is True:
                            print("===Boolean Options===")
                            print("Enables you to modify core boolean functions in system.")
                            print("Professional users only.")
                            is_boolean_logged_in = True
                            while is_boolean_logged_in is True:
                                boolean_console = input(">")
                                if boolean_console == "os_on_HDD":
                                    boolean_console = input("Change boolean to?>")
                                    if boolean_console == "True":
                                        os_on_HDD = True
                                    elif boolean_console == "False":
                                        os_on_HDD = False
                                    else:
                                        invalid_input()
                                elif boolean_console == "is_oobe_finished":
                                    boolean_console = input("Change boolean to?>")
                                    if boolean_console == "True":
                                        is_oobe_finished = True
                                    elif boolean_console == "False":
                                        is_oobe_finished = False
                                    else:
                                        invalid_input()
                                elif boolean_console == "is_pc_on":
                                    boolean_console = input("Change boolean to?>")
                                    if boolean_console == "True":
                                        is_pc_on = True
                                    elif boolean_console == "False":
                                        is_pc_on = False
                                    else:
                                        invalid_input()
                                elif boolean_console == "is_os_locked":
                                    boolean_console = input("Change boolean to?>")
                                    if boolean_console == "True":
                                        is_os_locked = True
                                    elif boolean_console == "False":
                                        is_os_locked = False
                                    else:
                                        invalid_input()
                                elif boolean_console == "is_debug_options_on":
                                    boolean_console = input("Change boolean to?>")
                                    if boolean_console == "True":
                                        is_debug_options_on = True
                                    elif boolean_console == "False":
                                        is_debug_options_on = False
                                    else:
                                        invalid_input()
                                elif boolean_console == "is_default_logged_in":
                                    boolean_console = input("Change boolean to?>")
                                    if boolean_console == "True":
                                        is_default_logged_in = True
                                    elif boolean_console == "False":
                                        is_default_logged_in = False
                                    else:
                                        invalid_input()
                                elif boolean_console == "is_oobe_logged_in":
                                    boolean_console = input("Change boolean to?>")
                                    if boolean_console == "True":
                                        is_oobe_logged_in = True
                                    elif boolean_console == "False":
                                        is_oobe_logged_in = False
                                    else:
                                        invalid_input()
                                elif boolean_console == "exit":
                                    break
                                elif boolean_console == "ls":
                                    print("os_on_HDD\n"
                                          "is_oobe_finished\n"
                                          "is_pc_on\n"
                                          "is_os_locked\n"
                                          "is_debug_options_on\n"
                                          "is_default_logged_in\n"
                                          "is_oobe_logged_in")
                                else:
                                    invalid_input()
                    elif name == "modify" & password == "boot":
                        if is_debug_options_on is True:
                            if is_os_dual_booted is True:
                                print("===Modify Dual Boot Start===")
                                print("Modification of dual boot configuration")
                                is_modify_boot_acc_active = True
                                while is_modify_boot_acc_active is True:
                                    modify_boot_console = input(">")
                                    if modify_boot_console == "priority":
                                        if is_os_dual_booted is True:
                                            print("There are currently " + how_much_os_installed + " os(s) installed.")
                                            is_priority_subproc_active = True
                                            while is_priority_subproc_active is True:
                                                modify_boot_console = input(">")
                                                if modify_boot_console == "ls":
                                                    print(osys_1_boot_name)
                                                    print(osys_20_boot_name)
                                                    print("Use number keys to change priority of os.")
                                                elif modify_boot_console == "1 rev 2":
                                                    time.sleep(0.5)
                                                    print("1st OS changed below 2nd.")
                                                elif modify_boot_console == "2 rev 1":
                                                    time.sleep(0.5)
                                                    print("2nd OS changed below 1st.")
                                                else:
                                                    invalid_input()
                                        else:
                                            print("No OS or unknown value.")
                                    else:
                                        invalid_input()
                        else:
                            print("Debug options is either not enabled or is replaced by an\n"
                                  "unidentifiable value."
                                  "\n"
                                  "Access is denied.")


                    else:
                        print("Invalid Username or Password. Please try again.")
                        time.sleep(1)
                        clsar()
        elif is_os_dual_booted is True and os_priority == osys_20_boot_name:
            os.system('python osys2alpha.py')
        else:
            print("ERROR: Operating System not found.")

#    else:
#        print("ERROR: Operating System not found.")

# hash_object = hashlib.sha1(b, default_name)
# hex_dig = hash_object.hexdigest()
# print(hex_dig)




