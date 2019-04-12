import tensorflow as tf
from utils.datas.datas import  *
from utils.nets.nets import  *

generator = G_conv_mnist()
discriminator = D_conv_mnist()
classifier = C_conv_mnist()

data = mnist()