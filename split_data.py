"""
This is a script which can split your original training data into two sets for
training and validation.

Run it like:
    ./split_data.py --train_dir=train --val_dir=val --train_percent=70

"""

import argparse
import os
import shutil
import numpy as np

def move_files(args):
    """
    Moves files from train dir to validation dir, depending on the percentage specified
    """
    training_files = []
    for (dirpath, dirnames, filenames) in os.walk(os.path.join('.', args.train_dir)):
        training_files.extend(filenames)

    num_training_files = len(training_files)
    num_validation_files = int((100.0 - args.train_percent)/100*num_training_files)

    print 'Moving {0} files into validation dir'.format(num_validation_files)
    permutation = np.random.permutation(num_training_files)[:num_validation_files]
    destination = os.path.join('.', args.val_dir)
    for pindex in permutation:
        src_filename = os.path.join('.', args.train_dir, training_files[pindex])
        shutil.move(src_filename, destination)
        print 'Moved {0} to {1}'.format(src_filename, destination)
    print 'Complete...'

def main():
    parser = argparse.ArgumentParser(description='Split Training Data')
    parser.add_argument('--train_dir', dest='train_dir', action='store',
                        default='train',
                        help='the training dir name which contains the original training set')
    parser.add_argument('--val_dir', dest='val_dir', action='store',
                        default='val',
                        help='the validation dir name which will contain the data pulled from the training dir')
    parser.add_argument('--train_percent', dest='train_percent', action='store',
                        default=70, type=int,
                        help='the percent of data retained as the training set. The remaining will be in the validation set')
    args = parser.parse_args()

    move_files(args)


if __name__ == '__main__':
    main()
