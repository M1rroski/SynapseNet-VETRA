# federated_learning/model.py
import tensorflow as tf

def create_keras_model():
    """Crea un modelo simple para federated learning."""
    return tf.keras.models.Sequential([
        tf.keras.layers.Dense(10, activation='relu', input_shape=(10,)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
