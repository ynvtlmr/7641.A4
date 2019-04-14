# 7641 - Assignment 4
## Markov Decision Processes

Author:
Yaniv Talmor

Adapted from Chad Maron's code

## Output
Output CSVs and images are written to `./output` and `./output/images` respectively. Sub-folders will be created for
each RL algorithm (PI, VI, and Q) as well as one for the final report data.

If these folders do not exist the experiments module will attempt to create them.

Graphing:
---------

The run_experiment script can be use to generate plots via:

```
python run_experiment.py --all
python run_experiment.py --plot
```

Since the files output from the experiments follow a common naming scheme this will determine the problem, algorithm,
and parameters as needed and write the output to sub-folders in `./output/images` and `./output/report`.


 python run_experiment.py --policy ; python run_experiment.py --value ; python run_experiment.py --plot ; 