# API Documentation

## Overview

This documentation provides details on how to interact with the Sentiment Analysis API. The API allows users to input text and receive a sentiment prediction based on a trained machine learning model.

## Endpoints

### 1. `/predict`

- **Description:** This endpoint accepts a piece of text and returns the predicted sentiment.
- **Method:** POST
- **URL:** `http://localhost:5000/predict`

#### Request:

- **Content-Type:** `application/json`
- **Body:**
  ```json
  {
    "text": "I love this movie!"
  }
  ```
