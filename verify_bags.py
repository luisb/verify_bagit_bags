import bagit
import argparse
import os

parser = argparse.ArgumentParser(description='Verify bags in a directory')
parser.add_argument('directory', help='Directory containing bags to verify')
args = parser.parse_args()

count = 0
bag_list = [f.path for f in os.scandir(args.directory) if f.is_dir()]
for bag_dir in sorted(bag_list):
    count += 1
    print(f'{count}. Verifying bag {bag_dir}')
    
    bag = bagit.Bag(bag_dir)
    if bag.is_valid():
        print(f'{bag.path} is valid')
    else:
        print(f'{bag.path} is not valid')
