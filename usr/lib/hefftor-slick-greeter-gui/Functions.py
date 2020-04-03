# ============================================
#           Author Brad Heffernan
# ============================================
import os
# import subprocess
from pathlib import Path
# from time import sleep
# import threading

home = os.path.expanduser("~")
base_dir = os.path.dirname(os.path.realpath(__file__))
# here = Path(__file__).resolve()
working_dir = ''.join([str(Path(__file__).parents[2]),
                       "/share/hefftor-slick-greeter-gui/"])


def pop_themes(self):
    themes = os.listdir("/usr/share/themes")
    for x in themes:
        self.theme_combo.append_text(x)
    self.theme_combo.set_active(0)
