config = {
    "sites" : [{
        "site" : "Local_IPP",
        "auth" : {
            "channel" : "local"
        },
        "execution" : {
            "executor" : "ipp",
            "provider" : "local",
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
                    "partition" : "debug"
                }
            }
        }
    }],
    "globals" : { "lazyErrors" : True },
    "controller" : { "publicIp" : "*" }
}
