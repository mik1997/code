import tensorflow as tf
import pandas as pd


def train(cfg):
    model = tf.keras.Sequential([
    tf.keras.layers.Dense(5, activation='relu', input_shape=(1,)),
    tf.keras.layers.Dense(5, activation='relu'),
    tf.keras.layers.Dense(1)])

    model.compile(optimizer='Adam', loss='mse', metrics='mse')

    data = pd.read_csv(cfg['data_path'], header=None)
    x = data.iloc[:, 0]
    y = data.iloc[:, 1]
    print(x)

    model.fit(x, y, epochs=cfg['epochs'])
