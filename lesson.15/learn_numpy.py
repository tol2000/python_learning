import functools
import operator
import numpy as np

src_shape = (2, 3, 4)
axis = 1

src_shape_seq = (0, 1, 2)
dst_shape_seq = (src_shape_seq[axis],) + tuple(x for n, x in enumerate(src_shape_seq) if n != axis)

res_shape = tuple(x for n, x in enumerate(src_shape) if n != axis)
res_size = functools.reduce(operator.mul, res_shape)
print(f'Result will be with size {res_size} and shape {res_shape}')

prc_shape = (src_shape[axis],) + res_shape

a = np.arange(0, 48, 2).reshape(src_shape)
a

print(f'src_shape: {src_shape}')
print(f'res_shape: {res_shape}')
print(f'prc_shape: {prc_shape}')

res = np.zeros(res_size, dtype=a.dtype).reshape(res_shape)
trf = np.zeros(a.size, dtype=a.dtype).reshape(prc_shape)
trf

src_shape_list = list(src_shape)

for i in range(prc_shape[0]):
    for j in range(prc_shape[1]):
        for k in range(prc_shape[2]):
            trf_tpl = (i, j, k)
            cur_tpl = tuple([trf_tpl[dst_shape_seq[0]], trf_tpl[dst_shape_seq[1]], trf_tpl[dst_shape_seq[2]]])
            print(f'{cur_tpl} -> {trf_tpl}')
            print(f'a: {a[trf_tpl]}')
            trf[trf_tpl] = a[trf_tpl]

trf
