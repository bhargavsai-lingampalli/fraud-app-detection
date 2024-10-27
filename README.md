
# Fraud Detection and Sentiment Analysis for Mobile Applications

## Project Overview

This project focuses on detecting fraudulent mobile applications. It incorporates Natural Language Processing (NLP) for sentiment analysis of user feedback to identify potential fraud. The system is built to scrape data from Google Play Store, analyze user reviews, and apply both fraud detection algorithms and sentiment analysis to flag suspicious apps.

## Live Demo

Check out the live demo of the project here: [Fraud Detection App](https://project-mini.streamlit.app/)


## Features
- **Fraud Detection**: Employs machine learning models to detect fraud patterns in mobile applications based on reviews and ratings.
- **Sentiment Analysis**: Uses NLP techniques to extract sentiment (positive, neutral, or negative) from user feedback, helping identify fraudulent or problematic apps.
- **Scraping**: Utilizes Google Play Scraper to gather app data and reviews.
- **Summarization**: Provides summarization of user reviews to gain quick insights into general app sentiment.

## Project Structure

- **fraud_detection.py**: Implements the machine learning model for fraud detection.
- **summarizer.py**: Handles summarization of user reviews using NLP techniques.
- **project.py**: Integrates all components and serves as the main script.
- **ai_summary.py**: Uses Gemini AI to summarize the user reviews.
- **requirements.txt**: Specifies the dependencies for the project.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/bhargavsai-lingampalli/fraud-app-detection
   cd fraud-app-detection
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Requirements

The project relies on the following libraries:
- `emoji~=2.12.1`
- `google-play-scraper~=1.2.7`
- `nltk~=3.8.1`
- `numpy~=1.26.4`
- `sumy~=0.11.0`
- `textblob~=0.18.0.post0`
- `google-generativeai~=0.7.2`
- `streamlit~=1.39.0`

For more details, see the [requirements.txt](requirements.txt).

## Usage

1. Run the main project script:
   ```bash
   streamlit run project.py
   ```

2. To use the fraud detection model:
   ```bash
   python fraud_detection.py
   ```

## Future Enhancements

- Add more robust fraud detection algorithms.
- Improve the accuracy of sentiment analysis.

## Contributions

Feel free to contribute by submitting issues or pull requests.
