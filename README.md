![favicon](https://github.com/NighthawkCode/open-webui/assets/81494065/181f8eb0-2a71-4527-8d9f-d92ecbdf5d5b)
# Nighthawk AI


Nighthawk AI is an intelligent assistant designed to streamline agricultural operations by providing automated dispatch and information retrieval capabilities.

## Tech Stack

- **Frontend**: Svelte
- **Backend**: FastAPI
- **Deployment**: Docker container on Heroku

## Prerequisites

- Docker installed on your local machine
- Heroku CLI installed and configured

## Setup and Deployment

### Local Setup

1. **Clone and navigate to the repository**:
   ```bash
   git clone https://github.com/NighthawkCode/open-webui.git
   cd open-webui

2. **Build the custom Docker image**
   ```docker build -t open-webui-custom .

3. **Run the container locally**
   ```docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui-custom --restart always open-webui-custom