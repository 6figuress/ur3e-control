from setuptools import setup

(
    setup(
        name="urbasic",
        version="0.0.1",
        description="Python library to control an UR robot",
        author="Mandelbr0t",
        modder="Axam",
        url="https://github.com/oroulet/python-urx",
        packages=["urbasic"],
        provides=["urbasic"],
        install_requires=["opencv-python", "requests"],
        python_requires=">=3.10,<3.12",
        license="GNU Lesser General Public License v3",
        classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Operating System :: OS Independent",
            "Topic :: System :: Hardware :: Hardware Drivers",
            "Topic :: Software Development :: Libraries :: Python Modules",
        ],
        package_data={
            "urbasic": ["devices/*"],
        },
    ),
)
