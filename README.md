LWR2Weight
==========

(C) 2013 Jorge Tornero Núñez
    http://imasdemase.com


What is it?
===========

LWR2Weight is a tool for computing the Weight of a length frequency distribution of fishes from the length-Weight relationship (LWR) of its species. This is a common calculation in fisheries science but the main purpose of LWR2Weight is to help in fishing surveys when the sample Weight of a length frequency distribution is missing (lost, unrcorded or unreliable due to mistakes while recording the data). Despite this, LWR2Weight main purpose is about gaining skill in python programming and git.

LWR2Weight stores the LWR data (family, species, geographical area and type of measurement, length range and n,a,b and r parameters for a given LWR, as well as the bibliographical source of the data) in a sqlite database, making possible to add more LWR's not only for other species but for different geographical areas of a species.



FEATURES
========

- Calculation of the Weight of length frequency distributions of fishes from the LWR of the species.
- Cross-checking of length distribution-LWR prediction range to prevent extrapolation.


DEPENDENCIES
============

TODO

INSTALL/UNINSTALL
=================

TODO

CHANGELOG
=========

2013/09/25
-----
First working release. Still lot of things/improvements to do:

- Cleaner code (Must learn first!)
- License and acknowledgement actions in menu must work
- PEP8tize all the code
- Edit/add Length-Weight Relationships (Single/batch)
- Get bibliographic info for the LWR2Weight

An initial dataset of Length-Weight Relationships is provided in the file LWR.data. The data comes from the article:

M.A. Torres, F. Ramos, I. Sobrino, Length–Weight relationships of 76 fish species from the Gulf of Cadiz (SW Spain), Fisheries Research, Volumes 127–128, September 2012, Pages 171-175, ISSN 0165-7836, http://dx.doi.org/10.1016/j.fishres.2012.02.001.
(http://www.sciencedirect.com/science/article/pii/S0165783612000562)

