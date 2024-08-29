# Chaldene

## Installation:


Make sure Python 3.10 is installed.

```
python --version
```
<br>

Clone the GitHub repository.

```
git clone https://github.com/bricarter/chaldene.git
```
<br>

Move into the `chaldene/` directory.

```
cd chaldene/
```
<br>

(Recommended) Create a virtual environment to hold the application's dependencies.

Here is the command to create a virtual environment using python's built in venv module.

```
python -m venv <venv_name> 
```
<br>

If you created a virtual environment in the previous step, activate the environment per your shell instructions.

Here are commands to activate virtual environments created using python's built in venv module.

| Shell | Command |
| --- | --- |
| bash/zsh | source <venv_name>/bin/activate |
| fish | source <venv_name>/bin/activate.fish |
| csh/tcsh | source <venv_name>/bin/activate.csh |
| PowerShell | <venv_name>/bin/Activate.ps1 |
| (Windows) PowerShell | <venv_name>/Scripts/Activate.ps1 |
| (Windows) cmd.exe | <venv_name>/Scripts/activate.bat |
<br>

(Optional) Upgrade pip.

```
pip install --upgrade pip
```
<br>

Install the dependencies found in the `requirements.txt` file.

```
pip install -r requirements.txt
```
<br>

Chaldene is installed and can now be run with the following command.

 ```
 flask run
 ```
 