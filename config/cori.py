config = {
    "sites" : [
        { "site" : "Cori.Remote.IPP",
          "auth" : {
              "channel" : "ssh",
              "hostname" : "cori.nersc.gov",
              "username" : "yadunand",
              "scriptDir" : "/global/homes/y/yadunand/parsl_scripts"
          },
          "execution" : {
              "executor" : "ipp",
              "provider" : "slurm",  # LIKELY SHOULD BE BOUND TO SITE
              "script_dir" : ".scripts",
              "block" : { # Definition of a block
                  "nodes" : 2,            # of nodes in that block
                  "taskBlocks" : 1,       # total tasks in a block
                  "walltime" : "00:10:00",
                  "initBlocks" : 1,
                  "minBlocks" : 0,
                  "maxBlocks" : 1,
                  "scriptDir" : ".",
                  "options" : {
                      "partition" : "debug",
                      "overrides" : '''#SBATCH --constraint=haswell
module load python/3.5-anaconda ;
source activate /global/homes/y/yadunand/.conda/envs/parsl_env_3.5'''
                  }
              }
          }
        }
        ],
    "globals" : {   "lazyErrors" : True },
    "controller" : { "publicIp" : '*' }
}
