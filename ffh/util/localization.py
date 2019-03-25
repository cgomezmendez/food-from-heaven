import gettext
import os
import ffh

locale_dir = os.path.join(os.path.abspath(os.path.dirname(ffh.__file__)), 'locale')
print(locale_dir)
translate = gettext.translation('ffh', locale_dir, fallback=False)

_ = translate.gettext
