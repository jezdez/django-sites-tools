from distutils.core import setup

setup(
    name='django-sites-tools',
    version='0.2.0',
    description="A Django app that provides tools for the contrib sites app.",
    author='Jannis Leidel',
    author_email='jannis@leidel.info',
    license='BSD',
    url='http://github.com/jezdez/django-sites-tools/',
    packages=['sites_tools'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
)
