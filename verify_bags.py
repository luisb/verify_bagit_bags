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
    try:
        bag.validate(processes=5)
    except bagit.BagValidationError as e:
        for d in e.details:
            if isinstance(d, bagit.ChecksumMismatch):
                print(f'    Expected {d.path} to have {d.algorithm} checksum of {d.expected} but found {d.found}')
    except bagit.BagError as e:
        print(f'    Error encountered while validating {bag.path}:')
        print(f'        {e}')
    else:
        print(f'    {bag.path} is VALID.')
