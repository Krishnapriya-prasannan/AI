
### **Day 9 - DCGAN for AI-Powered Image Generation (GANs)**  
This is part of my **#100DaysOfAI** challenge.  
On **Day 9**, I implemented a **Deep Convolutional Generative Adversarial Network (DCGAN)** to generate new images from the **Fashion MNIST** dataset.

---

### **Goal**  
Build a neural network that learns to generate realistic fashion item images using adversarial training between a Generator and a Discriminator.

---

### **Technologies Used**

| Tool             | Purpose                                            |
|------------------|----------------------------------------------------|
| Python           | Main programming language                          |
| TensorFlow / Keras | Deep learning framework                          |
| NumPy            | Data manipulation                                  |
| Matplotlib       | Visualizing generated images                       |
| Fashion MNIST    | Dataset of grayscale fashion item images           |
| VS Code          | Code editor                                        |

---

### **Dataset / Input**  
- Used the **Fashion MNIST** dataset consisting of **28x28 grayscale images** across 10 fashion categories (e.g., sneakers, shirts, bags).

---

### **How It Works**

1. **Data Preprocessing**
   - Normalized pixel values to the [-1, 1] range.
   - Batched and shuffled the training dataset.

2. **Generator Model**
   - Took 100-dimensional random noise as input.
   - Used transposed convolutions to upsample and generate fake images.
   - Output shape: (28, 28, 1)

3. **Discriminator Model**
   - Classified images as real or fake.
   - Used standard convolutional layers with LeakyReLU and Dropout.

4. **Training the DCGAN**
   - Generator tried to fool the discriminator.
   - Discriminator tried to correctly classify real vs. fake.
   - Losses calculated and backpropagated alternately in each step.

5. **Image Generation**
   - After each epoch, generated and saved a batch of fake images.
   - Visualized how the model improved over time.

---

### **Highlights**

- Built a **GAN from scratch** using TensorFlow/Keras.
- Understood adversarial training mechanics through hands-on implementation.
- Learned how the **Generator and Discriminator** compete to improve performance.
- Used **transposed convolutions** to upsample low-dimensional noise to full images.
- Tracked and visualized the progress of generated outputs after each epoch.

---

### **What I Learned**

- The architecture and functioning of **DCGANs**.
- How to use **LeakyReLU, Dropout, BatchNorm** in GAN training.
- Importance of balancing generator/discriminator loss.
- How to handle and visualize image generation tasks.
- Practical GAN training loop logic and checkpointing for image saving.

---

