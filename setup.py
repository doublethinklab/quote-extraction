import setuptools


with open('version') as f:
    version = f.read().strip()


# if adding other requirements in future...
# with open('requirements.txt') as f:
#     required = f.read().splitlines()


setuptools.setup(
    name='quote_extraction',
    version=version,
    author='Cecile Liu',
    author_email='svetlana@doublethinklab.org',
    description='Reusable module for quote extraction.',
    url=f'https://github.com/doublethinklab/quote-extraction.git#{version}',
    packages=setuptools.find_packages(),
    python_requires='>=3.9.5',
    # install_requires=required
)
