from setuptools import setup


if __name__ == "__main__":

    setup(
        name="anonomatic_client",
        version="0.0.1",
        description="anonomatic_client",
        long_description=local_file("README.md"),
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
