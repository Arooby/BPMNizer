import re
import os
import xml.etree.ElementTree as ET


class MyDrawEPC:
    def __init__(self, file):
        self.file = file

    def input_file(self):
        with open(self.file, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)

            if content:
                return True  # content read
            else:
                return False

