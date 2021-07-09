from setuptools import setup, find_packages

__version__ = "0.3.2"

with open("readme.md", "r") as f:
    readme = f.read()

requirements = ["requests-HTML>=0.10.0", "MangaDex.py>=2.0.6", "pillow>=8.0.1"]

setup(
    name = "mangas-dl",
    version = __version__,
    author = "Boubou0909",
    author_email = "balthazar0909@gmail.com",
    description = "Mangas' scans downloader app",
    long_description = readme,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Boubou0909/Mangas-dl",
    packages = find_packages(),
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