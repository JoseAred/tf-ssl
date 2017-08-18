# -----------------------------
# IMPORTS
# -----------------------------

import argparse
import numpy as np
import tensorflow as tf

# -----------------------------
# PARAMETER PARSING
# -----------------------------

def parse_argstring(argstring, dtype=float, sep='-'):
    return list(map(dtype, argstring.split(sep)))

def get_cli_params():
    parser = argparse.ArgumentParser()
    add = parser.add_argument

    # -------------------------
    # LOGGING
    # -------------------------
    add('--id', default='ladder')
    add('--logdir', default='logs/')
    add('--write_to', default=None)
    # description to print
    add('--description', default=None)

    # option to not save the model at all
    add('--do_not_save', action='store_true')

    # -------------------------
    # EVALUATE
    # -------------------------

    add('--test_frequency_in_epochs', default=5, type=int)
    add('--eval_batch_size', default=100, type=int)
    # validation
    add('--validation', default=0, nargs='?', const=1000, type=int)

    # -------------------------
    # TRAINING
    # -------------------------

    add('--which_gpu', default=0, type=int)
    add('--seed', default=1, type=int)

    add('--end_epoch', default=150, type=int)
    add('--num_labeled', default=100, type=int)
    add('--batch_size', default=100, type=int)
    add('--ul_batch_size', default=100, type=int)

    add('--initial_learning_rate', default=0.002, type=float)
    add('--decay_start', default=0.67, type=float)
    add('--lr_decay_frequency', default=5, type=int)

    # -------------------------
    # LADDER STRUCTURE
    # -------------------------
    # Specify encoder layers
    add('--encoder_layers',
                        default='784-1000-500-250-250-250-10')

    # Standard deviation of the Gaussian noise to inject at each level
    add('--encoder_noise_sd', default=0.3, type=float)

    # Default RC cost corresponds to the gamma network
    add('--rc_weights', default='2000-20-0.2-0.2-0.2-0.2-0.2')

    # Batch norm decay weight mode
    add('--static_bn', default=False, nargs='?', const=0.99, type=float)


    # -------------------------
    # COMBINATOR STRUCTURE
    # -------------------------
    # Specify form of combinator (A)MLP
    # add('--combinator_layers', default='4-1')
    # add('--combinator_sd', default=0.025, type=float)

    # -------------------------
    # VAT SETTINGS
    # -------------------------
    # vat params
    add('--epsilon', default = 8.0, type=float)
    add('--num_power_iterations', default=1, type=int)
    add('--xi', default=1e-6, type=float)

    # weight of VAT cost
    add('--vat_weight', default=0, type=float)

    # weight of AT cost
    add('--at_weight', default=0, type=float)

    # use VAT RC cost at each layer
    # add('--vat_rc', action='store_true')

    # corruption mode
    # add('--corrupt', default='gauss', choices=['gauss', 'vatgauss', 'vat'])
    # weight of entropy minimisation cost
    # add('--ent_weight', default=0, type=float)

    # add('--keep_prob_hidden', default=0.5, type=float)
    # add('--lrelu_a', default=0.1, type=float)
    # add('--top_bn', action='store_true')
    # add('--bn_stats_decay_factor', default=0.99, type=float)

    # -------------------------
    # CNN LADDER
    # -------------------------
    add('--cnn', action='store_true')
    # arguments for the cnn encoder/decoder
    add('--cnn_init_size', default=32, type=int)

    params = parser.parse_args()

    return params

def process_cli_params(params):
    # Specify base structure
    encoder_layers = parse_argstring(params.encoder_layers, dtype=int)
    rc_weights = parse_argstring(params.rc_weights, dtype=float)
    rc_weights = dict(zip(range(len(rc_weights)), rc_weights))
    params.encoder_layers = encoder_layers
    params.rc_weights = rc_weights
    params.decay_start_epoch = int(params.decay_start * params.end_epoch)


    if params.cnn:
        params.cnn_layer_types = ('c', 'c', 'c', 'max', 'c', 'c', 'c', 'max',
                                'c', 'c',
                       'c', 'avg', 'fc')
        params.cnn_fan = (3, 96, 96, 96, 96, 192, 192, 192, 192, 192, 192, 192,
                      192, 10)
        params.cnn_ksizes = (3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 1, None, None)
        params.cnn_strides = (1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, None, None)
        params.num_layers = len(params.cnn_fan) - 1
        # assert len(params.rc_weights) == len(params.cnn_fan) -1


    else:
        params.num_layers = len(params.encoder_layers) - 1

    params.encoder_layers = params.cnn_fan if params.cnn else \
        params.encoder_layers

    # NUM_EPOCHS = params.end_epoch
    # NUM_LABELED = params.num_labeled

    return params

def count_trainable_params():
    trainables = tf.trainable_variables()
    return np.sum([np.prod(var.get_shape()) for var in trainables])

def order_param_settings(params):
    param_dict = vars(params)
    param_list = []
    for k in sorted(param_dict.keys()):
        param_list.append(str(k) + ": " + str(param_dict[k]))

    return param_list

def preprocess(placeholder, params):
    return tf.reshape(placeholder, shape=[
        -1, params.cnn_init_size, params.cnn_init_size, params.cnn_fan[0]
    ]) if params.cnn else placeholder


def get_batch_ops(batch_size):
    join = lambda l, u: tf.concat([l, u], 0)
    split_lu = lambda x: (labeled(x), unlabeled(x))
    labeled = lambda x: x[:batch_size] if x is not None else x
    unlabeled = lambda x: x[batch_size:] if x is not None else x
    return join, split_lu, labeled, unlabeled