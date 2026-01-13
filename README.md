# InsightCoder: GenAI-Powered Market Research Pipeline

**InsightCoder** is basically an automated tool built to tackle the challenges of Qualitative Data Analysis (QDA) in Market Research Operations (MROps). It takes a ton of unstructured responses from open-ended surveys and turns them into clear, actionable insights for businesses, using Unsupervised Learning and Generative AI..


## 🚀 Key Features

*   **NLP Preprocessing:** This includes automatically getting rid of noise, breaking text into tokens, and filtering out stopwords.

*   **Sentiment Analysis:** We use a rule-based approach with TextBlob to score polarity.

*   **Unsupervised Topic Modeling:** It employs TF-IDF Vectorization and K-Means Clustering to uncover hidden themes without needing any human input.

*   **GenAI Labeling:** It connects with **Google Gemini 2.0** Flash to analyze keywords from clusters and produce professional semantic labels for each topic.

## 🛠️ Tech Stack
*   **Language:** Python 3.9+
*   **AI & ML:** Scikit-Learn (K-Means, TF-IDF), TextBlob
*   **Generative AI:** Google GenAI SDK (Gemini 2.0 Flash)
*   **Data Engineering:** Pandas, NumPy
*   **Environment:** Virtual Environment (venv), DotEnv security

## ⚙️ How It Works
1.  **Ingestion:** Loads raw survey CSV data.
2.  **Cleaning:** Regex-based cleaning pipeline removes punctuation and standardizes text.
3.  **Clustering:** The system groups reviews into clusters based on mathematical similarity (TF-IDF).
4.  **Labeling:** The top keywords from each cluster are sent to the LLM (Gemini), which acts as a "Market Research Analyst" to assign a business-context label.
5.  **Output:** Generates a `final_market_report.csv` ready for dashboard visualization.

## 📈 Example Output
| Customer Feedback | Sentiment | AI-Generated Topic |
| :--- | :--- | :--- |
| "Battery life is amazing!" | Positive | Battery Performance |
| "Too expensive for the features" | Negative | Value Perception Conflict |
| "App crashes constantly" | Negative | App Stability Issues |

---
*Built by Fahad Anwar as a prototype for Automated MROps workflows.*