# federated_learning/trainer.py
import tensorflow as tf
import tensorflow_federated as tff
from federated_learning.model import create_keras_model

def model_fn():
    """Devuelve un modelo TFF."""
    keras_model = create_keras_model()
    return tff.learning.models.from_keras_model(
        keras_model,
        input_spec=tf.TensorSpec(shape=(None, 10), dtype=tf.float32),
        loss=tf.keras.losses.BinaryCrossentropy(),
        metrics=[tf.keras.metrics.BinaryAccuracy()]
    )

def start_federated_training():
    """Simula un entrenamiento federado básico."""
    # Datos simulados
    def create_client_data():
        x = tf.random.normal((20, 10))
        y = tf.cast(tf.random.uniform((20,)) > 0.5, tf.float32)
        return tf.data.Dataset.from_tensor_slices((x, y)).batch(5)

    client_data = [create_client_data() for _ in range(3)]  # 3 clientes simulados

    iterative_process = tff.learning.algorithms.build_weighted_fed_avg(
        model_fn=model_fn,
        client_optimizer_fn=lambda: tf.keras.optimizers.SGD(learning_rate=0.02),
        server_optimizer_fn=lambda: tf.keras.optimizers.SGD(learning_rate=1.0)
    )

    state = iterative_process.initialize()

    for round_num in range(1, 4):  # 3 rondas de entrenamiento
        state, metrics = iterative_process.next(state, client_data)
        print(f"Ronda {round_num}, métricas: {metrics}")
    
    return { "message": "Entrenamiento federado completo", "final_metrics": metrics }
