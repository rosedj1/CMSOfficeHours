# Anaconda

The most popular, open source Python distribution platform in the world.
Conda makes managing your Python packages super easy.
Check it out in all its glory [here](https://www.anaconda.com/).

```python
"[Package, dependency and environment management for any language](https://conda.io/en/latest/) — Python, R, Ruby, Lua, Scala, Java, JavaScript, C / C++, FORTRAN, and more."
```

Conda tends to take care of all the dependencies when installing packages!

---

## How to install Anaconda

1. Go to the [Anaconda website](https://www.anaconda.com/products/individual)
to choose the **correct installation script** for your OS.
1. Use the `wget` command to download the  script.

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
```

1. Run the  script (you can even install Anaconda on remote machines):

```bash
bash Anaconda3-2020.02-Linux-x86_64.sh
```

---

## How to use Anaconda

### Set up your conda environment

```bash
conda create -n my_env # Create an environment called "my_env".
conda activate my_env  # Start up the environment.
# May have to do `source activate my_env`
conda deactivate       # Leave the environment.
```

### Install packages

The basic syntax is:

```bash
conda install numpy

# Install specific versions of packages:
conda install python=3.8.0
conda install scipy=2.3.4 -n my_env  # Can install specific versions into specific virtual envs.

# Install from a specific channel:
conda install -c conda-forge root

# Update a package:
conda update root
```

Install ROOT and all necessary dependencies:

```bash
conda create -n new_env root -c conda-forge

# So now you can do:
root             # Open up ROOT!
python; import ROOT
root --notebook  # Starts a JupyNB?
rootbrowse       # Opens up a TBrowser!
```

### Other useful `conda` commands

```bash
conda info -e  # See info about all your environments.

conda install -n my_venv numpy     # Install additional packages into my_venv.
conda install -n my_venv -c conda-forge numpy  # Install from a specific channel.

conda remove -n my_env --all  # Delete a conda env.

conda config --env --add channels conda-forge  # Avoids typing `-c conda-forge` all the time.

# Conda doesn't make it easy to rename an env.
# You have to clone it and delete the original:
conda create --name newboy --clone oldboy
conda remove --name oldboy --all
```

Important conda-related `bash` env variables:

```bash
$ROOTSYS
$CONDA_PREFIX
```
