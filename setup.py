from setuptools import setup, find_packages

setup(
    name='django-app-plugins',
    version=__import__('app_plugins').__version__,
    description='Reusable django application for writting pluggable reusable '
                'django applications.',
    long_description=open('docs/overview.txt').read(),
    author='Doug Napoleone',
    author_email='doug.napoleone@gmail.com',
    url='http://code.google.com/p/django-app-plugins/',
    license = 'MIT License',
    platforms = ['any'],
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
