from PIL import Image
from matplotlib import pyplot as plt
from ultralytics import YOLO

# Load the trained model
model = YOLO("yolov8n.yaml")
model._load("runs/detect/train14/weights/best.pt")
# Set the model in evaluation mode
model.val()

# Load the input image
image_path = r"C:\Users\minsa\PycharmProjects\IP\Project\data\images\train\strawberry1.jpg"
image = Image.open(image_path)

# Perform object detection
results = model(image)

# Retrieve the bounding box coordinates and labels
boxes = results[0].xyxy.numpy()
labels = results[0].labels.numpy()

# Annotate the image with bounding boxes and labels
fig, ax = plt.subplots()
ax.imshow(image)

for box, label in zip(boxes, labels):
    x_min, y_min, x_max, y_max = box
    box_width = x_max - x_min
    box_height = y_max - y_min

    # Draw bounding box
    rect = plt.Rectangle((x_min, y_min), box_width, box_height,
                         fill=False, color='red', linewidth=2)
    ax.add_patch(rect)

    # Add label
    class_name = model.names[label]
    ax.text(x_min, y_min - 5, class_name, color='red')

plt.axis('off')
plt.show()
