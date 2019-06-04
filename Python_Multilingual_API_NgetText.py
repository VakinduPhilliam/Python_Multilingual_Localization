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
# ngettext(singular, plural, n). 
# Do a plural-forms lookup of a message id. singular is used as the message id for purposes of lookup in the catalog, while n is used to determine which
# plural form to use. The returned message string is a Unicode string.
# 
# If the message id is not found in the catalog, and a fallback is specified, the request is forwarded to the fallback’s ngettext() method. Otherwise, when
# n is 1 singular is returned, and plural is returned in all other cases.
# 
# Here is an example:
# 

n = len(os.listdir('.'))

cat = GNUTranslations(somefile)

message = cat.ngettext(
    'There is %(num)d file in this directory',
    'There are %(num)d files in this directory',
    n) % {'num': n}
