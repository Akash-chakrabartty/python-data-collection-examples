from pathlib import Path
import pandas as pd
import wave
import struct
import math

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

AUDIO_DIR = Path("audio_files")
AUDIO_DIR.mkdir(exist_ok=True)


def _create_sample_wav():
    """Jodi kono .wav na thake, ekta choto demo tone create korbo."""
    sample_path = AUDIO_DIR / "sample.wav"
    if sample_path.exists():
        return

    framerate = 44100
    duration_sec = 1.0
    freq = 440.0  # A4 tone

    with wave.open(str(sample_path), "w") as wf:
        wf.setnchannels(1)       # mono
        wf.setsampwidth(2)       # 16-bit
        wf.setframerate(framerate)

        frames = []
        for i in range(int(duration_sec * framerate)):
            t = i / framerate
            value = int(32767 * math.sin(2 * math.pi * freq * t))
            frames.append(struct.pack("<h", value))

        wf.writeframes(b"".join(frames))


def collect_audio_metadata():
    # ensure at least one wav file
    if not any(AUDIO_DIR.glob("*.wav")):
        _create_sample_wav()
        print("No .wav found → created sample.wav inside audio_files folder ✔️")

    rows = []
    for path in AUDIO_DIR.glob("*.wav"):
        with wave.open(str(path), "rb") as wf:
            channels = wf.getnchannels()
            rate = wf.getframerate()
            frames = wf.getnframes()
            duration = frames / float(rate) if rate else 0.0

        rows.append({
            "file_name": path.name,
            "channels": channels,
            "sample_rate": rate,
            "n_frames": frames,
            "duration_sec": round(duration, 2),
        })

    df = pd.DataFrame(rows)
    df.to_csv(DATA_DIR / "audio_metadata.csv", index=False)
    print("Audio Metadata Saved Successfully ✔️")


if __name__ == "__main__":
    collect_audio_metadata()
