![favicon](https://github.com/NighthawkCode/open-webui/assets/81494065/181f8eb0-2a71-4527-8d9f-d92ecbdf5d5b)
# Nighthawk AI Staging

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
   ```bash
   docker build -t open-webui-custom .

3. **Run the container locally with GPU support**
   ```bash
   docker run -d -p 3000:8080 --gpus=all -v ollama:/root/.ollama -v open-webui:/app/backend/data --name open-webui-custom --restart always open-webui-custom

4. **View the local app**
   ```bash
   http://localhost:3000/

### Deploying Changes

When you are ready to test your changes on a deployment, follow these steps.

1. **Request Access to Nighthawk Staging on Heroku**
   - Reach out to ```radinubilo@gmail.com``` to get elevated permissions on the Heroku staging server

2. **Download the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)**
   ```bash
   curl https://cli-assets.heroku.com/install.sh | sh

3. **Login to the Heroku CLI**
   ```bash
   heroku login

4. **Build and Deploy the updated Docker image**
   ```
   heroku container:login
   heroku container:push web --app nighthawkui-v1
   heroku container:release web --app nighthawkui-v1