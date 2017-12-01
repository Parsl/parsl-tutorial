# Author: Yadu Nand Babuji <yadu@uchicago.edu>
# Written for the MPI section of the Parsl tutorial

CC?=mpicc

CFLAGS = -Wall -std=c99

SRC = $(wildcard *.c)

OBJS = $(SRC:.c=.o)

PROGS = $(SRC:.c=)

DEPS = $(wildcard *.h)

all: $(PROGS)

%: %.c $(DEPS)
	$(CC) $(CFLAGS) -o $@ $<

clean:
	rm -f $(PROGS) $(EXEC) *~
