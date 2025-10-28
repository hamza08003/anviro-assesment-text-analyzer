from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict
import logging

from app.sentiment import analyze_sentiment
from app.llm_service import LLMService

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="AI Text Analyzer",
    description="Analyze text sentiment and generate summaries using AI",
    version="1.0.0"
)

llm_service = LLMService()

class TextInput(BaseModel):
    text: str = Field(..., min_length=1, max_length=5000, description="Text to analyze")


class AnalysisResponse(BaseModel):
    sentiment: Dict[str, any]
    summary: str
    original_length: int


@app.get("/")
async def root():
    return {
        "message": "AI Text Analyzer API",
        "version": "1.0.0",
        "endpoints": {
            "analyze": "/analyze (POST)",
            "health": "/health (GET)",
            "docs": "/docs"
        }
    }


@app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "ai-text-analyzer"
    }

@app.post("/analyze", response_model=AnalysisResponse)
async def analyze_text(input_data: TextInput):
    try:
        text = input_data.text.strip()
        
        if not text:
            raise HTTPException(status_code=400, detail="Text cannot be empty")
        
        logger.info(f"Analyzing text of length: {len(text)}")
        
        sentiment_result = analyze_sentiment(text)
        logger.info(f"Sentiment: {sentiment_result['label']}")

        summary = await llm_service.summarize_text(text)
        logger.info("Summary generated")
        
        return AnalysisResponse(
            sentiment=sentiment_result,
            summary=summary,
            original_length=len(text)
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error during analysis: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    