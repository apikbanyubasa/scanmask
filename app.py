from flask import Flask, render_template, Response
import cv2, os
from ultralytics import YOLO

app = Flask(__name__)
camera = cv2.VideoCapture(0)

# Tentukan path absolute ke best.pt
BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "models", "best.pt")

# Load YOLOv8 model
model = YOLO(MODEL_PATH)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        results = model(frame)[0]
        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cls = int(box.cls[0])
            label = model.names[cls]

            # Pilih warna sesuai label
            if label == "with_mask":
                color = (0,255,0)
            elif label == "without_mask":
                color = (0,0,255)
            elif label == "mask_weared_incorrect":
                color = (0,255,255)
            else:
                color = (255,255,255)

            cv2.rectangle(frame, (x1,y1), (x2,y2), color, 2)
            cv2.putText(frame, label.replace("_"," "), (x1,y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

        ret, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
