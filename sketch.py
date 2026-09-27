import cv2

# Step 1: Image ko read karo
image = cv2.imread("woman.jpg")

# Step 2: RGB ko Grayscale me convert karo
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Grayscale image ko invert karo
inverted_gray = 255 - gray_image

# Step 4: Blur karo
blurred = cv2.GaussianBlur(inverted_gray, (21, 21), 0)

# Step 5: Inverted blur ko invert karo
inverted_blurred = 255 - blurred

# Step 6: Pencil Sketch banao
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=256.0)

# Step 7: Sketch dikhao
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch", pencil_sketch)

cv2.waitKey(0)
cv2.destroyAllWindows

