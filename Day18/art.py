
# Step 1: Install required libraries
# Run this cell only once (or if not installed)
# !pip install diffusers transformers accelerate scipy safetensors

# Step 2: Import necessary libraries
from diffusers import StableDiffusionPipeline
import torch

# Step 3: Load the Stable Diffusion model pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", 
    torch_dtype=torch.float16
)

# Step 4: Move the pipeline to GPU for faster inference
pipe = pipe.to("cuda")

# Step 5: Provide a text prompt for the image
prompt = "a futuristic city floating in the sky, highly detailed, digital art"

# Step 6: Generate the image
image = pipe(prompt).images[0]

# Step 7: Display or save the generated image
image.show()                    
# image.save("ai_art.png")      
