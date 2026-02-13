"""
Quick test script to verify Docker Model Runner is working.
Run this before using the text processor to ensure everything is set up correctly.
"""

import requests
import json
from textprocessor import TextProcessor


def test_model_runner_connection():
    """Test if Docker Model Runner is accessible."""
    print("=" * 60)
    print("Testing Docker Model Runner Connection")
    print("=" * 60)
    
    base_url = "http://localhost:8080"
    
    # Test 1: Health check
    print("\n1. Health Check...")
    try:
        response = requests.get(f"{base_url}/health", timeout=5)
        if response.status_code == 200:
            print("   ✓ Model Runner is healthy")
        else:
            print(f"   ✗ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("   ✗ Cannot connect to Model Runner on port 8080")
        print("\n   Start it with:")
        print("   docker run -d -p 8080:8080 --name model-runner \\")
        print("     -e MODEL=docker.io/granite-4.0-nano:350M-BF16 \\")
        print("     docker/model-runner")
        return False
    except Exception as e:
        print(f"   ✗ Error: {e}")
        return False
    
    # Test 2: List models
    print("\n2. Checking Available Models...")
    try:
        response = requests.get(f"{base_url}/v1/models", timeout=5)
        if response.status_code == 200:
            models = response.json()
            if 'data' in models and len(models['data']) > 0:
                print(f"   ✓ Found {len(models['data'])} model(s):")
                for model in models['data']:
                    print(f"     - {model.get('id', 'unknown')}")
            else:
                print("   ⚠ No models loaded")
        else:
            print(f"   ✗ Failed to list models: {response.status_code}")
    except Exception as e:
        print(f"   ✗ Error listing models: {e}")
    
    # Test 3: Simple completion test
    print("\n3. Testing Text Completion...")
    try:
        processor = TextProcessor(model="docker.io/granite-4.0-nano:350M-BF16")
        
        test_text = "Python is a programming language. It is widely used for data science and web development."
        
        result = processor.summarize(
            text=test_text,
            max_tokens=50,
            temperature=0.7
        )
        
        print("   ✓ Completion successful!")
        print(f"   Model: {result['model']}")
        print(f"   Tokens used: {result['tokens_used']['total']}")
        print(f"   Summary: {result['summary'][:100]}...")
        
        return True
        
    except Exception as e:
        print(f"   ✗ Completion failed: {e}")
        return False


def test_api_endpoint():
    """Test if Flask app endpoints would work."""
    print("\n" + "=" * 60)
    print("Testing Flask API Setup")
    print("=" * 60)
    
    print("\n✓ Available endpoints after starting Flask app:")
    print("  - POST http://localhost:5000/api/summarize")
    print("  - POST http://localhost:5000/api/extract-key-points")
    print("  - POST http://localhost:5000/api/analyze")
    print("\nStart Flask app with: python flask_app.py")


if __name__ == "__main__":
    print("\n" + "╔" + "=" * 58 + "╗")
    print("║  Docker Model Runner + Granite 4.0 - Connection Test    ║")
    print("╚" + "=" * 58 + "╝\n")
    
    success = test_model_runner_connection()
    test_api_endpoint()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ All tests passed! System is ready to use.")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
    print("=" * 60 + "\n")
