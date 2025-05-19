from setuptools import setup, find_packages

setup(
    name="asteroids",  # The name of your package
    version="0.1.0",    # Version number
    packages=find_packages(where="src"),  # Tells setuptools to look in 'src'
    package_dir={"": "src"},              # Maps packages to 'src/' folder
    install_requires=[
        "requests",      # Required library for API requests
        "pandas"         # Required library for data handling
    ],
    entry_points={                       # Defines terminal command
        "console_scripts": [
            "asteroids=asteroids.cli:main",  
            # This means: when user runs 'asteroids', run asteroids/cli.py > main()
        ],
    },
)
