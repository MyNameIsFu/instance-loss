import os
import setuptools

setuptools.setup(
    name="Instance Loss",
    version=os.environ.get("CI_COMMIT_TAG"),
    author="Muhammad Febrian Rachmadi, Michal Byra, Henrik Skibbe, Michael Fujarski",
    author_email="michael.fujarski@uni-muenster.de",
    description="Wrapper, Trainer, and Artist for MetaAI's SAM.",
    long_description_content_type="text/markdown",
    url="https://github.com/MyNameIsFu/instance-loss",
    packages=["instance_loss"],
    package_dir={"instance_loss": "./instance_loss"},
    install_requires=["monai"],
    classifiers=[
        "Programming Language :: Python :: 3.11"
    ],
)