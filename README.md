<img src="./assets/nusmodsbot.png" width="300px">

## About

Are you tired of opening the [NUSMods website](http://nusmods.com/) to check for module information? Well then, this bot is for you!

This bot helps you easily access module information like module code, module description, pre-requisites, etc. from your favorite app - telegram!

## Debugging

1. When running any of the .py files, if `os.getenv` doesn't seem to work, just copy the variables from your .env file to the program file itself.
2. Make sure you're using python3 (preferably python 3.10.5)
3. While installing `python-telegram-bot`, use `pip install python-telegram-bot -U --pre` since we are using version 20.x which is still in pre-release mode. Some of the features won't be available in the 13.x version.
4. Make sure you have installed `requests` as well
5. If `pip` does not work (i.e., you get an error `pip command not found`), try running `pip3 install ...` instead.
6. Read more [here](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions-%E2%80%93-Your-first-Bot)
