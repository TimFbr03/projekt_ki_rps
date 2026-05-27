import cv2

# Get the Windows host IP from WSL
WINDOWS_HOST = "$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}')"
stream_url = f"http://{WINDOWS_HOST}:8080/video"

cap = cv2.VideoCapture(stream_url)

if not cap.isOpened():
    print("Error: Could not connect to stream.")
    exit()

print("Connected to stream! Press 'q' to quit, 's' to save a snapshot.")

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break
        cv2.imshow("Webcam Stream", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('s'):
            cv2.imwrite("snapshot.jpg", frame)
            print("Snapshot saved.")
finally:
    cap.release()
    cv2.destroyAllWindows()
