try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Усадьба dymki.by',
    'author': 'Dmitry Vl.Rendov',
    'url': 'http://dymki.by',
    'author_email': 'drendov@gmail.com',
    'version': ''
               '0.1',
    'install_requires': ['nose'],
    'packages': ['balu'],
    'scripts': [],
    'name': 'balu'
}

setup(**config)
