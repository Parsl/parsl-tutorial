#include <stdlib.h>
#include <stdio.h>
#include <mpi.h>
#include <assert.h>

#define error(format, ...) fprintf(stderr, format , __VA_ARGS__)

int main(int argc, char **argv)
{
    int nprocs;
    int myrank;
    int stat;
    int namelen;
    char processor_name[MPI_MAX_PROCESSOR_NAME];

    MPI_Init(&argc, &argv);
    stat = MPI_Comm_size(MPI_COMM_WORLD, &nprocs);
    if ( stat != 0 ) error ("MPI_Comm_size returned an error code : %d", stat);

    stat = MPI_Comm_rank(MPI_COMM_WORLD, &myrank);
    if ( stat != 0 ) error ("MPI_Comm_rank returned an error code : %d", stat);

    MPI_Get_processor_name(processor_name, &namelen);

    fprintf(stdout, "[Rank:%d/%d] Hello World from %s \n", myrank, nprocs, processor_name);

    MPI_Finalize();
    return 0;
}
