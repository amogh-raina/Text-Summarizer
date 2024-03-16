import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR = "amogh-raina"
SRC_REPO = "TextSummarizer"
AUTHOR_EMAIL = "amoghraina391@gmail.com"


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A package to summarize text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)