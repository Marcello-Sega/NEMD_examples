#!/usr/bin/env python3
"""
Day 2 - liquid vapour coexistance.

"""

import numpy as np
import matplotlib.pyplot as plt
import glob

if __name__ == "__main__":

    #Look for ensemble run
    files = glob.glob("output_*")
    if files == []:
        files = ["./"]

    #Loop over files and average
    rho = []
    for file in files:
        print("Averaging folder ", file)
        density = np.genfromtxt(file+"/day2_density.profile", skip_header=4)
        chunk = density[:,0]
        z = density[:,1]
        ncount = density[:,2]
        rho.append(density[:,3])

    #Plot density
    rho = np.mean(rho,0)
    plt.plot(z, rho)
    plt.show()

    try:
        stress = np.genfromtxt(file+"/day2_stress.profile", skip_header=4)
    except FileNotFoundError:
        print("No stress profile, run with -var localstress 1")

    #Loop over files and average
    P_c = []; P_k = []; P = []
    for file in files:
        chunk = stress[:,0]
        z = stress[:,1]
        ncount = stress[:,2]
        P_c.append(stress[:,3:6]) #Configurational Stress
        P_k.append(stress[:,6:])  #Kinetic Stress

    #Plot Stress
    P_c = np.mean(P_c,0)
    P_k = np.mean(P_k,0)
    P = P_c + P_k #Total Stress k+c

    plt.plot(z, P_c[:,0], '-r',  label="$P^c_{xx}$")
    plt.plot(z, P_c[:,1], '-b',  label="$P^c_{yy}$")
    plt.plot(z, P_c[:,2], '-g',  label="$P^c_{zz}$")
    plt.plot(z, P_k[:,0], '--r', label="$P^k_{xx}$")
    plt.plot(z, P_k[:,1], '--b', label="$P^k_{yy}$")
    plt.plot(z, P_k[:,2], '--g', label="$P^k_{zz}$")
    plt.plot(z, P[:,0], ':r', label="$P_{xx}$")
    plt.plot(z, P[:,1], ':b', label="$P_{yy}$")
    plt.plot(z, P[:,2], ':g', label="$P_{zz}$")

    plt.legend(ncol=3)
    plt.show()

