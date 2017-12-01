config = {
    "sites" : [{
        "site" : "Midway_IPP",
        "auth" : {
            "channel" : "local"
        },
        "execution" : {
            "executor" : "ipp",
            "provider" : "slurm",
            "script_dir" : ".scripts",
            "block" : {
                "nodes" : 1,
                "taskBlocks" : 1,
                "walltime" : "00:05:00",
                "initBlocks" : 1,
                "minBlocks" : 0,
                "maxBlocks" : 1,
                "scriptDir" : ".",
                "options" : {
                    "partition" : "westmere",
                    "overrides" : '''module load mvapich2;
module load python/3.5.2+gcc-4.8;
source /scratch/midway/yadunand/parsl_env_3.5.2_gcc/bin/activate'''
                  }
              }
          }
        }
        ],
    "globals" : {   "lazyErrors" : True },
    "controller" : { "publicIp" :"*" }
}
