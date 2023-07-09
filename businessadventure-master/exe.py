import cx_Freeze

from cx_Freeze import setup, Executable

base = None

executables = [Executable("main2.py")]


setup(
    name = "Mon Programme",
    version = "1.0",
    description = 'Voici mon programme',
    executables = executables
)

