from setuptools import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.rst') as changelog_file:
    changelog = changelog_file.read()

if __name__ == "__main__":

    setup(
        name="anonomatic_client",
        version="0.0.1",
        description="Simple Anonomatic Client",
        long_description=readme + '\n\n' + changelog,
        author="Andrew Gross",
        author_email="andrew.w.gross@gmail.com",
        url="https://github.com/andrewgross",
        packages=find_packages(exclude=["*tests*"]),
        install_requires=[
            "requests>=2.0.0"
        ],
        include_package_data=True,
        classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3 :: Only",
        ],
        zip_safe=False,
    )
