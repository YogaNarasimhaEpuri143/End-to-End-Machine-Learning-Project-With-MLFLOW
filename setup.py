# Res
import setuptools  # In built, Making package.


HYPEN_E_DOT = "-e ."
def get_requirements(filePath):
    """
        This Function returns the all the required packages to install
    """
    requirements = []
    with open(filePath, "r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "YogaNarasimhaEpuri143"
SRC_REPO = "mlproject"
AUTHOR_EMAIL = "yoganarasimhaepuri143@gmail.com"

setuptools.setup(
    # include_package_data = True
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"htpps://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"htpps://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},  # instructing "setuptools" to treat the "src" directory as the location of project's top-level package (or) root namespace.
    packages=setuptools.find_packages(where="src"), # find the packages inside the given folder.

    install_requires=get_requirements("requirements.txt")
)