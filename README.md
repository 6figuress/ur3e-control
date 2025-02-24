# ur-control
A Python lib to control:
- a Universal Robots UR3-e arm
- a Robotiq Hand-Wrist Camera
- a Robotiq Two Fingers Adaptive Gripper

## Usage
Open the given Jupyter notebook to get a quick library overview:

- [ISCoin](ISCoin.ipynb): simple tests for the three modules
- [CamSettings](CamSettings.ipynb): a demonstrator to manually modify the camera 

## Install

### Poetry 

This codebase uses [poetry](https://python-poetry.org/docs/#installing-with-the-official-installer) for dependency management. Poetry can be installed with the command
```bash
curl -sSL https://install.python-poetry.org | python3 -
```
or, from a Windows Power shell, with
```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```
Make sure to add `poetry` to your `PATH` (see poetry documentation).

From the repository's top-level, run
```bash
poetry install
```

The virtual python environment can then be activated by invoking a `poetry shell`.

## Forks
Basecode is a fork of https://github.com/Mandelbr0t/UniversalRobot-Realtime-Control/tree/master.

## Credits
* [AMA](https://people.hes-so.ch/fr/profile/4756082430-axel-amand)
* [RIU](https://people.hes-so.ch/fr/profile/2314729-murielle-richard)