from setuptools import setup, find_packages

setup(
    name="map_analysis_project",
    version="0.1",
    description="A project for geographical analysis with OSMnx, NetworkX, and Folium.",
    packages=find_packages(),
    install_requires=[
        "osmnx",
        "pandas",
        "networkx",
        "matplotlib",
        "folium",
        "geopandas",
        "shapely"
    ],
    python_requires='>=3.6',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
