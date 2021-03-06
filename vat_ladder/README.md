
## Instructions for running experiments
### 1000 labels
#### Model: clw
```python vat_ladder.py --beta1 0.9 --beta1_during_decay 0.9 --corrupt_sd 0.3 --dataset mnist --decay_start 0.8 --encoder_layers 1000-500-250-250-250-10 --end_epoch 250 --epsilon 2.52055361325-0.0142655442678-0.000600210255729-0.000600210255729-0.000600210255729-0.000600210255729-0.000600210255729 --id full_clw_labeled-1000 --initial_learning_rate 0.002 --logdir logs/ --lr_decay_frequency 10 --lrelu_a 0.1 --model clw --num_labeled 1000 --num_power_iters 3 --rc_weights 3883.31083202-12.3484422252-0.053924582814-0.053924582814-0.053924582814-0.053924582814-0.053924582814 --static_bn 0.99 --test_frequency_in_epochs 5 --vadv_sd 0.5 --validation 0 --which_gpu 0 --xi 1e-6 ```

#### Model: nlw
```python vat_ladder.py --beta1 0.9 --beta1_during_decay 0.9 --corrupt_sd 0.3 --dataset mnist --decay_start 0.8 --encoder_layers 1000-500-250-250-250-10 --end_epoch 250 --epsilon 0.0883744878208-0.00120893605073-0.00809300661658-0.00809300661658-0.00809300661658-0.00809300661658-0.00809300661658 --id full_nlw_labeled-1000 --initial_learning_rate 0.002 --logdir logs/ --lr_decay_frequency 10 --lrelu_a 0.1 --model nlw --num_labeled 1000 --num_power_iters 3 --rc_weights 4427.48669938-5.45001666614-0.0126038172785-0.0126038172785-0.0126038172785-0.0126038172785-0.0126038172785 --static_bn 0.99 --test_frequency_in_epochs 5 --vadv_sd 0.5 --validation 0 --which_gpu 0 --xi 1e-6 ```

#### Model: c
```python vat_ladder.py --beta1 0.9 --beta1_during_decay 0.9 --corrupt_sd 0.3 --dataset mnist --decay_start 0.8 --encoder_layers 1000-500-250-250-250-10 --end_epoch 250 --epsilon 0.108709754061 --id full_c_labeled-1000 --initial_learning_rate 0.002 --logdir logs/ --lr_decay_frequency 10 --lrelu_a 0.1 --model c --num_labeled 1000 --num_power_iters 3 --rc_weights 1923.95759609-39.4668900902-0.48183882327-0.48183882327-0.48183882327-0.48183882327-0.48183882327 --static_bn 0.99 --test_frequency_in_epochs 5 --vadv_sd 0.5 --validation 0 --which_gpu 0 --xi 1e-6 ```

#### Model: n
```python vat_ladder.py --beta1 0.9 --beta1_during_decay 0.9 --corrupt_sd 0.3 --dataset mnist --decay_start 0.8 --encoder_layers 1000-500-250-250-250-10 --end_epoch 250 --epsilon 0.0479063852581 --id full_n_labeled-1000 --initial_learning_rate 0.002 --logdir logs/ --lr_decay_frequency 10 --lrelu_a 0.1 --model n --num_labeled 1000 --num_power_iters 3 --rc_weights 1619.81089345-5.24178539291-0.576045612497-0.576045612497-0.576045612497-0.576045612497-0.576045612497 --static_bn 0.99 --test_frequency_in_epochs 5 --vadv_sd 0.5 --validation 0 --which_gpu 0 --xi 1e-6 ```

### 100 labels
#### Model: clw
```python vat_ladder.py --beta1 0.9 --beta1_during_decay 0.9 --corrupt_sd 0.3 --dataset mnist --decay_start 0.8 --encoder_layers 1000-500-250-250-250-10 --end_epoch 250 --epsilon 0.0730815479025-0.482173463842-0.00140155463202-0.00140155463202-0.00140155463202-0.00140155463202-0.00140155463202 --id full_clw_labeled-100 --initial_learning_rate 0.002 --logdir logs/ --lr_decay_frequency 10 --lrelu_a 0.1 --model clw --num_labeled 100 --num_power_iters 3 --rc_weights 1966.16465847-14.2000743242-0.156300920559-0.156300920559-0.156300920559-0.156300920559-0.156300920559 --static_bn 0.99 --test_frequency_in_epochs 5 --vadv_sd 0.5 --validation 0 --which_gpu 0 --xi 1e-6 ```

#### Model: nlw
```python vat_ladder.py --beta1 0.9 --beta1_during_decay 0.9 --corrupt_sd 0.3 --dataset mnist --decay_start 0.8 --encoder_layers 1000-500-250-250-250-10 --end_epoch 250 --epsilon 0.0730815479025-0.482173463842-0.00140155463202-0.00140155463202-0.00140155463202-0.00140155463202-0.00140155463202 --id full_nlw_labeled-100 --initial_learning_rate 0.002 --logdir logs/ --lr_decay_frequency 10 --lrelu_a 0.1 --model nlw --num_labeled 100 --num_power_iters 3 --rc_weights 1966.16465847-14.2000743242-0.156300920559-0.156300920559-0.156300920559-0.156300920559-0.156300920559 --static_bn 0.99 --test_frequency_in_epochs 5 --vadv_sd 0.5 --validation 0 --which_gpu 0 --xi 1e-6 ```

