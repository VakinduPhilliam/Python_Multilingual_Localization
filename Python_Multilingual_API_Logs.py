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
# Internationalizing your programs and modules
# Internationalization (I18N) refers to the operation by which a program is made aware of multiple languages.
# Localization (L10N) refers to the adaptation of your program, once internationalized, to the local language and cultural habits.
# In order to provide multilingual messages for your Python programs, you need to take the following steps:
#
# 1.prepare your program or module by specially marking translatable strings
# 2.run a suite of tools over your marked files to generate raw messages catalogs
# 3.create language specific translations of the message catalogs
# 4.use the gettext module so that message strings are properly translated
# 
# In order to prepare your code for I18N, you need to look at all the strings in your files. Any string that needs to be translated should be marked by
# wrapping it in _('...') — that is, a call to the function _().
#
# For example:
# 

filename = 'mylog.txt'

message = _('writing a log message')

fp = open(filename, 'w')
fp.write(message)

fp.close()
