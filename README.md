# 🐾 Pet Name Generator

A smart and interactive web application that generates creative pet names using AI. Simply select your pet type, describe its color, and get personalized name suggestions powered by LangChain and OpenAI.

## ✨ Features

- **Interactive Web Interface**: Clean and user-friendly Streamlit-based UI
- **AI-Powered Name Generation**: Uses OpenAI's GPT-3.5-turbo model for intelligent name suggestions
- **Multiple Pet Types**: Support for Dogs, Cats, Birds, Rabbits, and Hamsters
- **Color-Based Suggestions**: Generates names based on your pet's color characteristics
- **Real-time Generation**: Instant name suggestions with loading indicators
- **Responsive Design**: Works seamlessly on different screen sizes

## 🚀 Technologies Used

- **Python 3.7+**: Core programming language
- **Streamlit**: Modern web application framework for creating interactive UIs
- **LangChain**: Framework for building applications with Large Language Models
- **OpenAI GPT-3.5-turbo-instruct**: AI model for generating creative pet names
- **python-dotenv**: Environment variable management for secure API key handling
- **OpenAI API**: Official OpenAI Python client for API integration

## 📋 Prerequisites

- Python 3.7 or higher
- OpenAI API key
- pip package manager

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Jeremymymy/Pet-Name-Generator-langchain-app.git
   cd Pet-Name-Generator-langchain-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run main.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:8501` to access the application

## 🎯 How to Use

1. **Select Pet Type**: Choose from Dog, Cat, Bird, Rabbit, or Hamster
2. **Enter Pet Color**: Describe your pet's main color (e.g., "brown", "white", "black")
3. **Generate Names**: Click the "Generate Names" button
4. **View Suggestions**: Get 5 creative name suggestions tailored to your pet
5. **Regenerate**: Click "Regenerate" for new suggestions if needed

## 📁 Project Structure

```
Pet-Name-Generator-langchain-app/
├── main.py                        # Main Streamlit application
├── langchain_helper.py            # LangChain integration and AI logic
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
└── .env                           # Environment variables (create this)
```

## 🔧 Configuration

The application uses the following configuration:
- **Model**: GPT-3.5-turbo-instruct
- **Temperature**: 0.7 (balanced creativity and consistency)
- **Max Characters**: 15 for color input
- **Generated Names**: 5 suggestions per request

## 🚨 Error Handling

The application includes comprehensive error handling for:
- Missing OpenAI API key validation
- API rate limit exceeded (RateLimitError)
- Network connectivity issues
- Invalid input validation
- Graceful error messages in both English and Chinese

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [LangChain](https://langchain.com/) for LLM application development
- [OpenAI](https://openai.com/) for the powerful GPT models
- [Python](https://python.org/) for the robust programming language

## 📞 Support

If you encounter any issues or have questions, please:
1. Check the [Issues](https://github.com/Jeremymymy/Pet-Name-Generator-langchain-app/issues) page
2. Create a new issue with detailed information
3. Contact the maintainer

---

**Made with ❤️ using LangChain and OpenAI**
