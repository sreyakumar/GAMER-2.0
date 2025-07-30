from setuptools import setup, find_packages

setup(
    name="gamer",
    version="0.1.0",
    description="GAMER - Graph-based Agent for MongoDB Entity Retrieval",
    packages=find_packages(),
    install_requires=[
        "langchain_core",
        "langgraph",
        "langsmith",
        "aind_data_access_api",
        "sentence_transformers",
        "pydantic",
        "langchain_aws",
        "langchain_experimental"
    ],
    python_requires=">=3.11",
    author="Your Name",
    author_email="your.email@example.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.11",
    ],
)
