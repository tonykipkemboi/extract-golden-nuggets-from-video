import streamlit as st
import requests
from datetime import datetime
import os
from dotenv import load_dotenv
import re
import json
import time

# Load environment variables
load_dotenv()

# Constants
BASE_URL = "https://api.twelvelabs.io/v1.2"

def init_session_state():
    """Initialize session state variables"""
    if 'api_key' not in st.session_state:
        st.session_state.api_key = None
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    if 'video_id' not in st.session_state:
        st.session_state.video_id = None

def login():
    """Handle user login"""
    # Set page config
    st.set_page_config(
        page_title="Video Golden Nuggets",
        page_icon="✨",
        layout="centered"
    )

    # Custom CSS
    st.markdown("""
        <style>
        .main-title {
            font-size: 3.2rem !important;
            font-weight: 700;
            color: #1E88E5;
            text-align: center;
            margin-bottom: 1rem;
            padding-top: 2rem;
        }
        .subtitle {
            font-size: 1.4rem !important;
            color: #424242;
            text-align: center;
            margin: 1.5rem auto 3rem auto;
            max-width: 800px;
            line-height: 1.5;
        }
        .feature-box {
            background: white;
            padding: 1.8rem 1.5rem;
            border-radius: 15px;
            border: 2px solid #e3f2fd;
            text-align: center;
            transition: all 0.3s ease;
            height: 100%;
        }
        .feature-box:hover {
            transform: translateY(-5px);
            border-color: #1E88E5;
            box-shadow: 0 5px 15px rgba(30, 136, 229, 0.1);
        }
        .feature-icon {
            font-size: 2.5rem;
            margin-bottom: 1.2rem;
        }
        .feature-text {
            color: #1E88E5;
            font-weight: 500;
            font-size: 1.1rem;
        }
        .login-title {
            font-size: 1.5rem !important;
            color: #1E88E5;
            text-align: center;
            margin: 3rem 0 2rem 0;
        }
        .stButton>button {
            width: 100%;
            margin-top: 1rem;
            height: 3rem;
            background-color: #1E88E5;
            color: white;
            border: none;
            border-radius: 8px;
        }
        .stButton>button:hover {
            background-color: #1565C0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Add some vertical spacing at the top
    st.markdown("<div style='padding: 1.5rem 0;'></div>", unsafe_allow_html=True)

    # Title and subtitle
    st.markdown('<h1 class="main-title">✨ Video Golden Nuggets</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Transform your videos into valuable insights using AI. Extract key moments, memorable quotes, and core messages in seconds.</p>', unsafe_allow_html=True)

    # Feature boxes using Streamlit columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div class="feature-box">
                <div class="feature-icon">🎯</div>
                <div class="feature-text">Smart Video Analysis</div>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div class="feature-box">
                <div class="feature-icon">⚡️</div>
                <div class="feature-text">Real-time Processing</div>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div class="feature-box">
                <div class="feature-icon">💎</div>
                <div class="feature-text">Key Insights Extraction</div>
            </div>
        """, unsafe_allow_html=True)

    # Login section
    st.markdown('<h3 class="login-title">🔑 Enter Your API Key to Get Started</h3>', unsafe_allow_html=True)

    # Center the login form
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        # Get API key
        api_key = st.text_input(
            "Twelve Labs API Key",
            type="password",
            help="Enter your API key to access your indexed videos"
        )
        
        # Add connect button
        if st.button("🔍 Connect to My Videos", type="primary", use_container_width=True):
            if api_key:
                with st.spinner("Connecting to Twelve Labs..."):
                    try:
                        response = requests.get(
                            f"{BASE_URL}/indexes",
                            headers={"x-api-key": api_key}
                        )
                        response.raise_for_status()
                        
                        # If we get here, the API key is valid
                        st.session_state.api_key = api_key
                        st.session_state.authenticated = True
                        st.success("✅ Successfully connected!")
                        time.sleep(1)  # Give user time to see success message
                        st.rerun()
                    except requests.exceptions.RequestException as e:
                        if hasattr(e, 'response') and e.response is not None:
                            try:
                                error_data = e.response.json()
                                st.error(f"❌ API Error: {error_data.get('message', str(e))}")
                            except:
                                st.error("❌ Invalid API key. Please check and try again.")
                        else:
                            st.error(f"❌ Connection error: {str(e)}")
            else:
                st.warning("⚠️ Please enter your API key to continue.")
    
    # Footer with Twelve Labs logo
    st.markdown("---")
    st.markdown("""
        <div style="text-align: center; margin: 1rem 0;">
            <p style="margin-bottom: 0.5rem; color: #666;">Powered by</p>
            <a href="https://twelvelabs.io/" target="_blank" style="text-decoration: none;">
                <img src="https://cdn.prod.website-files.com/63d42c9fdd5148cd77b8f0c6/63d837ee88fec83ad8bd902a_twelvelabs-logo-guideline.svg" 
                     style="height: 30px; vertical-align: middle;">
            </a>
        </div>
    """, unsafe_allow_html=True)
    
    # Sign up info
    st.markdown(
        '<p style="text-align: center; font-size: 0.9rem; color: #666; margin-top: 1rem;">Don\'t have an API key? <a href="https://twelvelabs.io/signup" target="_blank">Sign up for Twelve Labs</a> to get started!</p>',
        unsafe_allow_html=True
    )

