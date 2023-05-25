import os
import cv2
from paddleocr import PPStructure
import pdfkit

table_engine = PPStructure(show_log=False, layout=False)

img_path = 'Exemple-de-fiche-de-resultat.jpg'
img = cv2.imread(img_path)
result = table_engine(img)
html_content = result[0]['res']['html']

# Save HTML content to a temporary file
html_file_path = 'temp.html'
with open(html_file_path, 'w') as file:
    file.write(html_content)

# Specify the output PDF file path
pdf_file_path = 'output.pdf'

# Convert HTML to PDF
pdfkit.from_file(html_file_path, pdf_file_path)

# Remove the temporary HTML file
os.remove(html_file_path)

print(f"PDF file '{pdf_file_path}' has been generated.")
