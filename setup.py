import setuptools

with open("README.md", 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='reaver',
    version='2.0.0',
    author='Roman Ring',
    author_email='inoryy@gmail.com',
    description='Reaver: Deep Reinforcement Learning Agent for StarCraft II',
    long_description=long_description,
    keywords='reaver starcraft tensorflow machine reinforcement learning neural network',
    include_package_data=True,
    packages=setuptools.find_packages(),
    install_requires=[
        'numpy >= 1.13',
        'PySC2 >= 2.0',
        'absl-py >= 0.2.2',
        'gin-config >= 0.1.1',
        'tensorflow-probability >= 0.4.0'
    ],
    extras_require={
        'tf-cpu': [
            'tensorflow >= 1.10.0',
        ],
        'tf-gpu': [
            'tensorflow-gpu >= 1.10.0',
        ],
        'gym': [
            'PyOpenGL',
            'gym >= 0.9',
            'opencv-python'
        ],
        'atari': [
            'Pillow',
            'PyOpenGL',
            'gym >= 0.9',
            'atari_py >= 0.1.4',
        ],
        'mujoco': [
            'imageio',
            'gym >= 0.9',
            'mujoco_py >= 1.50',
        ]
    },
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    url='https://github.com/inoryy/reaver-pysc2',
)
