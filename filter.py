from fuc import pyvcf
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input", type=str, help="input vcf_file")
parser.add_argument("output", type=str, help="output vcf_file")

args = parser.parse_args()

vf = pd.read_csv(args.input, sep='\t')
dvf = pyvcf.VcfFrame(['##fileformat=VCFv4.3'], vf)
dvf.meta
dvf.df
filtered_vf = dvf.filter_qual(30)
filtered_vf.df
filtered1_vf = filtered_vf.markmiss('DP < 10, , greedy=True').df
f = open(args.output,"w")
filtered2_vf = filtered1_vf.markmiss('GT == "0/0"').df
print(filtered2_vf.to_string(),file = f)
f.close()
