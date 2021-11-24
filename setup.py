import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-rabbitmq",
    version="0.1.2",
    author="Yuhui Wang, Ibere Di Tizio Jr",
    author_email="ibere.tizio@gmail.com",
    description="Start a RabbitMQ consumer after django server start.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/IbereJr/django-rabbitmq",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
