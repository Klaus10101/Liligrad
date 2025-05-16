import setuptools

with open("README.md", "r") as f:
    DESC = f.read()

setuptools.setup(

    name= "Liligrad",
    version= "0.0.1",
    author= "Klaus10101",
    author_email= "Klaus10101code@gmail.com",
    description= "a mini scalar valued autograd engine",
    long_description= DESC,
    long_description_content_type= "text/mardown",
    url= "jttps://github.com/Klaus10101/Liligrad.git",
    packages=setuptools.find_packages(),
    classifiers=[
    "Programing Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
        
    ],
    python_requires= '>=3.8',

)
