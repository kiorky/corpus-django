# -*- coding: utf-8 -*-
from .base import *

try:
    from .local.base_pre import *
except ImportError:
    pass

try:
    from .local.prod_pre import *
except ImportError:
    pass


##### SECURITY #####

SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_HTTPONLY = True

# Suppose we are using HTTPS
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True # Just in case, should be done by webserver instead


try:
    from .local.base_post import *
except ImportError:
    pass

try:
    from .local.prod_post import *
except ImportError:
    pass
