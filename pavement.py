import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
from socket import gethostname
import os, sys
from os import environ

from sphinxcontrib import paverutils

sys.path.append(os.getcwd())

home_dir = os.getcwd()


master_url = None
if master_url is None:
    if 'RSHOST' in os.environ:
        master_url = environ['RSHOST']
    elif gethostname() in  ['web608.webfaction.com', 'rsbuilder']:
        master_url = 'http://interactivepython.org'
    elif gethostname() == 'runestone-deploy':
        master_url = 'https://runestone.academy'
    else:
        master_url = 'http://127.0.0.1:8000'
        
master_app = 'runestone'
serving_dir = "./build/Ex3Parsons"
dest = '../../static'
project_name = "Ex3Parsons"

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/Ex3Parsons",
        sourcedir="_sources",
        outdir="./build/Ex3Parsons",
        confdir=".",
        project_name = "Ex3",
        template_args={'course_id': 'Ex3Parsons',
                       'login_required':'true',
                       'appname':master_app,
                       'loglevel': 10,
                       'course_url':master_url,
                       'use_services': 'true',
                       'python3': 'true',
                       'dburl': 'postgresql://runestone@localhost/runestone',
                       'basecourse': 'Ex3Parsons'
                        }
    )
)

# Check to see if we are building on our Jenkins build server, if so use the environment variables
# to update the DB information for this build
if 'DBHOST' in environ and  'DBPASS' in environ and 'DBUSER' in environ and 'DBNAME' in environ:
    options.build.template_args['dburl'] = 'postgresql://{DBUSER}:{DBPASS}@{DBHOST}/{DBNAME}'.format(**environ)

from runestone import build  # build is called implicitly by the paver driver.