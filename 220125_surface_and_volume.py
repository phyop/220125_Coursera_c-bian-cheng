#!/usr/bin/python3
# -*- coding: utf-8 -*-

# h = int(input("高度h = "))
# w = int(input("寬度w = "))
# d = int(input("長度d = "))

path = "./in.txt"
hwd = []

f = open(path, "r")
lines = f.readlines()
for line in lines:
    hwd.append(int(line))
f.close()

h, w, d = hwd[0], hwd[1], hwd[2]
sur = 2*(h*w + w*d + d*h)
vol = h*w*d

print(sur, vol, end=" ")
print()

"""
#include <stdio.h>

int main ()
{
	int h, w, d;
	int surface_area, volume;

	scanf ( "%d%d%d", &h, &w, &d );

	surface_area	= 2 * ( h * w + w * d + d * h );
	volume 		= h * w * d;

	printf ( "%d %d", surface_area, volume );
	return 0;
}
"""
