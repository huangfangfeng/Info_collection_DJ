# -*- coding: utf-8 -* 
"""
WSGI config for infocollection project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'infocollection.settings')

application = get_wsgi_application()
'''
#添加如下，设定项目路径，使settings模块位于系统路径import os
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_DIR)

sys.path.append('/var/www/html/mydjango/infocollection/')
sys.path.append('/root/.pyenv/version/3.7.2/lib/python3.7')
'''
