
import logging

import os

import yaml     

import pathlib

from database.localdb import check_lang

from main_startup.config_var import Config

from main_startup import (

    CMD_LIST,

    XTRA_CMD_LIST,

    Config,

    Stylish,

    Stylish2,

    Stylish3,

    Stylish4,

    bot

)

language_string = {}

class Engine:

    def __init__(self):

        self.path = "./bot_utils_files/Fonts/strings/"

        

    def get_all_files_in_path(self, path):

        path = pathlib.Path(path)

        return [i.absolute() for i in path.glob("**/*")]

    def load_language(self):

        all_files = self.get_all_files_in_path(self.path)

        for filepath in all_files:

            with open(filepath) as f:

                data = yaml.safe_load(f)

                language_to_load = data.get("language")

                logging.debug(f"Loading : {language_to_load}")

                language_string[language_to_load] = data

        logging.debug("All language Loaded.")

        

    def get_string(self, string):

        lang_ = Stylish.selected_lang

        return (

            language_string.get(lang_).get(string)

            or f"**404_STRING_NOT_FOUND :** `String {string} Not Found in {lang} String 	File. - Please Report It To @FridayChat`"        )
