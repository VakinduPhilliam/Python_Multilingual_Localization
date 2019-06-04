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
# Localizing your application.
# If you are localizing your application, you can install the _() function globally into the built-in namespace, usually in the main driver file of your
# application. This will let all your application-specific files just use _('...') without having to explicitly install it in each file.
# 
# In the simple case then, you need only add the following bit of code to the main driver file of your application:
# 

import gettext

gettext.install('myapplication')
