import sys

project_home = u"/home/gmontano/pythonDashQuandl"

if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from dashapp import app
server = app.server