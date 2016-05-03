import sys
from pprint import pprint

pprint(sys.path)

from .algo import lalgo


lalgo()

from .lloo import  gola

from . import lloo

from .chardet import detect

from . import chardet
from . import pysrt



def load_srt(path):
    print('some loader loading', path, pysrt)
