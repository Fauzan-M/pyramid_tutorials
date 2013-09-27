from setuptools import setup

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'ZODB3',
    'pyramid_zodbconn',
    'pyramid_tm',
]

setup(name='tutorial',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = tutorial:main
      """,
)