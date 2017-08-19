import tensorflow as tf
import os
from src.val import build_graph
from src.train import evaluate_metric
from src import input_data
import numpy as np
import argparse
from src.utils import parse_argstring
from skopt import gp_minimize, dump
import sys

class Hyperopt(object):
    def __init__(self):
        # Parse command line and default parameters
        self.params = self.get_cli_params()
        self.params_dict = vars(self.params)
        self.get_default_params()
        # for k in sorted(self.params_dict.keys()):
        #     print(k, self.params_dict[k])


    def get_cli_params(self):
        # if x is None:
        #     x = [150, 0.67, 100, 0.002, 0.3, 8.0, 1.0,
        #          2000, 20, 0.2, 0.2, 0.2, 0.2, 0.2]

        parser = argparse.ArgumentParser()

        # -------------------------
        # Specify at run time of hyperopt
        parser.add_argument('--which_gpu', default=0, type=int)
        parser.add_argument('--num_labeled', default=100, type=int)
        # parser.add_argument('--static_bn', default=False, nargs='?', const=0.99, type=float)
        parser.add_argument('--dump_path', default='res')
        # parser.add_argument('--lw', action='store_true')
        # layerwise VAT costs
        parser.add_argument('--lw', default=False, nargs='?',
            const='5.0-0.5-0.05-0.05-0.05-0.05-0.05')

        params = parser.parse_args()
        return params

    def add(self, key, default=None, type=None):
        self.params_dict[key] = default

    def get_default_params(self):
        add = self.add
        # -------------------------
        # Use default values
        add('initial_learning_rate', 0.002)
        add('static_bn', 0.99)
        add('end_epoch', 20)
        add('decay_start', 1.0)
        add('decay_start_epoch', 100)
        add('beta1', 0.9)
        add('beta1_during_decay', 0.5)
        add('test_frequency_in_epochs', default=5, type=int)
        add('eval_batch_size', default=100, type=int)
        add('validation', default=1000, type=int)
        add('seed', default=1, type=int)
        add('lr_decay_frequency', default=5, type=int)
        add('batch_size', default=100, type=int)
        add('encoder_layers',
            default=parse_argstring('784-1000-500-250-250-250-10', dtype=int))
        add('num_power_iterations', default=1, type=int)
        add('xi', default=1e-6, type=float)
        add('cnn', False)
        add('ul_batch_size', 250)
        add('encoder_noise_sd', 0.3)

        # rc_weights = [1000, 10, 0.1, 0.1, 0.1, 0.1, 0.1]
        # add('rc_weights', dict(zip(range(len(rc_weights)), rc_weights)))


    def convert_dims_to_params(self, x):

        add = self.add
        # -------------------------
        # Optimize
        add('epsilon', x[0])
        add('rc_weights', dict(zip(range(len(x[1:8])), x[1:8])))

        if self.params.lw is not False:
            lw_eps = x[8:]
            self.params.lw_eps = dict(zip(range(len(lw_eps)), lw_eps))

        return self.params

    def objective(self, x):

        p = self.convert_dims_to_params(x)

        tf.reset_default_graph()

        # -----------------------------
        # Set GPU device to use
        os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
        os.environ["CUDA_VISIBLE_DEVICES"] = str(p.which_gpu)

        # Set seeds
        np.random.seed(p.seed)
        tf.set_random_seed(p.seed)

        # Load data
        print("===  Loading Data ===")
        mnist = input_data.read_data_sets("MNIST_data",
                                          n_labeled=p.num_labeled,
                                          validation_size=p.validation,
                                          one_hot=True,
                                          disjoint=False)
        num_examples = mnist.train.num_examples
        if p.validation > 0:
            mnist.test = mnist.validation
        iter_per_epoch = (num_examples // p.batch_size)
        num_iter = iter_per_epoch * p.end_epoch

        # Build graph
        if p.lw is not False:
            g, m, trainable_parameters = build_graph(p, model='lw')
        else:
            g, m, trainable_parameters = build_graph(p, model='top')

        with tf.Session() as sess:
            init = tf.global_variables_initializer()
            sess.run(init)
            print("=== Training ===")
            for i in range(num_iter):

                images, labels = mnist.train.next_batch(p.batch_size,
                                                        p.ul_batch_size)
                _ = sess.run(
                    [g['train_step']],
                    feed_dict={g['images']: images,
                               g['labels']: labels,
                               g['train_flag']: True})

            print("----------------------------------------")
            print("----------------------------------------")
            print("=== Evaluating ===")
            error = tf.constant(100.0) - m['acc']
            val_err = evaluate_metric(mnist.validation, sess, error, graph=g,
                                      params=p)

        return val_err


def main():

    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # filter out info, warnings

    hyperopt = Hyperopt()

    dims = [
        (0.01, 10.0, 'log-uniform'),    # 0: epsilon
        # rc_weights
        (500., 5000, 'log-uniform'), # 1
        (5.00, 50., 'log-uniform'), # 2
        (0.01, 1.0, 'log-uniform'), # 3
        (0.01, 1.0, 'log-uniform'), # 4
        (0.01, 1.0, 'log-uniform'), # 5
        (0.01, 1.0, 'log-uniform'), # 6
        (0.01, 1.0, 'log-uniform')  # 7
    ]
    x0 = [5.0, 1000, 10, 0.1, 0.1, 0.1, 0.1, 0.1]

    if hyperopt.params.lw is not False:
        dims += [
            (0.5, 5.0, 'log-uniform'), # 8
            (1e-3, 0.5, 'log-uniform'), # 9
            (1e-5, 0.1, 'log-uniform'), # 10
            (1e-5, 0.1, 'log-uniform'), # 11
            (1e-5, 0.1, 'log-uniform'), # 12
            (1e-5, 0.1, 'log-uniform'), # 13
            (1e-5, 0.1, 'log-uniform')  # 14
        ]
        x0 += [1.0, 0.1, 0.001, 0.001, 0.001, 0.001, 0.001]


    print("=== Beginning Search ===")

    res = gp_minimize(hyperopt.objective, dims, n_calls=16, x0=x0, verbose=True)
    print(res.x, res.fun)

    dump(res, hyperopt.params.dump_path + '.gz')



if __name__ == '__main__':
    main()
    # func()
