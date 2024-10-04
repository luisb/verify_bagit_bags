import bagit
import argparse
import os

parser = argparse.ArgumentParser(description='Verify bags in a directory')
parser.add_argument('directory', help='Directory containing bags to verify')
args = parser.parse_args()

for dir in os.listdir(args.directory):
    bag_dir = os.path.join(args.directory, dir)
    print(f'Verifying bag {bag_dir}')
    
    bag = bagit.Bag(bag_dir)
    if bag.is_valid():
        print(f'{bag.path} is valid')
    else:
        print(f'{bag.path} is not valid')
