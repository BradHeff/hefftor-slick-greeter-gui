# ============================================
#           Author Brad Heffernan
# ============================================
import os


def pop_themes(self):
    themes = os.listdir("/usr/share/themes")
    for x in themes:
        self.theme_combo.append_text(x)
    self.theme_combo.set_active(0)