from setuptools import setup

setup(
    name='excel-worksheet-maker',
    version='0.0.1',
    description='Utils for fast forming xlswriter Workbook file using strict format column list and data list',
    url='git@github.com:evgenyshipko/excel-worksheet-maker.git',
    author='Shipko Evgeny',
    author_email='evgeny-shipko@ya.ru',
    license='unlicense',
    packages=['excel_worksheet_maker'],
    zip_safe=False, install_requires=['xlsxwriter']
)