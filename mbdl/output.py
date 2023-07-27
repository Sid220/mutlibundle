class Colours:
    CEND = '\33[0m'
    CBOLD = '\33[1m'
    CITALIC = '\33[3m'
    CURL = '\33[4m'
    CBLINK = '\33[5m'
    CBLINK2 = '\33[6m'
    CSELECTED = '\33[7m'

    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'

    CBLACKBG = '\33[40m'
    CREDBG = '\33[41m'
    CGREENBG = '\33[42m'
    CYELLOWBG = '\33[43m'
    CBLUEBG = '\33[44m'
    CVIOLETBG = '\33[45m'
    CBEIGEBG = '\33[46m'
    CWHITEBG = '\33[47m'

    CGREY = '\33[90m'
    CRED2 = '\33[91m'
    CGREEN2 = '\33[92m'
    CYELLOW2 = '\33[93m'
    CBLUE2 = '\33[94m'
    CVIOLET2 = '\33[95m'
    CBEIGE2 = '\33[96m'
    CWHITE2 = '\33[97m'

    CGREYBG = '\33[100m'
    CREDBG2 = '\33[101m'
    CGREENBG2 = '\33[102m'
    CYELLOWBG2 = '\33[103m'
    CBLUEBG2 = '\33[104m'
    CVIOLETBG2 = '\33[105m'
    CBEIGEBG2 = '\33[106m'
    CWHITEBG2 = '\33[107m'


def print_error(msg):
    print(Colours.CRED + Colours.CBOLD + "[-] " + Colours.CEND + Colours.CRED + msg + Colours.CEND)


def print_succ(msg):
    print(Colours.CGREEN + Colours.CBOLD + "[+] " + Colours.CEND + Colours.CGREEN + msg + Colours.CEND)


def print_warn(msg):
    print(Colours.CYELLOW + Colours.CBOLD + "[!] " + Colours.CEND + Colours.CYELLOW + msg + Colours.CEND)


def print_info(msg):
    print(Colours.CBLUE + Colours.CBOLD + "[i] " + Colours.CEND + Colours.CBLUE + msg + Colours.CEND)


def print_fatal(msg):
    print(Colours.CRED + Colours.CBOLD + "[!] " + Colours.CEND + Colours.CRED + msg + Colours.CEND)


def print_question(msg):
    print(Colours.CVIOLET + Colours.CBOLD + "[?] " + Colours.CEND + Colours.CVIOLET + msg + Colours.CEND, end="")


def yes_no(question, callback_y, callback_n):
    print_question(question)
    if input(" (y/n): ").lower() == "y":
        callback_y()
    else:
        callback_n()


def corrupt():
    print_fatal("Corrupt file")
    exit(1)
