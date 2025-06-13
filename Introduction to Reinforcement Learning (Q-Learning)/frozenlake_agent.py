import numpy as np
import gymnasium as gym

# Create the environment
env = gym.make("FrozenLake-v1", is_slippery=True)

# Initialize Q-table
state_space = env.observation_space.n
action_space = env.action_space.n
q_table = np.zeros((state_space, action_space))

# Hyperparameters
alpha = 0.8          # learning rate
gamma = 0.95         # discount factor
epsilon = 1.0        # exploration rate
epsilon_decay = 0.995
epsilon_min = 0.01
episodes = 2000
max_steps = 100

# Training phase
for episode in range(episodes):
    state, _ = env.reset()

    for step in range(max_steps):
        # Epsilon-greedy policy
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state, :])

        new_state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated

        # Q-learning update
        q_table[state, action] = q_table[state, action] + alpha * (
            reward + gamma * np.max(q_table[new_state, :]) - q_table[state, action]
        )

        state = new_state

        if done:
            break

    # Decay exploration rate
    if epsilon > epsilon_min:
        epsilon *= epsilon_decay

# Testing phase
print("\nTesting the agent...\n")
test_episodes = 10
for ep in range(test_episodes):
    state, _ = env.reset()
    done = False
    print(f"Episode {ep + 1}:")

    for step in range(max_steps):
        env.render()
        action = np.argmax(q_table[state, :])
        state, reward, terminated, truncated, _ = env.step(action)
        done = terminated or truncated

        if done:
            print("Reached Goal!" if reward == 1 else "Fell in a hole!")
            break

env.close()
