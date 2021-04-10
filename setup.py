from setuptools import setup
setup(
    name='TypeWriter',
    version='0.0.1',
    entry_points={
        'console_scripts': [
            'TypeWriter=typewriter:run'
        ]
    }
)