# Video Golden Nuggets Extractor ✨

A user-friendly web application that helps you extract valuable insights from your videos using the Twelve Labs AI API.

## Features

- Extract top 3 "golden nuggets" from any video
- Get detailed insights including:
  - Descriptions
  - Notable Quotes
  - Timestamps
  - Significance
- Real-time streaming of analysis results
- User-friendly web interface

## Setup

1. Clone this repository
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root and add your Twelve Labs API key:
   ```
   TWELVELABS_API_KEY=your_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your web browser to the URL shown in the terminal
3. Paste your Twelve Labs video ID
4. Click "Extract Golden Nuggets"
5. Watch as the insights are generated in real-time!

## Requirements

- Python 3.7+
- Twelve Labs API key
- Internet connection

## Note

Make sure your video has been uploaded to the Twelve Labs platform first to get a video ID.
