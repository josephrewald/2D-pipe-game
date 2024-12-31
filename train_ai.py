import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from game_env import PixelLineGameEnv

def create_model(input_shape, action_space):
    model = Sequential([
        Dense(24, activation='relu', input_shape=input_shape),
        Dense(24, activation='relu'),
        Dense(action_space, activation='linear')
    ])
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
    return model

env = PixelLineGameEnv()
model = create_model((4,), env.action_space.n)

episodes = 1000
for episode in range(episodes):
    state = env.reset()
    state = np.reshape(state, [1, 4])
    done = False
    while not done:
        action = np.argmax(model.predict(state)[0])
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, 4])
        target = reward + 0.99 * np.max(model.predict(next_state)[0])
        target_f = model.predict(state)
        target_f[0][action] = target
        model.fit(state, target_f, epochs=1, verbose=0)
        state = next_state

    print(f"Episode {episode + 1}/{episodes} completed")

model.save("2d_pipe_model.h5")
print("Training completed")
