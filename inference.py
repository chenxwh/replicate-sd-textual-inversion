import argparse
import torch
from diffusers import StableDiffusionPipeline


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model_dir",
        default="textual_inversion_spyro-dragon",
    )
    parser.add_argument(
        "--prompt",
        default="Golden Gate Bridge in style of <spyro-dragon>.",
    )
    parser.add_argument(
        "--output_path",
        default="output.png",
    )

    args = parser.parse_args()
    
    pipe = StableDiffusionPipeline.from_pretrained(model_id,torch_dtype=torch.float16).to("cuda")
    with torch.autocast("cuda"):
        image = pipe(args.prompt, num_inference_steps=50, guidance_scale=7.5).images[0]

    image.save(args.output)
