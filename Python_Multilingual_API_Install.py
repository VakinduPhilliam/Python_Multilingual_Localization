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
#
# install(names=None). 
# This method installs gettext() into the built-in namespace, binding it to _.
# 
# If the names parameter is given, it must be a sequence containing the names of functions you want to install in the builtins namespace in addition to _().
# Supported names are 'gettext', 'ngettext', 'lgettext' and 'lngettext'.
# 
# Note that this is only one way, albeit the most convenient way, to make the _() function available to your application.
# Because it affects the entire application globally, and specifically the built-in namespace, localized modules should never install _().
# Instead, they should use this code to make _() available to their module:
# 

import gettext

t = gettext.translation('mymodule', ...)

_ = t.gettext
 
#
# This puts _() only in the module’s global namespace and so only affects calls within this module.
#