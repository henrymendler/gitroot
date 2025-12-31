#-------------------------------#
#      Makefile for DOS systems #
#   using a Turbo c compiler.   #
#-------------------------------#
CC=tcc
CFLAGS=-v -w -ml

calc.exe: calc1.c
         $(CC) $(CFLAGS) -e calc1.exe calc.c

clean:
        erase calc1.exe