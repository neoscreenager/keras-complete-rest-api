# initialize Redis connection settings
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0

# initialize constants used to control image spatial dimensions and
# data type
IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
IMAGE_CHANS = 3
IMAGE_DTYPE = "float32"

# initialize constants used for server queuing
IMAGE_QUEUE = "image_queue"
BATCH_SIZE = 32
SERVER_SLEEP = 0.25
CLIENT_SLEEP = 0.25

'''
Below is the table that shows image size, weights size, top-1 accuracy,
top-5 accuracy, no.of.parameters and depth of each deep neural net architecture
available in Keras.

Model 	     Image size 	Weights size 	Top-1 accuracy 	Top-5 accuracy 	Parameters 	Depth
Xception 	 299 x 299  	88 MB 	        0.790 	        0.945 	        22,910,480 	  126
VGG16 	     224 x 224 	    528 MB 	        0.715 	        0.901 	        138,357,544    23
VGG19 	     224 x 224 	    549 MB 	        0.727 	        0.910 	        143,667,240    26
ResNet50 	 224 x 224 	    99 MB 	        0.759 	        0.929 	        25,636,712 	  168
InceptionV3  299 x 299 	    92 MB 	        0.788 	        0.944 	        23,851,784 	  159
Inception
ResNetV2 	 299 x 299 	    215 MB 	        0.804 	        0.953 	        55,873,736 	  572
MobileNet 	 224 x 224 	    17 MB 	        0.665 	        0.871 	        4,253,864 	  88

'''
