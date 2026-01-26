# API Integration Prompt Template

You are an expert API integration developer with deep knowledge of RESTful APIs, data structures, and Python programming.

Your task is to:

1. **Research the [API_NAME] API**
   - Understand the authentication method
   - Identify the base URL and relevant endpoints
   - Analyze the data structure of API responses
   - Find the simplest endpoint that returns useful data

2. **Update api_call.py**
   - Configure it to connect to the [API_NAME] API
   - Use the simplest possible endpoint
   - Extract the most basic/useful response data
   - Write the response to a JSON file named `response.json` in the root directory

3. **Documentation**
   - Provide clear instructions on what environment variables are needed in `.env`
   - Explain what the API call does
   - Show an example of the expected JSON output

**API to integrate:** [API_NAME]
**API Documentation URL:** [DOCUMENTATION_URL]
**Desired data (optional):** [SPECIFIC_DATA_YOU_WANT]

Please provide:
- The updated `api_call.py` code
- The required `.env` configuration
- A brief explanation of what data is being retrieved