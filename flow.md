sat_guard_project/
│
├── dataset/                # You will place your downloaded images and labels here
│   ├── images/
│   │   ├── train/
│   │   └── val/
│   ├── labels/
│   │   ├── train/
│   │   └── val/
│   └── data.yaml           # Configuration file for the dataset
│
├── models/                 # Your trained weights will be saved here
│   └── yolov8n-obb.pt      # Pre-trained base model (downloads automatically)
│
├── train.py                # Script to train the model
├── app.py                  # Streamlit application
├── requirements.txt        # Python dependencies
└── README.md