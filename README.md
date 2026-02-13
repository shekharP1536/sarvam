# Document Converter with AI Summarization

A Flask-based document converter that uses Docling for document processing and Docker Model Runner with Granite 4.0 Nano model for intelligent text summarization and analysis.

## Features

- **Document Conversion**: Convert PDF, DOCX, HTML, PPTX, images, and more to Markdown, JSON, or YAML
- **AI Summarization**: Generate concise summaries of converted documents using local Granite model
- **Key Points Extraction**: Extract main points from documents automatically
- **Custom Analysis**: Perform custom AI-powered text analysis with user-defined instructions
- **Batch Processing**: Convert multiple documents at once
- **OCR Support**: Extract text from images and scanned documents
- **Local Model**: Uses Docker Model Runner for privacy and no API costs

## Prerequisites

- Python 3.8+
- Docker Desktop with AI features enabled
- Docker Model Runner

## Installation

1. **Start Docker Model Runner with Granite model:**
   ```powershell
   docker run -d -p 8080:8080 --name model-runner `
     -e MODEL=docker.io/granite-4.0-nano:350M-BF16 `
     docker/model-runner
   ```

2. **Install Python dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **(Optional) Set custom Model Runner URL:**
   ```powershell
   $env:MODEL_RUNNER_URL="http://localhost:8080/v1"
   ```

## Usage

### Starting the Flask Server

```powershell
python flask_app.py
```

The server will start on `http://localhost:5000`

### API Endpoints

#### 1. Document Conversion
```bash
POST /api/convert
```
Convert a document to markdown, JSON, or YAML.

**Form Data:**
- `file` - Document file (required)
- `output_format` - markdown/json/yaml (default: markdown)
- `use_ocr` - true/false (default: true)

**Example:**
```powershell
curl -X POST http://localhost:5000/api/convert `
  -F "file=@document.pdf" `
  -F "output_format=markdown"
```

#### 2. Document Summarization
```bash
POST /api/summarize
```
Convert a document and generate an AI summary.

**Form Data:**
- `file` - Document file (required)
- `use_ocr` - true/false (default: true)
- `max_tokens` - Maximum tokens for summary (default: 500)
- `temperature` - 0-2, sampling temperature (default: 0.7)

**Example:**
```powershell
curl -X POST http://localhost:5000/api/summarize `
  -F "file=@document.pdf" `
  -F "max_tokens=500" `
  -F "temperature=0.7"
```

**Response:**
```json
{
  "filename": "document.pdf",
  "text_content": "Full converted text...",
  "summary": "AI-generated summary...",
  "metadata": {
    "model": "gpt-4o-mini",
    "tokens_used": {
      "prompt": 1234,
      "completion": 456,
      "total": 1690
    },
    "finish_reason": "stop"
  },
  "success": true
}
```

#### 3. Extract Key Points
```bash
POST /api/extract-key-points
```
Convert a document and extract key points.

**Form Data:**
- `file` - Document file (required)
- `use_ocr` - true/false (default: true)
- `num_points` - Number of key points (default: 5)

**Example:**
```powershell
curl -X POST http://localhost:5000/api/extract-key-points `
  -F "file=@document.pdf" `
  -F "num_points=5"
```

#### 4. Custom Analysis
```bash
POST /api/analyze
```
Convert a document and perform custom AI analysis.

**Form Data:**
- `file` - Document file (required)
- `instruction` - Analysis instruction (required)
- `use_ocr` - true/false (default: true)
- `max_tokens` - Maximum tokens (default: 1000)

**Example:**
```powershell
curl -X POST http://localhost:5000/api/analyze `
  -F "file=@document.pdf" `
  -F "instruction=Identify the main risks mentioned in this document"
```

#### 5. Batch Conversion
```bash
POST /api/convert/batch
```
Convert multiple documents at once.

**Form Data:**
- `files[]` - Multiple document files (required)
- `output_format` - markdown/json/yaml (default: markdown)
- `use_ocr` - true/false (default: true)

### Using the TextProcessor Class Directly

```python
from textprocessor import TextProcessor

# Initialize with Docker Model Runner (default)
processor = TextProcessor(model="docker.io/granite-4.0-nano:350M-BF16")

# Or use with custom base URL
processor = TextProcessor(
    model="docker.io/granite-4.0-nano:350M-BF16",
    base_url="http://localhost:8080/v1"
)

# Summarize text
result = processor.summarize(
    text="Your long text here...",
    max_tokens=500,
    temperature=0.7
)
print(result["summary"])

# Extract key points
points = processor.extract_key_points(
    text="Your text here...",
    num_points=5
)
print(points["key_points"])

# Custom analysis
analysis = processor.custom_analysis(
    text="Your text here...",
    instruction="Identify the main themes"
)
print(analysis["result"])
```

### Quick Summarization

```python
from textprocessor import quick_summarize

summary = quick_summarize("Your text here...")
print(summary)
```

