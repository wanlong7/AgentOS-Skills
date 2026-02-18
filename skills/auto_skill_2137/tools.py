{
    "stock_expert": {
        "function": "Generate investment advice and analyze stock market trends.",
        "inputs": [
            {
                "name": "stock_ticker",
                "type": "string",
                "description": "The stock ticker symbol for the company."
            },
            {
                "name": "time_period",
                "type": "string",
                "description": "The time period for which to analyze the stock trends (e.g., '1M', '6M', '1Y')."
            },
            {
                "name": "analysis_type",
                "type": "string",
                "description": "The type of analysis to perform (e.g., 'technical', 'fundamental')."
            }
        ],
        "outputs": [
            {
                "name": "advice",
                "type": "string",
                "description": "The investment advice based on the analysis."
            },
            {
                "name": "trend_analysis",
                "type": "string",
                "description": "The analysis of the stock trends."
            }
        ]
    }
}