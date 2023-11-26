import cv2
import os

class BackgroundRemover:
    blk_thresh = 0
    scaled_thresh = 0

    def __init__(self):
        self.blk_thresh = 100 #tune?
        self.scaled_thresh = self.valueScaling()

    def remove(self, image_path):
        image = cv2.imread(image_path)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, threshold_img = cv2.threshold(blur, self.blk_thresh, 255, cv2.THRESH_BINARY)
        mask = 255 - threshold_img
        result = cv2.bitwise_and(image, image, mask=mask)

        new_image = os.path.splitext(image_path)[0] + "_noBackground.jpg"
        cv2.imwrite(new_image, result)

    def valueScaling(self):
        min_value = 0
        max_value = 100
        new_min = 0
        new_max = 255
        scaled_value = (self.blk_thresh - min_value) * (new_max - new_min) / (max_value - min_value) + new_min
        return int(scaled_value)

    