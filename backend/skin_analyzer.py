from PIL import Image
import random

def analyze_skin(image_path):
    """
    Simple placeholder ML-free skin analysis.
    You will replace this with a real ML model in the future.
    """

    # Random but tuned values for now (70% believable)
    skin_types = ["Dry", "Oily", "Combination", "Normal"]
    skin_tones = ["Fair", "Medium", "Deep", "Olive"]
    acne_levels = ["Clear", "Mild", "Moderate", "Severe"]
    hydration_levels = ["Very Dry", "Moderately Dry", "Balanced", "Well Hydrated"]
    wrinkle_levels = ["Light", "Moderate", "Advanced"]
    pore_sizes = ["Fine", "Medium", "Large"]

    # Generate mock output
    result = {
        "skin_type": random.choice(skin_types),
        "skin_tone": random.choice(skin_tones),
        "acne_level": random.choice(acne_levels),
        "hydration_level": random.choice(hydration_levels),
        "wrinkle_assessment": random.choice(wrinkle_levels),
        "pore_size": random.choice(pore_sizes),
        "overall_score": random.randint(60, 95)
    }

    return result
