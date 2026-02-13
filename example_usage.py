"""
Example usage of TextProcessor for document summarization with Docker Model Runner.

Before running:
1. Install requirements: pip install -r requirements.txt
2. Start Docker Model Runner with Granite model:
   docker run -d -p 8080:8080 --name model-runner \
     -e MODEL=docker.io/granite-4.0-nano:350M-BF16 \
     docker/model-runner
3. (Optional) Set custom base URL: $env:MODEL_RUNNER_URL="http://localhost:8080/v1"
"""

import requests
from textprocessor import TextProcessor, quick_summarize


def example_direct_usage():
    """Example: Using TextProcessor directly with text."""
    
    # Sample text to summarize
    sample_text = """
    Artificial Intelligence (AI) has transformed numerous industries over the past decade. 
    Machine learning algorithms now power everything from recommendation systems to autonomous 
    vehicles. Deep learning, a subset of machine learning, has been particularly successful 
    in image recognition, natural language processing, and game playing. The field continues 
    to evolve rapidly with new architectures and techniques being developed regularly. 
    However, challenges remain in areas such as explainability, bias, and energy consumption.
    """
    
    print("=" * 60)
    print("Example 1: Direct Text Summarization")
    print("=" * 60)
    
    # Initialize processor with Docker Model Runner
    processor = TextProcessor(model="docker.io/granite-4.0-nano:350M-BF16")
    
    # Generate summary
    result = processor.summarize(
        text=sample_text,
        max_tokens=100,
        temperature=0.7
    )
    
    print(f"\nOriginal Text Length: {len(sample_text)} characters")
    print(f"\nSummary:\n{result['summary']}")
    print(f"\nModel: {result['model']}")
    print(f"Tokens Used: {result['tokens_used']['total']}")
    print()


def example_key_points():
    """Example: Extract key points from text."""
    
    sample_text = """
    Climate change is one of the most pressing challenges of our time. Rising global 
    temperatures are causing ice caps to melt, sea levels to rise, and weather patterns 
    to become more extreme. The primary cause is greenhouse gas emissions from human 
    activities, particularly the burning of fossil fuels. Solutions include transitioning 
    to renewable energy sources, improving energy efficiency, and implementing carbon 
    capture technologies. International cooperation through agreements like the Paris 
    Climate Accord is essential for addressing this global issue.
    """
    
    print("=" * 60)
    print("Example 2: Extract Key Points")
    print("=" * 60)
    
    processor = TextProcessor(model="docker.io/granite-4.0-nano:350M-BF16")
    
    result = processor.extract_key_points(
        text=sample_text,
        num_points=4
    )
    
    print(f"\nKey Points:\n{result['key_points']}")
    print(f"\nTokens Used: {result['tokens_used']['total']}")
    print()


def example_custom_analysis():
    """Example: Custom text analysis."""
    
    sample_text = """
    The company's Q4 revenue increased by 23% year-over-year to $5.2 billion. 
    Net income rose to $890 million, up from $720 million in the same quarter last year. 
    The cloud computing division was the primary growth driver, contributing 45% of 
    total revenue. Operating expenses increased by 18%, mainly due to increased R&D 
    spending on AI initiatives. The company announced plans to hire 1,000 additional 
    engineers in the coming year.
    """
    
    print("=" * 60)
    print("Example 3: Custom Analysis")
    print("=" * 60)
    
    processor = TextProcessor(model="docker.io/granite-4.0-nano:350M-BF16")
    
    result = processor.custom_analysis(
        text=sample_text,
        instruction="Identify the positive and negative financial indicators in this text.",
        max_tokens=300
    )
    
    print(f"\nAnalysis:\n{result['result']}")
    print(f"\nTokens Used: {result['tokens_used']['total']}")
    print()


def example_quick_summarize():
    """Example: Quick summarization using convenience function."""
    
    sample_text = """
    Quantum computing leverages quantum mechanical phenomena to process information. 
    Unlike classical bits that are either 0 or 1, quantum bits (qubits) can exist 
    in superposition states. This enables quantum computers to solve certain problems 
    exponentially faster than classical computers.
    """
    
    print("=" * 60)
    print("Example 4: Quick Summarize Function")
    print("=" * 60)
    
    summary = quick_summarize(sample_text)
    print(f"\nQuick Summary:\n{summary}")
    print()


def example_api_usage():
    """Example: Using the Flask API endpoints."""
    
    print("=" * 60)
    print("Example 5: API Usage")
    print("=" * 60)
    print("\nAPI Endpoints Available:")
    print()
    
    print("1. Summarize Document:")
    print("   POST http://localhost:5000/api/summarize")
    print("   Form Data:")
    print("     - file: (document file)")
    print("     - use_ocr: true/false (optional)")
    print("     - max_tokens: integer (optional)")
    print("     - temperature: 0-2 (optional)")
    print()
    
    print("2. Extract Key Points:")
    print("   POST http://localhost:5000/api/extract-key-points")
    print("   Form Data:")
    print("     - file: (document file)")
    print("     - use_ocr: true/false (optional)")
    print("     - num_points: integer (optional)")
    print()
    
    print("3. Custom Analysis:")
    print("   POST http://localhost:5000/api/analyze")
    print("   Form Data:")
    print("     - file: (document file)")
    print("     - instruction: (your analysis instruction)")
    print("     - use_ocr: true/false (optional)")
    print("     - max_tokens: integer (optional)")
    print()
    
    print("Example cURL command:")
    print('curl -X POST http://localhost:5000/api/summarize \\')
    print('  -F "file=@document.pdf" \\')
    print('  -F "max_tokens=500" \\')
    print('  -F "temperature=0.7"')
    print()


if __name__ == "__main__":
    import os
    
    # Check if Docker Model Runner is likely running
    print("\n╔════════════════════════════════════════════════════════════╗")
    print("║  Docker Model Runner - Granite 4.0 Nano Model             ║")
    print("╚════════════════════════════════════════════════════════════╝\n")
    
    model_runner_url = os.getenv("MODEL_RUNNER_URL", "http://localhost:8080/v1")
    print(f"Expected Model Runner URL: {model_runner_url}")
    print(f"Model: docker.io/granite-4.0-nano:350M-BF16\n")
    
    if True:  # Always try to run examples with Docker Model Runner
        print("✓ Running examples with Docker Model Runner...\n")
        
        try:
            example_direct_usage()
            example_key_points()
            example_custom_analysis()
            example_quick_summarize()
            example_api_usage()
            
            print("=" * 60)
            print("All examples completed successfully!")
            print("=" * 60)
        except ExceptiDocker Model Runner is running on port 8080")
            print("2. Granite model is loaded in Docker Model Runner")
            print("3. All dependencies are installed")
            print("\nTo start Docker Model Runner:")
            print("docker run -d -p 8080:8080 --name model-runner \\")
            print("  -e MODEL=docker.io/granite-4.0-nano:350M-BF16 \\")
            print("  docker/model-runner
            print("1. Your OpenAI API key is valid")
            print("2. You have internet connection")
            print("3. All dependencies are installed")
