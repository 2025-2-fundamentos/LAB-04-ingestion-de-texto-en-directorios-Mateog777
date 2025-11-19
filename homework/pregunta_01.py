import os
import zipfile
import pandas as pd

def pregunta_01():
    zip_path = "files/input.zip"
    input_dir = "files/input"
    output_dir = "files/output"

    if not os.path.isdir(input_dir):
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall("files")

    os.makedirs(output_dir, exist_ok=True)

    def build_dataset(split):
        base_path = os.path.join(input_dir, split)
        rows = []
        for sentiment in os.listdir(base_path):
            sentiment_path = os.path.join(base_path, sentiment)
            if os.path.isdir(sentiment_path):
                for fname in os.listdir(sentiment_path):
                    if fname.endswith(".txt"):
                        fpath = os.path.join(sentiment_path, fname)
                        with open(fpath, "r", encoding="utf-8") as f:
                            text = f.read().strip()
                        rows.append({"phrase": text, "target": sentiment})
        return pd.DataFrame(rows)

    train_df = build_dataset("train")
    train_df.to_csv(os.path.join(output_dir, "train_dataset.csv"), index=False)

    test_df = build_dataset("test")
    test_df.to_csv(os.path.join(output_dir, "test_dataset.csv"), index=False)
