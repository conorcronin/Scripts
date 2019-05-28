# This is a script that can be run on startup
# It will start a browser with tabs and open URLs from a txt file
# aswell as opening other programs I use daily
# Author: Conor Cronin
import webbrowser, time, os

def questionOne():
    answer = raw_input("Browser Tabs? y/n")
    if answer == "y":
        f = "Path\To\List\Of\URLS.txt"

        f = open(f)
        urlfile = f.read().splitlines()

        for url in urlfile:
            webbrowser.open_new_tab(url)

        print("Tabs: loading")
    else:
        return

def questionTwo():
    answerTwo = raw_input("Programs? y/n")
    if answerTwo == "y":
        time.sleep(5)
        g = "Path\To\List\Of\Programs.txt"

        g = open(g)
        programFile = g.read().splitlines()

        for program in programFile:
            os.startfile(program)

        print("Programs: loading")
    else:
        return

questionOne()
questionTwo()

print("Closing...")
time.sleep(10)
exit()
