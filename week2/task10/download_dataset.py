import os
import kagglehub
import pandas as pd

current_folder = os.path.dirname(os.path.abspath(__file__))

dataset_folder = os.path.join(
    current_folder,
    "dataset"
)

if os.path.exists(dataset_folder) and os.listdir(dataset_folder):

    print("Dataset already exists.")

else:

    print("Downloading dataset...")

    kagglehub.dataset_download(
        "binib1997/superstore",
        output_dir=dataset_folder
    )

    print("Dataset downloaded successfully.")
