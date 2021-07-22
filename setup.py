from setuptools import setup, find_packages

__version__ = "1.0.2"

with open("readme.md", "r") as f:
    readme = f.read()

requirements = ["requests-HTML>=0.10.0", "MangaDex.py>=2.0.6", "pillow>=8.0.1", "imgurpython>=1.1.7"]

setup(
    name = "mangas-dl",
    version = __version__,
    author = "Boubou0909",
    author_email = "balthazar0909@gmail.com",
    description = "Mangas' scans downloader app",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Boubou0909/Mangas-dl",
    packages = find_packages(include=["mangas_dl.*"]),
    data_files = [("mangas_dl", ["mangas_dl/HELP.md", "mangas_dl/conf.ini", "mangas_dl/language_codes.json", "mangas_dl/settings.json", "mangas_dl/websites_used.json"])],
    install_requires = requirements,
    entry_points = '''
        [console_scripts]
        mangas-dl=mangas_dl.__main__:main
    ''',
    classifiers = 
    [
        "Programming Language :: Python :: 3.9"
    ]
)