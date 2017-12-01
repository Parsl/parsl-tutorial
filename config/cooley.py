config = {
    "sites": [{
        "site": "ALCF_Cooley_Local",
        "auth": {
            "channel": "local",
            "hostname": "cooleylogin1.alcf.anl.gov"
        },
        "execution":  {
            "executor": "ipp",
            "provider": "cobalt",
            "scriptDir": ".scripts",
            "block": {
                "nodes": 1,
                "walltime": "00:20:00",
                "initBlocks": 1,
                "maxBlocks": 1,
                "minBlocks": 0,
                "taskBlocks": "$CORES",
                "scriptDir": ".",
                "options": {
                    "overrides": "source activate /projects/CSC249ADCD01/conda_envs/parsl_env_1",
                    "account": "CSC249ADCD01"
                },
            },
        },
    }],
    "controller": {"publicIp": "*"},
    "globals": {"lazyErrors": True},
}
