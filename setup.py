from glob import glob
from setuptools import setup, find_packages, Extension
try:
    from Cython.Build import cythonize
    EXTENSIONS = cythonize(
        Extension(
            'test_project.test',
            sources=glob('./test_project/*.pyx'),
        ),
    )
except ImportError:
    EXTENSIONS = [
        Extension(
            'test_project.test',
            sources=glob('./test_project/*.c'),
        ),
    ]


VERSION = '0.1.2'


setup(
    name='python-test-project',
    version=VERSION,
    license='MIT',
    url='https://github.com/Chiorufarewerin/python-test-project',
    author='Artur Beltsov',
    author_email='artur1998g@gmail.com',
    description='TEST',
    long_description='TEST',
    long_description_content_type='text/x-rst',
    packages=find_packages(exclude=['tests', 'benchmark']),
    python_requires='>=3.6',
    zip_safe=False,
    ext_modules=EXTENSIONS,
)
