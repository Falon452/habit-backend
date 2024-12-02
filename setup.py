from setuptools import setup, find_packages

setup(
    name="habit_backend",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
    ],
    entry_points={
        "console_scripts": [
            "habit_backend=habit_backend.main:app",
        ],
    },
)
