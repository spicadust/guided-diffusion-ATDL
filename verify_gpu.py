import tensorflow as tf

def check_gpu():
    # Check if TensorFlow can see any GPUs
    gpus = tf.config.list_physical_devices('GPU')
    
    if not gpus:
        print("No GPU available. TensorFlow is using CPU.")
    else:
        print(f"Number of GPUs available: {len(gpus)}")
        for gpu in gpus:
            print(f"GPU Name: {gpu.name}")
        
        # Try to create a simple operation on the GPU
        try:
            with tf.device('/GPU:0'):
                a = tf.constant([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
                b = tf.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
                c = tf.matmul(a, b)
                print("Matrix multiplication result:")
                print(c)
            print("GPU is working correctly with TensorFlow.")
        except RuntimeError as e:
            print("GPU is available but there was an error using it:")
            print(e)

if __name__ == "__main__":
    check_gpu()
