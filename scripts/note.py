#!/usr/bin/env python.exe
# %%
from selenium import webdriver
import re
from pathlib import Path
# %%
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=options)
# %%
for h in driver.window_handles:
    driver.switch_to.window(h)
    print(driver.current_url)
    m = re.match(r"https://atcoder.jp/contests/(.*)/tasks/\1_(.*)", driver.current_url)
    if m is not None:
        break
else:
    exit(1)
# %%
driver.execute_script(
(Path(__file__).parent/"AtCoder_Note.js").read_text()
)
driver.refresh()