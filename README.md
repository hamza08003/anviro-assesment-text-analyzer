# 🤖 AI Text Analyzer

An AI-powered microservice that performs sentiment analysis and text summarization using machine learning and LLM APIs.

## 🛠️ Technologies Used

- **FastAPI**: Python web framework
- **TextBlob**: Natural language processing library for sentiment analysis
- **OpenRouter API**: Free LLM API for text summarization
- **Docker**: Containerization
- **Uvicorn**: ASGI server

## 📋 Prerequisites

- Python 3.10+
- Docker (for containerized deployment)
- OpenRouter API key (free from [openrouter.ai](https://openrouter.ai))

## 🚀 Setup Instructions

### Option 1: Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-text-analyzer.git
   cd ai-text-analyzer
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   python -m textblob.download_corpora
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_actual_api_key_here
   ```

5. **Run the application**
   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access the API**
   - API: http://localhost:8000
   - Interactive Docs: http://localhost:8000/docs
   - Alternative Docs: http://localhost:8000/redoc

### Option 2: Docker Deployment

1. **Get OpenRouter API Key**
   - Sign up at [openrouter.ai](https://openrouter.ai)
   - Get your free API key

2. **Create .env file**
   ```bash
   echo "OPENROUTER_API_KEY=your_api_key_here" > .env
   ```

3. **Build Docker image**
   ```bash
   docker build -t text-analyzer .
   ```

4. **Run Docker container**
   ```bash
   docker run -p 8000:8000 --env-file .env text-analyzer
   ```

5. **Access the API**
   - API: http://localhost:8000
   - Docs: http://localhost:8000/docs

## 📖 API Usage

### Analyze Text Endpoint

**POST** `/analyze`

**Request Body:**
```json
{
  "text": "I absolutely love this product! It exceeded my expectations."
}
```

**Response:**
```json
{
  "sentiment": {
    "label": "positive",
    "polarity": 0.65,
    "subjectivity": 0.85
  },
  "summary": "The user expresses strong positive feelings about a product that surpassed their expectations.",
  "original_length": 58
}
```

### Health Check

**GET** `/health`

**Response:**
```json
{
  "status": "healthy",
  "service": "ai-text-analyzer"
}
```

## 🧪 Testing with cURL

```bash
# Analyze positive text
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"text": "This is amazing! I love it!"}'

# Analyze negative text
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{"text": "This is terrible. Very disappointed."}'

# Health check
curl http://localhost:8000/health
```

## 📁 Project Structure

```
ai-text-analyzer/
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI application
│   ├── sentiment.py      # Sentiment analysis module
│   └── llm_service.py    # LLM API integration
├── tests/                # Test files (future)
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🔧 Configuration

Environment variables:

- `OPENROUTER_API_KEY`: Your OpenRouter API key (required)
- `OPENROUTER_MODEL`: LLM model to use (default: `meta-llama/llama-3.2-3b-instruct:free`)
