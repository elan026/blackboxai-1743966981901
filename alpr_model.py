import cv2
import pytesseract
import numpy as np

def detect_license_plate(image):
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Edge detection
    edged = cv2.Canny(blurred, 50, 150)
    
    # Find contours
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]
    
    plate = None
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        
        if len(approx) == 4:
            plate = approx
            break
    
    if plate is not None:
        # Extract the license plate region
        mask = np.zeros(gray.shape, np.uint8)
        cv2.drawContours(mask, [plate], 0, 255, -1)
        cv2.bitwise_and(image, image, mask=mask)
        
        # OCR using Tesseract
        x,y,w,h = cv2.boundingRect(plate)
        roi = gray[y:y+h, x:x+w]
        text = pytesseract.image_to_string(roi, config='--psm 11')
        
        return {
            'success': True,
            'plate_text': text.strip(),
            'plate_coordinates': plate.tolist()
        }
    else:
        return {
            'success': False,
            'error': 'No license plate detected'
        }