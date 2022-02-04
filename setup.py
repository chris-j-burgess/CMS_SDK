import setuptools

setuptools.setup(
    name="CMS_SDK",
    version="1.0.0"
    description="Software Development kit for CMS"
    packages=setuptools.find_packages('src')
    package_dir={'':'src'}
)