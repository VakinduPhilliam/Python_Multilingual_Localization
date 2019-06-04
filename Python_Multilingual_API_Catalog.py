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
# Solaris message catalog support.
# The Solaris operating system defines its own binary .mo file format, but since no documentation can be found on this format, it is not supported at this
# time.
# 
# The Catalog constructor
# GNOME uses a version of the gettext module by James Henstridge, but this version has a slightly different API. Its documented usage was:
# 

import gettext

cat = gettext.Catalog(domain, localedir)

_ = cat.gettext

print(_('hello world'))
