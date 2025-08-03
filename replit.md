# Overview

This is a Korean acrostic poem generator built with Streamlit and powered by Google's Gemini AI. The application allows users to input Korean words and generates N-line acrostic poems (삼행시, 사행시, etc.) where each line starts with the consecutive characters of the input word. The poems are designed to be meaningful, connected, and use beautiful poetic expressions in Korean.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
- **Streamlit Web Framework**: Single-page application using Streamlit for the user interface
- **Caching Strategy**: Uses `@st.cache_resource` decorator for efficient client initialization and resource management
- **Error Handling**: Built-in error display using Streamlit's error messaging system

## Backend Architecture
- **Google Gemini Integration**: Uses the Google Generai SDK to interact with Gemini 2.5 Flash model
- **API Client Management**: Cached client initialization to avoid repeated API authentication
- **Prompt Engineering**: Structured Korean language prompts with specific formatting rules for acrostic poem generation

## Configuration Management
- **Environment Variables**: API key management through `GEMINI_API_KEY` environment variable
- **Security**: API keys stored as environment variables rather than hardcoded values

## Language Processing
- **Korean Language Support**: Specialized for Korean acrostic poems (N행시)
- **Character-based Generation**: Each character of the input word becomes the starting character for poem lines
- **Formatting Rules**: Structured output format with consistent Korean poetic conventions

# External Dependencies

## AI Services
- **Google Gemini API**: Primary AI service for poem generation using the Gemini 2.5 Flash model
- **Google Generai SDK**: Python client library for Gemini API integration

## Web Framework
- **Streamlit**: Core web application framework for UI and user interaction

## Python Environment
- **Environment Variables**: System environment for secure API key storage
- **Standard Libraries**: Built-in `os` module for environment variable access