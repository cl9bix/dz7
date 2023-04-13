from setuptools import setup

setup(name='myapp',
      version='1.0.0',
      entry_point={'console_scripts':['-e = clean_folder.clean:normalize']})
      
      