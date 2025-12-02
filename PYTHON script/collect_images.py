from pathlib import Path
import pandas as pd

from PIL import Image, ImageDraw

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

IMG_DIR = Path("image_files")
IMG_DIR.mkdir(exist_ok=True)


def _create_sample_image():
    """Jodi kono image na thake, ekta simple sample image create korbo."""
    sample_path = IMG_DIR / "sample_image.jpg"
    if sample_path.exists():
        return

    img = Image.new("RGB", (200, 200), color=(100, 150, 200))
    draw = ImageDraw.Draw(img)
    draw.text((50, 90), "Akash", fill=(255, 255, 255))
    img.save(sample_path, "JPEG")


def collect_image_metadata():
    # jodi kono .jpg/.png na thake, ekta sample image create korbo
    if not any(IMG_DIR.glob("*.jpg")) and not any(IMG_DIR.glob("*.png")):
        _create_sample_image()
        print("No image found → created sample_image.jpg inside image_files folder ✔️")

    rows = []
    for path in list(IMG_DIR.glob("*.jpg")) + list(IMG_DIR.glob("*.png")):
        try:
            with Image.open(path) as img:
                width, height = img.size
                mode = img.mode
        except Exception as e:
            print(f"Skip {path.name}: {e}")
            continue

        rows.append({
            "file_name": path.name,
            "width": width,
            "height": height,
            "mode": mode
        })

    if not rows:
        print("No valid images found ❌")
        return

    df = pd.DataFrame(rows)
    df.to_csv(DATA_DIR / "image_metadata.csv", index=False)
    print("Image Metadata Saved Successfully ✔️")


if __name__ == "__main__":
    collect_image_metadata()
