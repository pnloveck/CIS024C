
import argparse
import helper

parser = argparse.ArgumentParser()
parser.add_argument("add1",help = "Provide the 1st number you want to add",type=int)
parser.add_argument("add2",help = "Provide the 2nd number you want to add",type=int)

args  = parser.parse_args()

print helper.num_add(args.add1,args.add2)