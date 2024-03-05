import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.metrics import accuracy_score

# Separate features and target
X = df.drop('Activity', axis=1)
y = df['Activity']

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Print the shapes of the train and test sets
print('X_train shape:', X_train.shape)
print('y_train shape:', y_train.shape)
print('X_test shape:', X_test.shape)
print('y_test shape:', y_test.shape)

# Create a dictionary to map activity names to integers
activity_to_int = {
    'WALKING': 0,
    'WALKING_UPSTAIRS': 1,
    'WALKING_DOWNSTAIRS': 2,
    'SITTING': 3,
    'STANDING': 4,
    'LAYING': 5
}

# Convert activity names to integers in y_train
y_train = np.array([activity_to_int[activity] for activity in y_train])

# Convert activity names to integers in y_test
y_test = np.array([activity_to_int[activity] for activity in y_test])

# Print the updated y_train and y_test
print('y_train:', y_train)
print('y_test:', y_test)

# Reshape the data for LSTM input (samples, time steps, features)
X_train = np.reshape(X_train.values, (X_train.shape[0], X_train.shape[1], 1))
X_test = np.reshape(X_test.values, (X_test.shape[0], X_test.shape[1], 1))

# Build the LSTM model
model = Sequential()
model.add(LSTM(units=50, input_shape=(X_train.shape[1], 1)))
# Multiclass classification output
model.add(Dense(units=6, activation='softmax'))
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# This code defines a sequential model with an LSTM layer followed by a Dense layer with softmax activation. The LSTM layer is designed to capture temporal dependencies in the input data, while the Dense layer with softmax activation outputs probabilities for each of the 6 classes, allowing the model to perform multi-class classification.

# Train the model
history = model.fit(X_train, y_train, epochs=20, batch_size=32,
                    validation_data=(X_test, y_test), verbose=1)

# Evaluate the model
score = model.evaluate(X_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
