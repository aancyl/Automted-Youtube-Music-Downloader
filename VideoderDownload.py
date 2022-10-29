# This program downloads audio from youtube videos using Videoder.
# IMPORTANT : please change the values according to your screen, I would recommend using https://sourceforge.net/projects/mpos/ to do so.

import time as tm
import pyautogui as p


def goTo(name):
    p.press('win'), tm.sleep(1)
    p.click(727, 169), tm.sleep(1)
    p.write(name), tm.sleep(2),  p.press('enter')

def VideoderDownload():
    goTo('Videoder'), tm.sleep(10)
    p.hotkey('win', 'right')

    goTo('brave'), tm.sleep(3) # Change the name of your default browser
    p.hotkey('win', 'left')
    p.hotkey('ctrl', 't')
    p.write('www.youtube.com'), p.press('enter')
    tm.sleep(3)

    download_vid = ['EK Akela Is shaher main'] # enter the title of a video in ''
    count = 0
    while count != len(download_vid):
        tm.sleep(1)
        p.click(423, 163), tm.sleep(1.10)
        p.write(f'{download_vid[count]} '), p.press('enter')
        tm.sleep(1)
        p.click(130, 376), tm.sleep(4)

        # coppying the hhtp request
        p.click(294, 85), p.hotkey('ctrl', 'a')
        p.hotkey('ctrl', 'c'), tm.sleep(0.5)

        # Vidoeder stuff
        p.click(1628, 136), p.click(1628, 136)
        p.click(1168, 104), p.hotkey('ctrl', 'v'), p.press('enter')
        tm.sleep(10)
        p.click(1550, 680), tm.sleep(3)
        p.click(1488, 610), tm.sleep(3)
        tm.sleep(5)
        p.click(1628, 136), p.click(1628, 136)
        p.click(372, 162)
        p.hotkey('ctrl', 'a'), p.press('delete')
        count += 1
    p.hotkey('win', 'd')

VideoderDownload()


