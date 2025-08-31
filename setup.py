# This is the setup script for the E2E Chicken Disease Classification, Computer Vision project.
# It uses setuptools library to package the project and make it installable.
# The project is structured to include a README file for long description,
# and it specifies metadata such as version, author, and project URLs.
# The source code is located in the 'src' directory, and the package is named 'ChickenDisease'.

import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "1.0"
REPO_NAME = "E2E_CV_Class_ChickenDisease"
AUTHOR_USER_NAME = "MohamedEmam82"
SRC_REPO = "ChickenDisease"
AUTHOR_EMAIL = "mohamed.salaheldin.emam@gmail.com"

setuptools.setup(
    name=SRC_REPO, # This is the name of the package that will be installed
    version=__version__,
    author=AUTHOR_USER_NAME, # This is the author's username, typically on GitHub
                             # The author's email is used for contact purposes, such as issues or contributions
                             # It is a good practice to provide a valid email address for maintainers.
    author_email=AUTHOR_EMAIL,
    description="End to end Chicken Disease Classification, Computer Vision project using CNNs, TensorFlow.",
    long_description=long_description,
    long_description_content="text/markdown", # Specifies that the long description is in Markdown format
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}", 
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues", 
    },
    package_dir={"": "src"}, # Specify that the source code is in the 'src' directory
    packages=setuptools.find_packages(where="src") # Automatically find packages in the src directory
)