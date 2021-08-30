from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Python package to interact with whatsapp'
LONG_DESCRIPTION = 'Python package to interact with whatsapp using different methods'

setup(
        name="wpkit", 
        version=VERSION,
        author="rootkral4",
        author_email="rootkral4@hotmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=["keyboard"],
        keywords=['whatsapp', 'web whatsapp'],

)