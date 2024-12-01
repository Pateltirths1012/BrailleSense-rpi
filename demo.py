from picamera2 import Picamera2, Preview, MappedArray
from pprint import pprint
import cv2
import pytesseract
import time
from pybraille import convertText
import re
import RPi.GPIO as GPIO

camera = Picamera2()
preview_config = camera.create_preview_configuration({"size": (1024, 768)})
camera.start_preview(Preview.QTGL)
camera.configure(preview_config)
camera.start()

threshold = 50

display_data = []
detected_data = []
processed_senteces = []

output_file = "detected_text.txt"

def output_text(request):
	colour = (0,255,255)
	font = cv2.FONT_HERSHEY_SIMPLEX
	with MappedArray(request, "main") as m:
		for item in display_data:
			x,y,w,h = item["box"]
			cv2.putText(m.array, item["text"], (x,y), font, (h + 4) / 35, colour, (h + 12) // 12)

camera.post_callback = output_text

def clean_text(text):
        text = re.sub(r"[^a-zA-Z0-9.,!? ]", "", text)  # Remove unwanted characters
        return text.strip().lower()
       
def text_to_braille(file_path):
	try:
		with open(file_path, "r") as file:
			lines = file.readlines()
			braille_text = [convertText(line.strip()) for line in lines if line.strip()]
			return braille_text
	except FileNotFoundError:
		print(f"Error: {file_path} not found.")
		return []

def clear_cache():
	with open(output_file, "w") as file:
		file.write("")
		


while True:
	time.sleep(5)
	start_time = time.time()
	while time.time() - start_time < 15
		array = camera.capture_array()
		data = [line.split('\t') for line in pytesseract.image_to_data(array).split('\n')][1:-1]
		data = [{"text": item[11], "conf": float(item[10]), "box": (item[6], item[7], item[8], item[9])} for item in data]
		data = [item for item in data if item["conf"] > threshold and not item["text"].isspace()]
		for item in data:
			item["box"] = tuple(map(int, item["box"]))
		#pprint(data, width=500, sort_dicts=False)
		detected_text = [item["text"] for item in data]
		print(detected_text)
		
		cleaned_text = [clean_text(text) for text in detected_text]
		
		with open(output_file, "a") as file:
			for line in cleaned_text:
				if line:
					file.write(line + "\n")
		
		#print the cleaned text for debugging
		print("Cleaned Text:", cleaned_text)
		
		#Read and convert text to braille
		braille_text = text_to_braille(output_file)
		print("Cleaned Text:", braille_text) #print the braille conversion
		
		display_data = data
		
	key = cv2.waitkey(1) & 0xFF
	if key == ord("q"):
		camera.stop()
	
	clear_cache()
	print("Restart")



