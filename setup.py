try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Контроль и управление инвентарём',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': ''
               '0.1',
    'install_requires': ['nose'],
    'packages': ['Inventory'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)