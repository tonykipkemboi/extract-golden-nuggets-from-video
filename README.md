# Video Golden Nuggets Extractor 

An AI-powered Streamlit application that helps you extract valuable insights from your videos using the Twelve Labs AI API. This tool analyzes your videos and identifies the most significant moments, providing detailed information about each "golden nugget" including descriptions, quotes, timestamps, and their significance.

## Features

- **Smart Video Analysis**: Extract top 3 "golden nuggets" from any video
- **Comprehensive Insights** for each nugget:
  - Detailed Description
  - Notable Quotes
  - Timestamps (HH:MM:SS format)
  - Significance and Impact
- **Real-time Processing**: Watch as insights are generated in real-time
- **User-friendly Interface**: Clean, modern design with intuitive controls
- **Secure Authentication**: Safe API key handling
- **Markdown Formatting**: Well-formatted, easy-to-read output

## Setup

1. **Prerequisites**:
   - Python 3.7+
   - Twelve Labs API key
   - Internet connection

2. **Installation**:
   ```bash
   # Clone the repository
   git clone https://github.com/tonykipkemboi/extract-golden-nuggets-from-video.git
   cd extract-golden-nuggets-from-video

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Configuration**:
   Create a `.env` file in the project root:
   ```
   TWELVELABS_API_KEY=your_api_key_here
   ```

## Usage

1. **Start the Application**:
   ```bash
   streamlit run app.py
   ```

2. **Access the Web Interface**:
   - Open your browser to the URL shown in the terminal
   - Usually `http://localhost:8501`

3. **Extract Insights**:
   - Enter your Twelve Labs API key
   - Select a video from your indexed videos
   - Click "Extract Golden Nuggets"
   - Watch as the AI analyzes your video!

## Important Notes

- **Video Preparation**: Videos must be uploaded and indexed on the Twelve Labs platform first
- **API Key**: Get your API key from [Twelve Labs](https://twelvelabs.io/signup)
- **Rate Limits**: Be aware of your API usage limits

## Security

- API keys are handled securely
- No credentials are stored permanently
- Environment variables are used for sensitive data

## Contributing

Contributions are welcome! Feel free to:
- Open issues
- Submit pull requests
- Suggest improvements
- Report bugs

## 🎨 Customization

The app uses a custom light theme for better readability. You can modify the theme by editing `.streamlit/config.toml`:
```toml
[theme]
base="light"
primaryColor="#1E88E5"  # Twelve Labs blue
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"
```

## License

MIT License - feel free to use this project for your own purposes!

## Acknowledgments

- Powered by [Twelve Labs](https://twelvelabs.io) AI
- Built with [Streamlit](https://streamlit.io)
