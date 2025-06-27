# 🇵🇰 CNIC Information Extractor using Streamlit + GPT-4o

This project allows users to upload or capture an image of a Pakistani CNIC (Computerized National Identity Card) using their camera or device gallery, and then extracts structured information using OpenAI's GPT-4o Vision model.

## 🚀 Features

- Upload CNIC images via camera or file
- Extracts:
  - Full Name
  - Father's Name
  - Gender
  - Nationality
  - Date of Birth
  - CNIC Number
- Works on both desktop and mobile
- Uses OpenAI GPT-4o for accurate image understanding
- Clean, responsive Streamlit interface

## 🧠 Powered By

- Streamlit for the UI
- OpenAI GPT-4o for image analysis

## 📦 Requirements

Install dependencies:

pip install -r requirements.txt

Create a .env file with your OpenAI API key:

OPENAI_KEY=your-api-key-here

Or set it in your terminal session:

export OPENAI_KEY=your-api-key-here

## 📝 How to Run

streamlit run streamlit_app.py

Then open the provided local URL in your browser. On mobile, you'll be able to choose Camera or Gallery when uploading.

## 🛡️ Security Notes

- CNIC images are not stored or saved
- API keys are loaded from a secure environment variable
- Use HTTPS for camera input on mobile browsers

## 📁 Folder Structure

.
├── streamlit_app.py        # Main app
├── requirements.txt        # Dependencies
├── README.md               # Project documentation
└── .env                    # (Optional) For storing OpenAI API key

## 📤 Deployment Options

- Streamlit Cloud
- Railway / Render / VPS (with HTTPS)

## 📄 License

MIT License

## 🙏 Acknowledgments

- OpenAI GPT-4o
- NADRA (format reference only – no real CNIC data is used)
