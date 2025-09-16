# Python-Assignment-6
# Ubuntu Image Fetcher

A respectful, community-minded tool for collecting images from the web.

## 🌍 Philosophy

Inspired by the Ubuntu principle:  
**"I am because we are."**  
This script connects to the global web, fetches shared visual resources, and organizes them for later appreciation.

## 🛠 Features

- Prompts user for one or more image URLs
- Creates a `Fetched_Images` directory if it doesn't exist
- Downloads and saves images in binary mode
- Extracts or generates safe filenames
- Skips non-image URLs and duplicate downloads
- Handles HTTP and connection errors gracefully

## 📦 Requirements

- Python 3.x
- `requests` library

Install dependencies:
```bash
pip install requests