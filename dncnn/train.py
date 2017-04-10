import os
import glob
import argparse
import tensorflow as tf
slim = tf.contrib.slim

import trainer

def parse_args():

    parser = argparse.ArgumentParser()
    parser.add_argument("--logdir",
                        type=str,
                        default="log/")
    parser.add_argument("--dataset_dir",
                        type=str,
                        default="flickr")
    parser.add_argument("--checkpoint_basename",
                        type=str,
                        default="artifact")

    parser.add_argument("--batch_size",
                        type=int,
                        default=32)
    parser.add_argument("--image_size",
                        type=int,
                        default=96)
    parser.add_argument("--quality",
                        type=int,
                        default=20)

    parser.add_argument("--learning_rate",
                        type=float,
                        default=0.01)
    parser.add_argument("--decay_steps",
                        type=int,
                        default=25000)
    parser.add_argument("--max_steps",
                        type=int,
                        default=100000)
    parser.add_argument("--decay_ratio",
                        type=float,
                        default=0.5)
    parser.add_argument("--beta1",
                        type=float,
                        default=0.5)

    parser.add_argument("--num_threads",
                        type=int,
                        default=4)
    parser.add_argument("--max_to_keep",
                        type=int,
                        default=100)
    parser.add_argument("--summary_every_n_steps",
                        type=int,
                        default=20)
    parser.add_argument("--save_model_steps",
                        type=int,
                        default=1000)
    parser.add_argument("--min_after_dequeue",
                        type=int,
                        default=5000)
    return parser.parse_args()


def main(args):
    # prepare filenames to read in training
    im_paths = glob.glob("{}/train/origin/*.jpg".format(args.dataset_dir))
    im_names = [path.split(".")[0].split("/")[-1] for path in im_paths]

    t = trainer.Trainer(im_names, args)
    t.fit()

if __name__ == "__main__":
    args = parse_args()
    main(args)
