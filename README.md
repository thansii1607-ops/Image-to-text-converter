# AI Attention Visualizer

## Live Demo

https://image-to-text-converter-znaxfqv9s2svk7qcwvnjkh.streamlit.app/

## Project Overview

AI Attention Visualizer is a Streamlit-based web application that extracts text from study-note images using Optical Character Recognition (OCR) and visualizes attention scores for the extracted words.

The application takes an image as input, extracts the text, processes the words, generates numerical embeddings, calculates attention scores, and displays the attention results through an interactive web interface.

## Objective

The main objective of this project is to demonstrate the integration of:

- Image processing
- Optical Character Recognition
- Word embeddings
- Attention mechanism
- Data visualization
- Streamlit web application

## Features

- Upload study-note images
- Supports JPG, JPEG, and PNG formats
- Extract text using Tesseract OCR
- Process extracted words
- Generate numerical word embeddings
- Calculate attention scores
- Display word-level attention
- Identify the highest-attention word
- Interactive Streamlit interface

## Technologies Used

- Python
- Streamlit
- NumPy
- Pillow
- Pytesseract
- Tesseract OCR

## System Workflow

```text
Image Upload
      |
      v
Image Processing
      |
      v
OCR Text Extraction
      |
      v
Word Processing
      |
      v
Word Embeddings
      |
      v
Attention Calculation
      |
      v
Attention Visualization
      |
      v
Highest Attention Word
