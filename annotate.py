import cv2


img = cv2.imread("38gt.jpg")
H, W = img.shape[:2]
with open("38gt.txt", "r") as f:
    data = f.readlines()

color_table = [(0, 0, 255), (0, 255, 0), (255, 0, 0)]
class_name = ["Platelets", "RBC", "WBC"]
for d in data:
    label, cx, cy, w, h = map(float, d.split())
    label = int(label)
    xmin = int((cx - (w / 2)) * W)
    xmax = int((cx + (w / 2)) * W)
    ymin = int((cy - (h / 2)) * H)
    ymax = int((cy + (h / 2)) * H)
    cv2.rectangle(img, (xmin, ymin), (xmax, ymax), color_table[label], 2)
    cv2.putText(img, class_name[label], (xmin, ymin), cv2.FONT_HERSHEY_SIMPLEX,
                1, color_table[label], 2)

cv2.imshow("result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("result_imgs/38gt.jpg", img)