## Running Examples

```powershell
python example_usage.py
```

This will demonstrate:
1. Direct text summarization
2. Key points extraction
3. Custom analysis
4. Quick summarize function
5. API usage examples

## Supported File Types

- PDF (`.pdf`)
- Word Documents (`.docx`)
- HTML (`.html`, `.htm`)
- PowerPoint (`.pptx`)
- Images (`.png`, `.jpg`, `.jpeg`)
- AsciiDoc (`.asciidoc`)
- Markdown (`.API key (default: "not-needed" for Docker Model Runner)
- `model` - Model name (default: "docker.io/granite-4.0-nano:350M-BF16")
- `base_url` - API base URL (default: "http://localhost:8080/v1")

**Available Models via Docker Model Runner:**
- `docker.io/granite-4.0-nano:350M-BF16` - Fast, lightweight (350M parameters)
- `docker.io/granite-4.0-mini:1.2B` - Better quality (1.2B parameters)
- Other Granite or compatible models

**For OpenAI API (alternative):**
```python
processor = TextProcessor(
    api_key="your-openai-key",
    model="gpt-4o-mini",
    base_url="https://api.openai.com/v1"
)
```

### TextProcessor Options

- `api_key` - OpenAI API key (or use OPENAI_API_KEY env var)
- `model` - OpenAI model (default: "gpt-4o-mini")
  -MODEL_RUNNER_URL` - Docker Model Runner API URL (default: http://localhost:8080/v1)
- `OPENAI_API_KEY` - OpenAI API key (only if using OpenAI instead of local modelpt-3.5-turbo

### Flask App Settings

In `flask_app.py`, adjust `AppConfig`:
```python
MAX_PAGES = 100           # Maximum pages per document
MAX_FILE_SIZE = 20_971_520  # 20MB per file
UPLOAD_FOLDER = "uploads"
RESULT_FOLDER = "results"
```

## Environment Variables

- `OPENAI_API_KEY` - Your OpenAI API key (required)
nection refused` - Docker Model Runner not running on port 8080
- `Failed to generate summary` - Model error or insufficient context

## Docker Model Runner

### Starting the Model Runner

```powershell
# Start with Granite 4.0 Nano (350M)
docker run -d -p 8080:8080 --name model-runner `
  -e MODEL=docker.io/granite-4.0-nano:350M-BF16 `
  docker/model-runner

# Check status
docker ps

# View logs
docker logs model-runner

# Stop
docker stop model-runner

# Remove
docker rm model-runner
```

### Checking Model Status

```powershell
# List available models
curl httpbetter quality**: Consider using Granite 4.0 Mini (1.2B) model

## Troubleshooting

**Docker Model Runner Not Running:**
```
Connection refused on localhost:8080
```
Solution: Start Docker Model Runner:
```powershell
docker run -d -p 8080:8080 --name model-runner `
  -e MODEL=docker.io/granite-4.0-nano:350M-BF16 `
  docker/model-runner
```

**Model Loading Error:**
```
Failed to load model
```
Solution: Ensure Docker has sufficient resources (8GB+ RAM recommended)

**Import Error:**
```
ModuleNotFoundError: No module named 'openai'
```
Solution: Install dependencies:
```powershell
pip install -r requirements.txt
```

**Port Already in Use:**
```
Port 8080 is already allocated
```
Solution: Use a different port:
```powershell
docker run -d -p 8081:8080 --name model-runner `
  -e MODEL=docker.io/granite-4.0-nano:350M-BF16 `
  docker/model-runner

$env:MODEL_RUNNER_URL="http://localhost:8081/v1"
```
- No data sent to external services
- Complete privacy
}
```

Common errors:
- `No file provided` - File not included in request
- `Unsupported file type` - File extension not supported
- `Configuration error` - OpenAI API key not set or invalid
- `Failed to generate summary` - OpenAI API error

## Cost Considerations

Using OpenAI API incurs costs based on token usage:
- `gpt-4o-mini` - Most cost-effective for summarization
- `gpt-4o` - Higher quality but more expensive
- Monitor your token usage via the response metadata

## Tips

1. **For long documents**: Set higher `max_tokens` values
2. **For factual summaries**: Use lower `temperature` (0.3-0.5)
3. **For creative analysis**: Use higher `temperature` (0.7-1.0)
4. **For scanned documents**: Enable `use_ocr=true`
5. **For faster processing**: Use `gpt-4o-mini` model

## Troubleshooting

**OpenAI API Key Error:**
```
ValueError: OpenAI API key is required
```
Solution: Set the environment variable:
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
```

**Import Error:**
```
ModuleNotFoundError: No module named 'openai'
```
Solution: Install dependencies:
```powershell
pip install -r requirements.txt
```

**Connection Error:**
Ensure you have internet connectivity for OpenAI API calls.

## License

MIT License

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.
