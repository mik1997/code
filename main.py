import argparse
import sys
import os
from model.train import train
# Press the green button in the gutter to run the script.

def main(args):

    cfg = args.__dict__

    train(cfg)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Training script for HED')
    parser.add_argument('--epochs', dest='epochs', default=5, type=int)
    parser.add_argument('--train', dest='data_path', default=os.environ.get('SM_CHANNEL_TRAIN'))

    args = parser.parse_args()

    main(args)


