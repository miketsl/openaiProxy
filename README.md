# openaiProxy
The intent of this project is to create a drop in replacement of the OpenAI api, so that all the tooling that currently uses OpenAI will work seamlessly.
The proxy will then add additional use cases and features that are not currently implemented in OpenAI.  For example:
  - Use packages like EdgeGPT to allow the use of Bing Chat instead of OpenAI
  - Store OpenAI api keys and manage budgets vs time.  For example, only allow $20 per day on key xyz
  - Proxy to other foundational LLM services like Cohere, Claude, HuggingFace etc

This project is in Python because most of the interesting projects seem to be written in Python atm.