#### Model: c
```python vat_ladder.py --beta1 0.9 --beta1_during_decay 0.9 --corrupt_sd 0.3 --dataset mnist --decay_start 0.8 --encoder_layers 1000-500-250-250-250-10 --end_epoch 250 --epsilon 0.0320562984459 --id full_c_labeled-100 --initial_learning_rate 0.002 --logdir logs/ --lr_decay_frequency 10 --lrelu_a 0.1 --model c --num_labeled 100 --num_power_iters 3 --rc_weights 744.348310569-5.76127754805-0.777167499267-0.777167499267-0.777167499267-0.777167499267-0.777167499267 --static_bn 0.99 --test_frequency_in_epochs 5 --vadv_sd 0.5 --validation 0 --which_gpu 0 --xi 1e-6 ```

#### Model: n
```python vat_ladder.py --beta1 0.9 --beta1_during_decay 0.9 --corrupt_sd 0.3 --dataset mnist --decay_start 0.8 --encoder_layers 1000-500-250-250-250-10 --end_epoch 250 --epsilon 0.0209401405553 --id full_n_labeled-100 --initial_learning_rate 0.002 --logdir logs/ --lr_decay_frequency 10 --lrelu_a 0.1 --model n --num_labeled 100 --num_power_iters 3 --rc_weights 754.495982501-8.69486925733-0.871556893638-0.871556893638-0.871556893638-0.871556893638-0.871556893638 --static_bn 0.99 --test_frequency_in_epochs 5 --vadv_sd 0.5 --validation 0 --which_gpu 0 --xi 1e-6 ```

### 50 labels
#### Model: clw
```python vat_ladder.py --beta1 0.9 --beta1_during_decay 0.9 --corrupt_sd 0.3 --dataset mnist --decay_start 0.8 --encoder_layers 1000-500-250-250-250-10 --end_epoch 250 --epsilon 0.176257042417-0.00854125262579-0.000184083181869-0.000184083181869-0.000184083181869-0.000184083181869-0.000184083181869 --id full_clw_labeled-50 --initial_learning_rate 0.002 --logdir logs/ --lr_decay_frequency 10 --lrelu_a 0.1 --model clw --num_labeled 50 --num_power_iters 3 --rc_weights 3911.83759511-9.02105649897-0.0593409260282-0.0593409260282-0.0593409260282-0.0593409260282-0.0593409260282 --static_bn 0.99 --test_frequency_in_epochs 5 --vadv_sd 0.5 --validation 0 --which_gpu 0 --xi 1e-6 ```

#### Model: nlw
```python vat_ladder.py --beta1 0.9 --beta1_during_decay 0.9 --corrupt_sd 0.3 --dataset mnist --decay_start 0.8 --encoder_layers 1000-500-250-250-250-10 --end_epoch 250 --epsilon 0.0478824401043-0.0704417429427-0.000854090192827-0.000854090192827-0.000854090192827-0.000854090192827-0.000854090192827 --id full_nlw_labeled-50 --initial_learning_rate 0.002 --logdir logs/ --lr_decay_frequency 10 --lrelu_a 0.1 --model nlw --num_labeled 50 --num_power_iters 3 --rc_weights 1006.29215947-8.66109203716-0.0717106445511-0.0717106445511-0.0717106445511-0.0717106445511-0.0717106445511 --static_bn 0.99 --test_frequency_in_epochs 5 --vadv_sd 0.5 --validation 0 --which_gpu 0 --xi 1e-6 ```

#### Model: c
```python vat_ladder.py --beta1 0.9 --beta1_during_decay 0.9 --corrupt_sd 0.3 --dataset mnist --decay_start 0.8 --encoder_layers 1000-500-250-250-250-10 --end_epoch 250 --epsilon 0.0212469650433 --id full_c_labeled-50 --initial_learning_rate 0.002 --logdir logs/ --lr_decay_frequency 10 --lrelu_a 0.1 --model c --num_labeled 50 --num_power_iters 3 --rc_weights 1918.4990815-32.3557779114-0.799217885741-0.799217885741-0.799217885741-0.799217885741-0.799217885741 --static_bn 0.99 --test_frequency_in_epochs 5 --vadv_sd 0.5 --validation 0 --which_gpu 0 --xi 1e-6 ```

#### Model: n
```python vat_ladder.py --beta1 0.9 --beta1_during_decay 0.9 --corrupt_sd 0.3 --dataset mnist --decay_start 0.8 --encoder_layers 1000-500-250-250-250-10 --end_epoch 250 --epsilon 0.0337167780996 --id full_n_labeled-50 --initial_learning_rate 0.002 --logdir logs/ --lr_decay_frequency 10 --lrelu_a 0.1 --model n --num_labeled 50 --num_power_iters 3 --rc_weights 1862.2207984-8.21492073196-0.053401218333-0.053401218333-0.053401218333-0.053401218333-0.053401218333 --static_bn 0.99 --test_frequency_in_epochs 5 --vadv_sd 0.5 --validation 0 --which_gpu 0 --xi 1e-6 ```