def main_app():
    """Main application after authentication"""
    st.title("✨ Video Golden Nuggets Extractor")
    
    # Show logout option
    if st.sidebar.button("Logout"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
    
    # Get available video IDs
    try:
        # Get videos from indexes
        response = requests.get(
            f"{BASE_URL}/indexes",
            headers={"x-api-key": st.session_state.api_key}
        )
        response.raise_for_status()
        data = response.json()
        
        video_options = {}
        if 'data' in data:
            for index in data['data']:
                try:
                    videos_response = requests.get(
                        f"{BASE_URL}/indexes/{index['_id']}/videos",
                        headers={"x-api-key": st.session_state.api_key}
                    )
                    videos_response.raise_for_status()
                    videos_data = videos_response.json()
                    
                    if 'data' in videos_data:
                        for video in videos_data['data']:
                            video_id = video.get('_id')
                            if video_id:
                                name = video.get('metadata', {}).get('filename', 'Untitled')
                                created_at = video.get('created_at', '')
                                if created_at:
                                    from datetime import datetime
                                    created = datetime.fromisoformat(created_at.replace('Z', '+00:00'))
                                    created_str = created.strftime('%Y-%m-%d %H:%M')
                                else:
                                    created_str = 'Unknown date'
                                
                                label = f"{name} (Created: {created_str})"
                                video_options[label] = video_id
                except Exception as e:
                    st.write(f"Error fetching videos for index {index['_id']}: {str(e)}")
                    continue
        
        if video_options:
            selected_video = st.selectbox(
                "Choose a video to analyze",
                options=list(video_options.keys())
            )
            
            if selected_video:
                video_id = video_options[selected_video]
                st.success(f"Selected video ID: {video_id}")
                
                # Add a button to trigger the analysis
                if st.button("🎯 Extract Golden Nuggets"):
                    with st.spinner("Generating insights..."):
                        try:
                            # Prepare the request payload
                            payload = {
                                "video_id": video_id,
                                "prompt": """Identify and list top 3 "golden nuggets" from this video. A "golden nugget" is a particularly valuable, insightful, or impactful moment within the video—a standout segment that offers significant information, memorable quotes, key takeaways, or exceptional entertainment value.

For each golden nugget, please provide:
1. Description: A brief summary (1-2 sentences) of the moment
2. Notable Quote: A notable quote mentioned in the video that captures the golden nugget
3. Significance: An explanation of why this moment is significant or valuable
4. Timestamp: The approximate time within the video when the golden nugget occurs (please use the format HH:MM:SS - HH:MM:SS)

Make sure it's in proper markdown format, and include a title for each golden nugget.""",
                                "temperature": 0.5,
                                "stream": True
                            }
                            
                            # Make the API call
                            response = requests.post(
                                f"{BASE_URL}/generate",
                                headers={
                                    "x-api-key": st.session_state.api_key,
                                    "Content-Type": "application/json"
                                },
                                json=payload,
                                stream=True
                            )
                            
                            # Check for HTTP errors
                            response.raise_for_status()
                            
                            # Create a placeholder for the streaming response
                            output = st.empty()
                            full_text = ""
                            
                            # Process the streaming response
                            for line in response.iter_lines():
                                if line:
                                    try:
                                        json_response = json.loads(line)
                                        if "text" in json_response:
                                            full_text += json_response["text"]
                                            output.markdown(full_text)
                                    except json.JSONDecodeError:
                                        continue
                            
                            # If we got here, the request was successful
                            st.success("✨ Analysis complete!")
                            
                        except requests.exceptions.RequestException as e:
                            st.error("❌ Error making request to Twelve Labs API")
                            if hasattr(e, 'response') and e.response is not None:
                                try:
                                    error_data = e.response.json()
                                    st.error(f"API Error: {error_data.get('message', str(e))}")
                                except:
                                    st.error(str(e))
                            else:
                                st.error(f"Connection error: {str(e)}")
                        except Exception as e:
                            st.error(f"❌ Unexpected error: {str(e)}")
                            import traceback
                            st.error(f"Error details:\n```\n{traceback.format_exc()}\n```")
        else:
            st.warning("No videos found in your indexes. Please make sure you have videos uploaded to your Twelve Labs account.")
            
    except Exception as e:
        st.error(f"Error: {str(e)}")
        if hasattr(e, 'response'):
            st.write("API Error Response:", e.response.json())

# Initialize session state
init_session_state()

# Main app flow
if not st.session_state.authenticated:
    login()
else:
    main_app()
