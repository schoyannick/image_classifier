import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

batch_size = 32
img_height = 65
img_width = 120

data_dir = "images/bet_button"


class BetButtonClassifier:
    def train(self):
        train_ds = tf.keras.utils.image_dataset_from_directory(
            data_dir,
            validation_split=0.2,
            subset="training",
            seed=1234,
            image_size=(img_height, img_width),
            batch_size=batch_size,
        )

        val_ds = tf.keras.utils.image_dataset_from_directory(
            data_dir,
            validation_split=0.2,
            subset="validation",
            seed=1234,
            image_size=(img_height, img_width),
            batch_size=batch_size,
        )

        class_names = train_ds.class_names

        AUTOTUNE = tf.data.AUTOTUNE

        train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
        val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)
        num_classes = len(class_names)

        model = Sequential(
            [
                layers.Rescaling(1.0 / 255, input_shape=(img_height, img_width, 3)),
                layers.Conv2D(16, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Conv2D(32, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Conv2D(64, 3, padding="same", activation="relu"),
                layers.MaxPooling2D(),
                layers.Flatten(),
                layers.Dense(128, activation="relu"),
                layers.Dense(num_classes),
            ]
        )

        model.compile(
            optimizer="adam",
            loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=["accuracy"],
        )

        epochs = 20
        model.fit(train_ds, validation_data=val_ds, epochs=epochs)

        self.save_model(model)
        self.save_class_names(class_names)

        return (model, class_names)

    def save_model(self, model):
        model.save("saved_model/bet_button_classifier")

    def load_model(self):
        new_model = tf.keras.models.load_model("saved_model/bet_button_classifier")
        return new_model

    def save_class_names(self, class_names):
        with open("saved_model/bet_button_class_names.txt", "w") as f:
            for line in class_names:
                f.write(f"{line}\n")

    def load_class_names(self):
        with open("saved_model/bet_button_class_names.txt") as file:
            lines = [line.rstrip() for line in file]
            return lines
