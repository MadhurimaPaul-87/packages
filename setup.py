from distutils.core import setup
setup(
  name = 'packages',         # How you named your package folder (MyLib)
  packages = ['packages'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'An Anova package',   # Give a short description about your library
  author = 'Madhurima Paul',                   # Type in your name
  author_email = 'mguharoy4@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/MadhurimaPaul-87/packages',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/MadhurimaPaul-87/packages/archive/refs/tags/v_01.tar.gz'
  keywords = ['anova', 'SSB', 'SSW'],   # Keywords that define your package best
   install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
          'matplotlib',
      ],   
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
