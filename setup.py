#!/usr/bin/env python
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()
    requirements = [req.replace('==', '>=') for req in requirements]


def _clean_version():
    """
    This function was required because scm was generating developer versions on
    GitHub Action.
    """
    def get_version(version):
        return str(version.tag)
    def empty(version):
        return ''

    return {'local_scheme': get_version, 'version_scheme': empty}


# normal setuptool inputs
setuptools.setup(
    name='pollination-honeybee-radiance',                                   # will be used for package name unless it is overwritten using __queenbee__ info.
    author='ladybug-tools',                                                 # the owner account for this package - required if pushed to Pollination
    author_email='info@ladybug.tools',
    packages=setuptools.find_namespace_packages(                            # required - that's how pollination find the package
        include=['pollination.*'], exclude=['tests', '.github']
    ),
    install_requires=requirements,
    use_scm_version=_clean_version,
    setup_requires=['setuptools_scm'],
    url='https://github.com/pollination/pollination-honeybee-radiance',      # will be translated to home
    project_urls={
        'icon': 'https://raw.githubusercontent.com/ladybug-tools/artwork/master/icons_bugs/grasshopper_tabs/HB-Radiance.png',
        'docker': 'https://hub.docker.com/r/ladybugtools/honeybee-radiance'
    },
    description='Honeybee Radiance plugin for Pollination.',                # will be used as package description
    long_description=long_description,                                      # will be translated to ReadMe content on Pollination
    long_description_content_type="text/markdown",
    maintainer='mostapha, ladybug-tools',                                   # Package maintainers. For multiple maintainers use comma
    maintainer_email='mostapha@ladybug.tools, info@ladybug.tools',
    keywords='honeybee, radiance, ladybug-tools, daylight',                 # will be used as keywords
    license='PolyForm Shield License 1.0.0, https://polyformproject.org/wp-content/uploads/2020/06/PolyForm-Shield-1.0.0.txt', # the license link should be separated by a comma
    zip_safe=False
)
