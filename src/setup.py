from distutils.core import setup

setup(
    name='Assss',
    version='1.0',
    description='Cool scanner that can scan hosts for potential vulnerabilities. ', 
    author="Ashot Arushanyan, Sergey Kirakosyan, Smbat Voskanyan",
    author_email="smbo.voskanyan2002@gmail.com", #or pthomas@qualys.com
    url='https://github.com/TheSenPie/assss',
    packages=['assss'],
    scripts=['assss/Assss.py'],
    classifiers = [
        "Development Status :: 1 - Pre-Alpha",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Topic :: Internet :: WWW/HTTP"
        "Programming Language :: Python :: 3.x"
    ]
)