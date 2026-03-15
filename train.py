from ultralytics import YOLO

def main():
    print("Loading YOLOv8-OBB base model...")
    # Load the base model
    model = YOLO('yolov8n-obb.pt')

    print("Starting rapid POC training on CPU...")
    # Train using the built-in tiny dataset (dota8.yaml)
    results = model.train(
        data='dota8.yaml',     # Auto-downloads a tiny 8-image dataset!
        epochs=3,              # Only train for 3 rounds (super fast)
        imgsz=320,             # Smaller images so your CPU can handle it quickly
        batch=2,               # Process 2 images at a time
        device='cpu',          # Force CPU usage to bypass your CUDA error
        project='models',      
        name='sat_guard_poc'   # Save to models/sat_guard_poc/
    )

    print("\n✅ Training complete!")
    print("Your test model is saved at: models/sat_guard_poc/weights/best.pt")

if __name__ == '__main__':
    main()