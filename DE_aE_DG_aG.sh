#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cat <("$DIR"/getFreeEnergyDiff.py 3-product-freq.out 1-reactant-freq.out)  <("$DIR"/getFreeEnergyDiff.py 2-transition-freq.out 1-reactant-freq.out ) | awk '/E/ {q++; if (q==1) {deltaE=$(NF-1)} else {activE=$(NF-1)}} /G/ {p++; if (p==1) {deltaG=$(NF-1)} else {activG=$(NF-1)}} END {printf "    DE     Ea     DG     Ga   \n---------------------------\n%+6.1f %6.1f %+6.1f %6.1f\n", deltaE, activE, deltaG, activG}'

