# 1D fluid simulation code (python version)
[![GitHub license](https://img.shields.io/github/license/ablotekar/OneD-Fluid-Simulation-Python)](https://github.com/ablotekar/OneD-Fluid-Simulation-Python/blob/master/LICENSE.txt) [![GitHub issues](https://img.shields.io/github/issues/ablotekar/OneD-Fluid-Simulation-Python)](https://github.com/ablotekar/OneD-Fluid-Simulation-Python/issues) ![GitHub all releases](https://img.shields.io/github/downloads/ablotekar/OneD-Fluid-Simulation-Python/total) ![GitHub issues](https://img.shields.io/github/issues/ablotekar/OneD-Fluid-Simulation-Python) ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/ablotekar/OneD-Fluid-Simulation-Python) ![GitHub top language](https://img.shields.io/github/languages/top/ablotekar/OneD-Fluid-Simulation-Python)

## Introduction 
It is python version of the 1D fluid simulation code used in the study of 
ion and electron acoustic solitary wave in the different plasma environment. 

Ref:
1. http://dx.doi.org/10.1063/1.4964478
2. http://dx.doi.org/10.1063/1.4991467
3. http://dx.doi.org/10.1029/2018JA026303
4. http://dx.doi.org/10.1063/1.5119993

To understand the methodology use in the development of code please 
refer [Lotekar et. al., Commun. NonlinearSci. Numer. Simul, 2019](http://dx.doi.org/10.1016/j.cnsns.2018.07.041)

In the code the module **"fluidplasma"** consist different functions used in
writing code for particular plasma system. 

## Fluid simulation codes 

The fluid simulation codes are written by using the different useful function from
package **"fluidplasma"**. In the following subsections, the information of
of some codes is give. 

### Ion acoustic solitary wave simulation 
In the package script **"ion_acoustic_solitary_wave_two_componunt_plasma.py"** simulate
ion acoustic solitary wave in the plasma which consist of the fluid ion and 
superthermal electron 

![wkplot](./figures/wkplot.png)

(Figure shows the w-k (frequency-wavenumber) plot generated from the output)


## Note
This code takes a huge time to compute. Hence, it's not practical to use for any research. It is written to understand the algorithm. If user is interested to do fluid simulation please use [fortran version of 1D fluid code.](https://github.com/ablotekar/oneD-fluid-simulation-code-fortran.git)


## Credits
      
This software was developed by Ajay Lotekar ([ablotekar@gmail.com](ablotekar@gmail.com)).

1D fluid simulation code to study the plasma waves in the different plasma environment. 
