from downtool import down
from api import DtServerApi
import datetime
import time
import requests

a = DtServerApi()
a.start()
a.getHistory()
a.startByWebServer()

 