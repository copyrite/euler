libs := gmp
e2: %: %.c
	gcc -o $@.exe $@.c -Wall -Wpedantic -std=c89 $(foreach lib,$(libs),-l$(lib))
