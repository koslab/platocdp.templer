from setuptools import setup, find_packages
import os

version = '1.6.dev0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='platocdp.templer',
      version=version,
      description="Convenience templer templates for PlatoCDP stuff",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Code Generators",
        ],
      keywords='',
      author='KOSLAB Technologies',
      author_email='izhar@koslab.org',
      url='http://github.com/koslab/platocdp.templer',
      license='MIT',
      packages=find_packages(),
      namespace_packages=['platocdp'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'templer.core',
          'templer.zope',
          'templer.localcommands',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      platocdp_plone = platocdp.templer:PlatoCDPPlone
      platocdp_policy = platocdp.templer:PlatoCDPPolicy
      platocdp_theme = platocdp.templer:PlatoCDPTheme
      platocdp_buildout = platocdp.templer:PlatoCDPBuildout
      platocdp_i18noverride = platocdp.templer:PlatoCDPI18NOverride

      [templer.templer_sub_template]
      content_type = platocdp.templer.localcommands.dexterity:DexterityContent
      behavior = platocdp.templer.localcommands.dexterity:DexterityBehavior
      upgrade_profile = platocdp.templer.localcommands.genericsetup:UpgradeProfile
      skin_layer = platocdp.templer.localcommands.genericsetup:SkinLayer
      schemaextender = platocdp.templer.localcommands.archetypes:SchemaExtender
      basic_portlet = platocdp.templer.localcommands.portlet:BasicPortlet
      nonconfigurable_portlet = platocdp.templer.localcommands.portlet:NonConfigurablePortlet
      viewlet = platocdp.templer.localcommands.browser:Viewlet
      view = platocdp.templer.localcommands.browser:View
      css = platocdp.templer.localcommands.genericsetup:CSSResource
      js = platocdp.templer.localcommands.genericsetup:JSResource
      vocabulary = platocdp.templer.localcommands.components:Vocabulary
      """,
      )
