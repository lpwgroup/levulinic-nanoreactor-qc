#!/usr/bin/env python

import sys

temperature = 298.15
au2kcal = 627.5096080306

def read_free_energy(fnm):
    for line in open(fnm):
        read_imgfrq_line = 0
        read_enthalpy_line = 0
        read_entropy_line = 0
        conv_crit_met = 0
        if 'Imaginary Frequencies' in line:
            if read_imgfrq_line:
                raise RuntimeError('Second line with Imaginary Frequencies?')
            n_imgfrq = int(line.split()[3])
            read_imgfrq_line = 1
        if 'Convergence criterion met' in line:
            if conv_crit_met == 0:
                escf_plus_gsolv = float(line.split()[1])
            conv_crit_met = 1
        if 'Total Enthalpy:' in line:
            if read_enthalpy_line:
                raise RuntimeError('Second line with Total Enthalpy?')
            enth_kcal = float(line.split()[2])
            read_enthalpy_line = 1
        if 'Total Entropy:' in line:
            if read_entropy_line:
                raise RuntimeError('Second line with Total Entropy?')
            entr_cal_k = float(line.split()[2])
            read_entropy_line = 1
    g_kcal = au2kcal * escf_plus_gsolv
    e_kcal = g_kcal
    g_kcal += enth_kcal
    g_kcal -= temperature * entr_cal_k / 1000
    return e_kcal, g_kcal

def main():
    scf_energy1, free_energy1 = read_free_energy(sys.argv[1])
    scf_energy2, free_energy2 = read_free_energy(sys.argv[2])
    print("Calculating energy differences for %s - %s:" % (sys.argv[1], sys.argv[2]))
    print(" ΔE(SCF+solv) = %.4f kcal/mol" % (scf_energy1 - scf_energy2))
    print(" ΔG           = %.4f kcal/mol" % (free_energy1 - free_energy2))

if __name__ == "__main__":
    main()
