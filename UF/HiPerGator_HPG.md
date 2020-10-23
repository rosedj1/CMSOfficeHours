# HiPerGator

The University of Florida has a supercomputer (a cluster of computers) called [HiPerGator (HPG)](https://www.rc.ufl.edu/services/hipergator/).

You have a couple main directories:

```bash
/home/<your_gatorlink_UN>/          # CANNOT handle big files (only has 20 GB of storage)
/blue/<group>/<your_gatorlink_UN>/  # can handle 51000 cores!
```

If you want access to certain software, you typically have to do `module load <package>`. Some examples:

```bash
module load python3  # Can also use the alias: `ml python3`

# Other useful modules:
ml rootpy
ml pycharm
ml tensorflow
ml vscode

# See available modules:
ml spider
ml spider cl   # Look for modules with 'cl' in name.

# Search for all modules that deal with Python.
ml key python

# Useful ml commands:
ml list                     # List your currently loaded modules.
ml purge                    # Unload all modules.
module unload python3       # Unload the python3 module.
ml intel                    # Allows you to do `make` commands.
ml intel/2018 openmpi/3.1.0 # Compiles stuff?
```

## How to submit SLURM scripts

The computer cluster is called **SLURM**
(**S**imple **L**inux **U**tility for **R**esource **M**anagement).

It is useful to add the extension `.sbatch` for SLURM scripts.
If you can run it locally, you can make a SLURM script to do it!

Example SLURM job script (`myslurmscript.sbatch`).

- NOTE: You must remove all characters starting from `#-->` to the end of the line. SLURM doesn't like comments.

```bash
#!/bin/bash                     #--> Could also be something like: #!/usr/bin/env python3
#SBATCH --job-name=my_job                    #--> Job name.
#SBATCH --output=completed_job_%j.log        #--> Output file name. %j=jobID
#SBATCH --error=completed_job_%j_error.log   #--> Error file name.
#SBATCH --mail-type=ALL         #--> Email job status. Options: BEGIN, END, ALL, FAIL, NONE
#SBATCH --mail-user=rosedj1@ufl.edu          #--> Your email.
#SBATCH --nodes=1
#SBATCH --ntasks=1              #--> Number of MPI tasks (processes). Ex: ntasks=1, runs on 1 CPU.
#SBATCH --cpus-per-task=4
#SBATCH --mem=4gb               #--> Total job memory request on a node. Default is 2gb.
#SBATCH --time=2:00:00          #--> Time limit (hh:mm:ss). Can also use: -t=00:01:00
#SBATCH --account=avery         #--> Use resources from this account.
#SBATCH --qos=avery             #--> Specify the QOS (quality of service).

#--> Now put the code you want to run below:
pwd; hostname; date

module load python3

echo "Running my python script."

python3 mypythonscript.py
```

### Notes on submitting to the SLURM scheduler

- Submit the SLURM script by doing: `sbatch myslurmscript.sbatch`
- Check that the job was submitted: `squeue -u rosedj1`
  - You can see the `<job_id>` here.
- Cancel the job: `scancel <job_id>`
- SLURM puts you in a clean shell (none of your aliases will be available).
  - So you should do something like: `source ~/.bash_profile`,
- If you submit your script from, say, this location: `/home/your_UN/work/myscript.sbatch`, then SLURM will put your new shell at: `/home/your_UN/work/`

[Check here](https://help.rc.ufl.edu/doc/Annotated_SLURM_Script)
for more options on SLURM scripts.
Useful options:

- `#SBATCH --mem-per-cpu=600mb    # Memory (RAM) per core/processor/CPU.`

Location of more example SLURM scripts: `/blue/data/training/SLURM/`

- To learn about single jobs, look at: `single_job.sh`
- To learn about parallel jobs, look at: `parallel_job.sh`

Pass in Bash variables into your SLURM script:

```bash
sbatch --export=A=5,b='test' my_script.sbatch
```

## Development Sessions

Before you submit a SLURM script, you can use an **interactive development session** to test your code first.

*When should I use a dev session?*

- When your code takes longer than 10 minutes (wall time).
- When you need more than 64 GB of RAM.
- When you need more than 16 cores.

**NOTE:** There are 6 dev nodes.

### How to start a SLURM interactive session on a compute node

```bash
srun --partition=hpg2-dev --pty bash -i --mem=4gb --ntasks=1 --cpus-per-task=8 --time=04:00:00
```

N.B. `srundev` is an alias for `srun --partition=hpg2-dev --pty bash -i`, so the above simplfies to:

```bash
module load ufrc  # Make the srundev command available.
srundev --mem=4gb --ntasks=1 --cpus-per-task=8 --time=04:00:00

# Another example:
srun -p bigmem --mem=400gb --time=16:00:00 --qos=avery-b --pty bash -i
```

Useful options:

```bash
srundev -h             # help!
srundev --time=04:00:  # begin a 4 hr dev session, with the default 1 processor core and 2 GB of memory
srundev -t 3-0 # session lasts 3 days
srundev -t 60  # session lasts 60 min
# default time is 00:10:00 (10 min) and max time is 12:00:00
# Specify which partition you want to run on - like a dev node:
--partition=hpg2-dev  # Can also choose `bigmem` for large memory tasks.
-p bigmem  # Either the process name or shortcut for --partition.
```

/ufrc/phz5155/$USER
- parallel file system
- CAN handle 51000 cores, reading and writing to it
- 2 TB limit per group
after ssh’ing into HPG, it will take you to:
/home/$USER
- for me this is: /home/rosedj1
- Get 20GB of space
- Has one server (node) hosting

My groups:
- It is CRUCIAL for HEP students to get their `group=avery`

To use class resources, instead of Korytov’s resources:
module load class/phz5155
- each time you want to submit a job, do this command^

See your associations:
showAssoc <username>

See your primary group's info:
slurmInfo
See a particular group's info:
slurmInfo <group>

View resource limits for a particular QOS:
showQos <qos>
- Find your <qos> options by doing `showAssoc`
- Example: `showQos avery`
- As of Pi Day 2020, this account has 100 CPU cores, 360 GB of RAM, and no GPUs. 
- Even more impressively, avery burst qos has 9x these resources! I.e. 3.24 TB of RAM!!!

***Install Python packages into your user area***
ml python3  # Necessary to get the `pip` command 
pip install --user <new_package>
Example: pip install --user vaex

SLURM sbatch directives

```bash
multi-letter directives are double dashes:
--nodes=1	# processors
--ntasks
--ntasks-per-node
--ntasks-per-socket
--cpus-per-task (cores per task)
# Memory usage:
--mem=1gb
--mem-per-cpu=1gb
--distribution

Long option	short option		description
--nodes=1		-N			request num of servers
--ntasks=1		-n			num tasks that job will use (useful for MPI applications)
--cpus-per-task=8	-c
```

If you invest in 10 cores, burst qos can use up to 90 cores!
#SBATCH --nodes=1

Task Arrays
#SBATCH --array=1-200%10	# run on 10 jobs at a time to be nice
$SLURM_ARRAY_TASK_ID 
%A: job id
%a: task id

HPG COMMANDS:

```bash
id                  # see your user id, your group id, etc.
sbatch <script.sh>  # submit script.sh to scheduler
sbatch --qos=phz5155-b <script.sh> 
squeue             # see ALL jobs running
squeue -u rosedj1  # just see your jobs
squeue -j <job_id>
scancel <job_id>   # kill a job
sacct              # View your jobs and account info.
sstat			# 
slurmInfo			# see info about resource utilization; must do: module load ufrc
slurmInfo -p		# partition, a better summary
slurmInfo -g <group_name>	# 
srun --mpi=pmix_v2 myApp
```

Memory utilization = MAX amount used at one point
Memory request = aim for 20-50% of total use

BE WISE ABOUT USING RESOURCES!

- Users have taken up 16 cores and TOOK MORE TIME than just using 1 core!!!

It would be interesting write a SLURM script which submits 
many of the same job with different cores, plots the efficiency vs. num cores

QOS or burstQOS
"Quality of Service"
When you do sbatch, the -b option is “burst capacity” to allow 9x allocation of resources when resources are idle
--qos=phz5155-b
--qos=<group>

*In the job summary email, the memory usage is talking about RAM efficiency*

Time: 
-t
time limit is 31 days
- It is to our benefit to be accurate with job time
- infinite loops will just waste resources and make you think your job is actually working
- the scheduler might postpone your job if it sees it will delay other people's jobs

Learning about Xpra:
module load gui
launch_gui_session -h	# shows help options
- This will load a session on a graphical node on the cluster
- Default time on server is 4 hrs
- use the -a option to use secondary account
- use the -b option to use burst SLURM qos

Paste the xpra url into your local terminal

Do: 
module load gui
launch_gui_session -e <executable>	(e.g., launch_rstudio_gui)
xpra attach ssh:<stuff>
xpra_list_sessions
scancel <job_id>

ln -s <file_path_that's_way_far_away> <dest_path>	# makes a symbolic link from <far_file> to <dest_path>

## Use Jupyter Notebooks on HPG

Go to: https://help.rc.ufl.edu/doc/Remote_Jupyter_Notebook
Copy and paste the SLURM script there.
sbatch <SLURM_job.sh>
In your browser: localhost:<port_number>

ssh -NL 26686:c25a-s26.ufhpc:26686 rosedj1@hpg2.rc.ufl.edu

module add jupyter
launch_jupyter_notebook
- In the job's log file, you will find the host 

Go to [jhub.rc.ufl.edu](jhub.rc.ufl.edu) to use an interactive Jupyter Notebook session on HPG.

The name Jupyter is a combination of other coding languages: Julia + Python + ??? + R
- Although Jupyter notebooks can accommodate R, users prefer R studio. 

You can either go to:
jhub.rc.ufl.edu (hopefully the link works...)
or you can run a SLURM script. I find this way more reliable.

How to run Jupyter Notebooks remotely using a SLURM script:
(1) Log into HPG. 
(2) You only need to do this step if you have never done it before. If you're not sure, then do this step anyway:
module load jupyter
jupyter-notebook password
- When it prompts you for a password, you can put anything or leave it blank.
(3) Make a new file (call it 'practice.sbatch') and put these contents inside:

```bash
#!/bin/bash
#SBATCH --job-name=jupyter
#SBATCH --output=jupyter_notebook_%j.log
#SBATCH --ntasks=1
#SBATCH --mem=2gb
#SBATCH --time=04:00:00
date;hostname;pwd

module add jupyter

launch_jupyter_notebook

# This script was taken from: https://help.rc.ufl.edu/doc/Remote_Jupyter_Notebook#SLURM_Job
```

(4) Do: `sbatch practice.sbatch`
(5) `cat` the log file produced in your area
(6) Copy the line that starts with `ssh` and execute that command in a second local terminal.
(7) Copy the line that looks like 'http://localhost:23775' and paste it into your browser.

Possible errors:
(1) "Resource allocation error" or something similar: This most likely means that your group doesn't have the necessary resources to submit SLURM scripts. How to check it:
- In your HPC terminal: `id`. This will show your group. Ask this person to put ~$1,000,000 towards HPC resources, because science. 
- For more debugging, go to: https://help.rc.ufl.edu/doc/Remote_Jupyter_Notebook

Important Notes:
- You can `import ROOT` but I can only get it to work on Python2 kernels.
- I cannot get feather to work on HPG or IHEPA computers.


Matt's potentially useful JupyNB tutorial:
/ufrc/data/training/Jupyter/Training_demo.ipynb

In the Notebook, do:
%env    # Can set environment variables.
%run     # Run a python script. 
%who    # See all defined variables. 
Put a '!' in front of a bash command to run that bash command!
- e.g. you can 
- I think you can also put %%bash at the top of the cell to run entire blocks of bash commands.
%timeit    # Runs 10K loops of your code, takes the 3 fastest 

df = pd.DataFrame(data, columns=['a','b'])
scatter_matrix(df, alpha=0.9, figsize=())

QUESTIONS:
[X] Why doesn't my squeue command work?
- change bash_profile
[X] I can't reconnect to my screen command because each time I log into the cluster I attach to a different node
- Reattach to: ssh login1
- `hostname` to get host info
[X] Do I have to run sbatch script.sbatch or can I just do ./script.sbatch
- ALWAYS do `sbatch`. This will use the cluster's resources instead of /ufrc/'s (a filesystem) resources. 
- Remember to do `scancel <job_id>`
- `squeue -u rosedj1` to get job_id
- /ufrc/  /orange/  /blue/ are all parallel file systems
- filesystem = hard drive, data storage
- login1, login2 are individual servers
[X] After I do cmsenv, I can't run a Python3 kernel. 
- I can! Lovely. 
[X] You say up above it runs 100K loops but I think it's just 10K loops. 
- It's smart and changes depending on the code!
[X] pandas 
- save files as hdf, as it is native to most systems
- These have trouble working: parquet, pickle, feather
[X] Diff between R and Python?
- R is for statistics!
- R is pure!
- Python has many modules, some of which may be incompatible with others.
[X] Figure out how to get ROOT working on remote Jupyter NB on HPG.
- Only works with Python2 kernel! 


### Use CMSSW on HPG

1. Start a dev session
2. source /cvmfs/cms.cern.ch/cmsset_default.sh    # this makes cmsrel and cmsenv two new aliases for you!
3. Now cmsrel your favorite CMSSW_X_Y_Z

### Vaex on HPG

```bash
ml python3
pip install --user vaex
How to convert root files to hdf5 on HPG:
from root_numpy import root2array
import numpy
import vaex
arr = root2array("<file.root>", "<tree>")
np.savetxt("<file.csv>", arr)
vdf = vaex.from_csv("<file.csv>")
vdf.export_hdf5("<file.hdf5>")
# Hopefully this doesn't get killed...
```

## General HPG Info

Data center near Satchel’s where HiPerGator resides
51000 cores in HPG2 cluster
(only 14000 cores in HPG1)
world-class cluster
3 PB of storage

threaded=parallel=open MPI

## Parallelism ()

### Some terms

- **Process**: A completely different program. Effectively runs in its own Python interpreter.
  - 
- asdf

Can do parallel applications:
- OpenMP, Threaded, Pthreads applications
- all cores on ONE server, shared memory
- CAN'T talk to other servers
MPI (Message Passing Interface)
- applications which can run across multiple servers

ntasks = # of MPI rinks
say you want to run 100 tasks across 10 nodes
100 MPI ranks
You might think the scheduler would put 10 MPI ranks on each node, 
- but it won't be so equal per node, necessarily!
The scheduler may put 30 tasks on one node, and distribute the remaining 70 tasks on other nodes.
Though you can control the ntasks-per-node
Two processors, each processor has 2 cores
16 cores per processor
64 cores per node

For Windows users who need a Terminal:
- MobaXterm
- or the Ubuntu subsystem
Need an SFTP client to move from to your computer
- Cyberduck
- FileZilla
Text editor:
- BBedit(?)

Cluster basics:
ssh’ing puts you into a login node
Then submit a job to the scheduler.
- The scheduler submits the job to the 51000 cores!
- You must prepare a file to tell scheduler what to do (BATCH script)
    - number of CPUS
    - RAM
    - how long to process the job

There are also compute nodes
- this is where the money is! 
- They are optimized to distribute jobs across different computers efficiently

## Resources

- The HPG [help page](help.rc.ufl.edu).
- UFIT [training page](training.it.ufl.edu).

What is HPG?
HPG is essentially just a big cluster of computers.
More technically, it is many interconnected servers (compute nodes). 
Each compute node has either 2 or 4 "sockets" and each socket holds around 32 or 64 "CPU cores" (CPUs). 
Therefore each node has a limited amount of:
- CPU cores, RAM, memory bandwidth, network bandwidth, and local storage.
Impressively, the entire HPG network has ~200 PB of memory (RAM)!!!

The two main partitions are HPG1 (old) and HPG2 (new):
HPG2 has ~500 computers: 
- 2 servers (nodes) per computer, 32 cores per server, 4 GB RAM/core = 256 GB RAM per HPG2 computer
HPG1 has ~250 computers: 
- 1 server (node) per computer, 64 cores per server, 4 GB RAM/core = 256 GB RAM per HPG1 computer
Actually though, there is only about 3.5 GB RAM/core available for processing!

You can get more info on the compute nodes by doing:
module load ufrc
nodeInfo

By default, your jobs will go to these partitions:
- hpg1-compute and hpg2-compute
If you want to specify a particular partition, do:
--partition=<whichever_partition_you_want>
(A list of partitions can be found by doing `nodeInfo`)

Default job parameters given by the scheduler:
1 CPU core
600 MB of memory (RAM)
10 min time limit
- Of course you can change these using directives (flags)!



Terminology:
8 cpus/task = 8 cores on that one server (compute node?)
1 node has: RAM, maybe 2 sockets (processors), each with 2 cores
Each server (compute node, physical server) has either 2 or 4 sockets.
You can also specify the number of tasks per processor: ntasks-per-socket
each processor only has a certain bandwidth to memory
processor = cpu = core


Entire PHZ5155 course is allocated a whole node!
- This is 32 cores on HPG2
The slowdown of your job may be in the bandwidth!

Example directives for specifying the amount of memory:
--mem=4gb
or
--mem-per-cpu=1000mb