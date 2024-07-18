# File Upload Server

This repository contains a basic file upload server built with Node.js. The server allows users to upload files through an HTML form, and the files are then saved to the server's filesystem.

## Features

- **File Upload**: Users can upload files using an HTML form.
- **Form Display**: A simple HTML form is served to the user for file uploads.
- **Multipart Handling**: The server handles multipart form data to extract and save the uploaded files.

## Requirements

- Node.js (version 12 or higher)

## Installation

1. Clone this specific directory only:
    ```bash
    git clone --no-checkout https://github.com/nilumahato/Computer-Network.git
   cd Computer-Network
   git sparse-checkout init --cone
   git sparse-checkout set FileUploadWebServer
   git checkout main
   ```

2. Install the dependencies:
    ```bash
    npm install
    ```

## Usage

1. Start the server:
    ```bash
    node index.js
    ```
2. Open your web browser and go to:
    ```
    http://localhost:3000
    ```
3. Upload a file using the form provided.

## Code Overview

### Server Setup

The server is created using the `http` module and listens on port 3000:

```javascript
const server = http.createServer((req, res) => {
    if (req.url == '/upload' && req.method == 'POST') {
        handleFileUpload(req, res);
    }
    else if (req.url == '/' && req.method == 'GET') {
        showUploadForm(res);
    }
    else {
        res.statusCode = 404;
        res.end('Page Not Found');
    }
});

server.listen(3000, () => {
    console.log('Server is running on port 3000');
    console.log('http://localhost:3000');
});
