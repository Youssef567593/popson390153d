from setuptools import setup, find_packages

setup(
    name='popson390153d',
    version='0.1.0',
    author='Youssef Dabbach',
    description='مكتبة لتحسين الصور وعرض مناظر ثلاثية الأبعاد',
    packages=find_packages(),
    install_requires=[
        'Pillow',
        'pygame',
        'PyOpenGL',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
