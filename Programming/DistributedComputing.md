# Distributed Computing

Parallel processing.

## Condor

[Docs.](https://htcondor.readthedocs.io/en/latest/)

Example from Bockjoo:

```bash
# On HiPerGator:
/home/bockjoo/site/ce/cms.rc.ufl.edu/check_site_slurm.sub

# To submit a condor-g job from cms.rc.ufl.edu, just execute:
condor_submit check_site_slurm.sub
```

You need to provide a script that runs on the worker node and puts it in the
same directory as `check_site_slurm.sub`.

- [Description](https://htcondor.com/htcondor-ce/v5/remote-job-submission/)
of job submission.

## SLURM

[Docs.](https://help.rc.ufl.edu/doc/UFRC_Help_and_Documentation)

## CRAB