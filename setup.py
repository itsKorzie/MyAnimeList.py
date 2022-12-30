import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name= 'MyAnimeList.py',
    version='1.0.0',
    author='Romain Croughs',
    author_email='romain.croughs@gmail.com',
    description='Easy-to-use MyAnimeList API wrapper library for Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/itsKorzie/MyAnimeList.py',
    project_urls = {
        "Report an issue": "https://github.com/itsKorzie/MyAnimeList.py/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)