from setuptools import setup

setup(name='pyproject',
      version='0.1',
      description='IDK',
      long_description="""
# pyproject
## Informació
- Per executar el programa s'ha de tenir instalat el python versio 3 o mes.
- Requeriments a requirements.txt.
- El fitxer compilar.bat transforma el .py en .pyc que es mes eficient i rapid.
- Executar amb opcio -h per veure mes opcions i funcionalitats.
## Instal·lació
- Utilitzant `pip`
```
pip install pyproject
```
## Ús
- Executar el fitxer `pyproject.py` o `pyproject.cpython-39.pyc` amb les opcions adients

- Opcions
```

```
""",
      long_description_content_type='text/markdown',
      url='https://github.com/NilPujolPorta/pyproject',
      author='Nil Pujol Porta',
      author_email='nilpujolporta@gmail.com',
      license='GNU',
      packages=['pyproject'],
      install_requires=[
          'argparse',
          "setuptools>=42",
          "wheel"
      ],
	  entry_points = {
        "console_scripts": ['pyproject = pyproject.pyproject:main']
        },
      zip_safe=False)