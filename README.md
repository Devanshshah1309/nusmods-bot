# About

I just made this to learn how to create telegram bots because they seemed cool!

The only relevant bot is the `officialNUSmodsBot` - everything else was just built in the process of trying to learn :)

# What does this bot do?

Help NUS students easily access module information like module code, module description, pre-requisites, etc. without having to open the website :)

# Debugging

1. When running any of the .py files, if `os.getenv` doesn't seem to work, just copy the variables from your .env file to the program file itself.
2. Make sure you're using python3 (preferably python 3.10.5)
3. While installing `python-telegram-bot`, use `pip install python-telegram-bot -U --pre` since we are using version 20.x which is still in pre-release mode. Some of the features won't be available in the 13.x version.
4. Make sure you have installed `requests` as well
5. If `pip` does not work (i.e., you get an error `pip command not found`), try running `pip3 install ...` instead.
6. Read more [here](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot)
