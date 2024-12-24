## Overview

### Agents Defined

1. **Web Agent**:
   - Purpose: Conducts web-based research using the DuckDuckGo tool.
   - Model: `Groq(id="llama-3.3-70b-versatile")`
   - Tools: DuckDuckGo for fetching relevant web information.
   - Features:
     - Includes sources in all responses.
     - Ensures the inclusion of recent and accurate data.
     - Outputs responses in Markdown format.
   
2. **Finance Agent**:
   - Purpose: Analyzes financial data, including stock prices, analyst recommendations, company info, and news.
   - Model: `Groq(id="llama-3.3-70b-versatile")`
   - Tools: YFinanceTools with features for:
     - Stock price analysis.
     - Analyst recommendations.
     - Company information and news.
   - Features:
     - Uses tables to present financial data.
     - Provides clear explanations for analyses.
     - Outputs responses in Markdown format.

3. **Agent Team**:
   - Combines Web Agent and Finance Agent to handle tasks requiring both web research and financial analysis.
   - Features:
     - Adheres to shared instructions for consistency.
     - Displays results in Markdown format with sources and tables where appropriate.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the root directory.
   - Add any required API keys or configurations. For example:
     ```env
     GROQ_API_KEY<your_api_key>
     OPENAI_API_KEY=<your_api_key>
     ```

## Usage

### Finance Agent
To summarize financial data such as the top 20 best stocks to buy in India for 2025 with growth predictions, use the `finance_agent`:

```python
finance_agent.print_response("Summarize the top 20 best stocks to buy in India for 2025, including percentage growth predictions.")
```

#### Expected Output
- A Markdown-formatted table listing:
  - Stock names.
  - Predicted percentage growth.
  - Analyst recommendations.
- Detailed explanations of the analysis process.

### Web Agent
To perform web-based research, query the `web_agent`:

```python
web_agent.print_response("What are the current technological advancements in AI?")
```

#### Expected Output
- A detailed response including:
  - Recent advancements.
  - Sources for all information.

### Agent Team
For tasks requiring both web research and financial analysis, use the `agent_team`:

```python
agent_team.print_response("Analyze the best industries for investment in 2025 and provide a list of recommended stocks.")
```

#### Expected Output
- A comprehensive response combining:
  - Web-based research.
  - Financial data analysis.
- Includes sources and data tables.



## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch.
4. Open a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

