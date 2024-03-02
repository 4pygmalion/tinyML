import os
import math
import subprocess

import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split



def create_data(n_sample:int):
    np.random.seed(0)
    x_values = np.random.uniform(low=0, high=2*math.pi, size=n_sample)
    np.random.shuffle(x_values)
    y_values = np.sin(x_values) + 0.1 * np.random.randn(n_sample)
    
    return x_values, y_values
    
def build_model():
    model = tf.keras.Sequential()
    model.add(tf.keras.layers.Dense(units=16, activation="relu", input_shape=(1,)))
    model.add(tf.keras.layers.Dense(units=16, activation="relu"))
    model.add(tf.keras.layers.Dense(1))
    
    return model

if __name__ == "__main__":
    DIR = os.path.dirname(os.path.abspath(__file__))
    xs, ys = create_data(1000)
    train_x, test_x, train_y, test_y = train_test_split(xs, ys)
    train_x, val_x, train_y, val_y = train_test_split(train_x, train_y)
    
    model = build_model()
    model.compile(optimizer="adam", loss="mse", metrics=["mae"])
    
    history = model.fit(
        train_x, 
        train_y, 
        epochs=15, 
        batch_size=16, 
        validation_data=(val_x, val_y)
    )
    
    loss = model.evaluate(test_x, test_y)
    print(loss)
    
    # Graph to tensorflow-lite
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE] # quantization
    tflite_model = converter.convert()  # serialized
    
    # write
    tfile_output = os.path.join(DIR, "sine_model_quantized.tflite")
    open(tfile_output, "wb").write(tflite_model) # binary 작성합니다.
    quantized_model_size = os.path.getsize(tfile_output)
    print("Quantized model is %d bytes" % quantized_model_size)
    
    # binary to \0x (16bit)
    output_dir = os.path.join(DIR, "sine_model_quantized.cc")
    subprocess.run(f"xxd -i {tfile_output} > {output_dir}", shell=True)
    print(f"save at {output_dir}")
    
    
    
    