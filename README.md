# Applying AI-Agents in Unity (C1TAI1) Spring 2026
This is the repository for the Applying AI-Agents in Unity (Spring 2026) course at Borås University

The course schedule can be found on [Kronox](https://www.google.com) and the course material can be found on [Canvas](https://www.google.com).

## Delopment Environment Setup

First, make sure you have installed Visual Studio Code, Git, and Miniconda on your computer.

### Software

Install the following software on your computer:

- [Visual Studio Code](https://code.visualstudio.com)
- [Git](https://git-scm.com/downloads)
- [Miniconda](https://docs.anaconda.com/miniconda/install/#quick-command-line-install)
- [Python](https://www.python.org) (optional) - comes pre-installed on Linux and Mac

### Verify the Software Installation

Verify the software has been successfully installed, by opening a terminal and issuing the following commands (each command should print out a version):

- `code --version`
- `git --version`
- `conda --version`

If you don't see the print-out of a version for a specific tool, make sure the path to your tool's folder has been added to your [`PATH` environment variable](https://gist.github.com/nex3/c395b2f8fd4b02068be37c961301caa7).

### Visual Studio Code (VSCode) Extensions

Then install the necessary Visual Studio Code Extensions by executing the commands below in your terminal:

- `code --install-extension ms-toolsai.jupyter`
- `code --install-extension ms-python.python`

## Course Repository

When you have installed the software above, open a terminal and clone the GitHub repository [C1TAI1_2026](https://github.com/paga-hb/C1TAI1_2026) to your computer, and create a Python environment:

- `git clone https://github.com/paga-hb/C1TAI1_2026.git agents`
- `cd agents`
- `conda create -y -p ./.conda python=3.6`
- `conda activate ./.conda`
- `python -m pip install --upgrade pip`
- `pip install ipykernel jupyter pylance`

## Open the First Workshop Notebook

Finally, make sure you are in the `agents` folder in your terminal, and open the first notebook in Visual Studio Code, by issuing the command below:

- `code -g notebooks/mdp_and_rl_theory.ipynb:0 .`

When the notebook opens in VSCode, click the text `Select Kernel` (in the top-right of the notebook), and choose `Python Environments... => conda (Python 3.6.13) .conda/bin/python`.

Now you can follow the instructions in the notebook.
