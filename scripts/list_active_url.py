#!/usr/bin/env python.exe
import win32gui
from selenium import webdriver
import re

def init_webdriver():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    return driver

driver = init_webdriver()

def list_title_url_handle():
    global driver
    ret = list()
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        url = driver.current_url
        title = driver.title
        ret.append( (title, url, handle) )
    return ret

def list_active_title():
    ret = list()
    def winEnumHandler(hwnd, ctx):
        if not win32gui.IsWindowVisible(hwnd): return
        title = win32gui.GetWindowText(hwnd)
        pattern = " - Google Chrome"
        if not title.endswith(pattern): return
        title = title.removesuffix(pattern)
        ret.append( title )
    win32gui.EnumWindows(winEnumHandler, None)
    return ret

def main():
    global driver
    ret = list()
    active_title = list_active_title()
    title_url_handle = list_title_url_handle()
    for atitle in active_title:
        for title, url, handle in title_url_handle:
            if atitle == title:
                driver.switch_to.window(handle)
                ret.append(url)
    return ret

def atcoder():
    pattern = r"https://atcoder.jp/contests/(.*)/tasks/\1_(.*)"
    urls = main()
    for url in urls:
        m = re.match(pattern, url)
        if m is not None:
            return url

if __name__ == '__main__':
    url = atcoder()
    print(url, end='\n')