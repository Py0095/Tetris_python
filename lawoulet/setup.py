from cx_Freeze import setup, Executable

setup(
    name="Lawoule",
    version="1.0",
    description="Devine le nombre mystère",
    executables=[Executable("main.py")]
)
