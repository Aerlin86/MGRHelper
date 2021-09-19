import os, shutil, datetime, tkinter, tkinter.filedialog, re, win10toast
from pathlib import Path


mgrdirectory = 0
mgrfile = 0


def cleaning() -> None:
    """Moves different types of files into separate folders."""
    files = os.listdir(mgrdirectory)  # list of files in directory for definitions
    files.remove(mgrfile)  # putting Praca Magisterska out of list above not to be included in definitions

    g = (".gif", ".jpg", ".JPG", ".jpeg", ".png", ".bmp")  # graphics files extensions
    t = (".doc", ".docx", ".txt", ".pdf")  # text files extensions
    x = (".xls", ".xlsx")  # table files extensions

    for file in files:
        if file.endswith(g):
            try:
                shutil.move(mgrdirectory + "\\" + file, mgrdirectory + "\\Grafika")
            except:
                same_name(file)

    for file in files:
        if file.endswith(t):
            try:
                shutil.move(mgrdirectory + "\\" + file, mgrdirectory + "\\Teksty")
            except:
                same_name(file)

    for file in files:
        if file.endswith(x):
            try:
                shutil.move(mgrdirectory + "\\" + file, mgrdirectory + "\\Tabele")
            except:
                same_name(file)

    try:
        path, dirs, files = next(os.walk("D:\Praca magisterska\Check"))
        file_count = len(files)
    except:
        pass

    if file_count > 0:
        same_name_notification()

# DATACOPY


now = str(datetime.datetime.now())[:19] # getting date and time to include in file name
now = now.replace(":","_") # changing : to _ so it can be saved as a file name


def makecopy() -> None:
    """Makes copy of the main thesis file."""
    src_dir=mgrdirectory + "\\" + mgrfile
    dst_dir=mgrdirectory + "\\Kopie zapasowe\\" + mgrfile +str(now)+".docx"
    shutil.copy(src_dir,dst_dir)

# DIRMAKER


def makedir() -> None:
    """Makes unexisting DIRs for cleaning def."""
    dir = os.path.join(mgrdirectory, "Grafika")
    if not os.path.exists(dir):
        os.mkdir(dir)

    dir = os.path.join(mgrdirectory, "Teksty")
    if not os.path.exists(dir):
        os.mkdir(dir)

    dir = os.path.join(mgrdirectory, "Kopie zapasowe")
    if not os.path.exists(dir):
        os.mkdir(dir)

    dir = os.path.join(mgrdirectory, "Tabele")
    if not os.path.exists(dir):
        os.mkdir(dir)

# CHOOSEDIR


def loaddir() -> dir:
    """Load thesis folder directory."""
    global mgrdirectory
    mgrdirectory = tkinter.filedialog.askdirectory(initialdir="/",  title='Proszę wybierz folder z pracą magisterską')
    mgrdirectory = mgrdirectory.replace('/', '\\')
    return mgrdirectory


def loadfile() -> dir:
    "Load main thesis file directory."
    global mgrfile
    mgrfile = tkinter.filedialog.askopenfilename(initialdir="/",  title='Proszę wybierz folder z pracą magisterską')
    mgrfile = mgrfile.replace('/', '\\')
    mgrfile = mgrfile.removeprefix(mgrdirectory + "\\")
    return mgrfile

# SAME NAME ERROR HANDLING DEFINITION


def same_name(file) -> None:
    """Same name error handling."""
    check_path_creation = (mgrdirectory + "\\Check")
    check_path = Path(check_path_creation)
    if not os.path.exists(check_path):
        os.mkdir(check_path)

    add = '(spr)'
    old_file_name = file
    path = mgrdirectory
    new_file_name = re.search("(.*)(\..*)", old_file_name)
    new_file = new_file_name.group(1)
    p = new_file_name.group(2)
    new_file_name = new_file + add + p
    os.rename(os.path.join(path, old_file_name), os.path.join(path, new_file_name))
    shutil.move(mgrdirectory + "\\" + new_file_name, check_path)


def same_name_notification() -> None:
    """Windows 10 pop up windows with information about same name error."""
    pop = win10toast.ToastNotifier()
    pop.show_toast("UWAGA", "Część plików miała takie same nazwy!", threaded=True)