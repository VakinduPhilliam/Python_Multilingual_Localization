# Python Multilingual API
# gettext — Multilingual internationalization services.
# The gettext module provides internationalization (I18N) and localization (L10N) services for your Python modules and applications.
# It supports both the GNU gettext message catalog API and a higher level, class-based API that may be more appropriate for Python files.
# The interface described below allows you to write your module and application messages in one natural language, and provide a catalog of translated
# messages for running under different natural languages.
#
# GNU gettext API:
#
# The gettext module defines the following API, which is very similar to the GNU gettext API.
# If you use this API you will affect the translation of your entire application globally.
# Often this is what you want if your application is monolingual, with the choice of language dependent on the locale of your user.
# If you are localizing a Python module, or if your application needs to switch languages on the fly, you probably want to use the class-based API instead.
#
# Changing languages on the fly.
# If your program needs to support many languages at the same time, you may want to create multiple translation instances and then switch between them
# explicitly, like so:
# 

import gettext

lang1 = gettext.translation('myapplication', languages=['en'])
lang2 = gettext.translation('myapplication', languages=['fr'])

lang3 = gettext.translation('myapplication', languages=['de'])

# start by using language1

lang1.install()

# ... time goes by, user selects language 2

lang2.install()

# ... more time goes by, user selects language 3

lang3.install()
