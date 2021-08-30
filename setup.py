from setuptools import setup, find_packages
from pathlib import Path

setup(
        name="wpkit", 
        version='0.0.1',
        author="rootkral4",
        author_email="rootkral4@hotmail.com",
        description='Python package to interact with whatsapp',
        long_description=(Path(__file__).parent / "README.md").read_text(),
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=["keyboard"],
        url='https://github.com/rootkral4/wpkit',
        keywords=['whatsapp', 'web whatsapp'],

)