import win32api, win32gui, win32con, win32process, time, subprocess

w = win32api.GetSystemMetrics(0)
h = win32api.GetSystemMetrics(1)

def main():
    time.sleep(3)
    ffplay = win32gui.FindWindow(None, "pynamic_player")
    progman = win32gui.FindWindow("Progman", "Program Manager")
    win32gui.SendMessageTimeout(progman, 0x052C, 0, 0, win32con.SMTO_NORMAL, 1000)
    time.sleep(0.1)
    hwnd = win32gui.GetWindow(progman, win32con.GW_HWNDPREV)
    wkwname = win32gui.GetClassName(hwnd)
    print(wkwname)
    if wkwname == "WorkerW" :
        win32gui.SetParent(ffplay, hwnd)
        win32gui.SetWindowPos(ffplay, win32con.HWND_BOTTOM, 0, 0, w, h, 0 | win32con.SWP_NOZORDER)

subprocess.Popen(['player.bat', str(w), str(h)])
main()
