# **Intelligent Financial Reporting Agent**

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Microsoft Fabric](https://img.shields.io/badge/Microsoft-Fabric-purple)
![Azure](https://img.shields.io/badge/Cloud-Azure-lightblue)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![Vanna AI](https://img.shields.io/badge/VannaAI-Text--to--SQL-orange)
![RAG](https://img.shields.io/badge/Model-RAG--GPT4-red)
![License](https://img.shields.io/badge/License-Educational-yellow)

---

## 🧭 Overview
This project demonstrates an **end-to-end Wealth Asset Management platform** powered by **Microsoft Fabric Lakehouse** and **LangChain-based Text-to-SQL models**.  
It provides a structured, scalable data architecture for managing **client portfolios, assets, transactions**, and **risk assessments**, while enabling natural-language querying of financial data.

The workflow involves:
- Setting up Microsoft Fabric Lakehouse  
- Inserting 1 GB of dummy financial data  
- Running a Text-to-SQL model for query generation  
- Integrating LangChain for context-aware query refinement  

---

## 🏗️ Microsoft Fabric Lakehouse
**Microsoft Fabric Lakehouse** acts as the cloud data foundation for storing and managing portfolio-related datasets.  
It unifies data ingestion, transformation, and querying, enabling secure and real-time analytics.

Steps include:
1. Define schema — tables, views, stored procedures  
2. Load dummy data using Python (Faker & PyODBC)  
3. Query and visualize through LangChain and Vanna AI  

---

## 🧩 Text-to-SQL Model
The **Text-to-SQL Model** enables users to query the Lakehouse via natural language inputs.  
It automatically generates SQL statements for financial operations such as:
- Portfolio valuations  
- Asset distribution analysis  
- Transaction retrieval  
- Risk summaries  

**Model Scripts**
- Training: `RAGToSQL/TrainRAG.py`  
- Inference: `RAGToSQL/InferenceRAG.py`  
- Fabrics Integration: `RAGToSQL/FabricsRAG.py`

---

## 🧠 LangChain Integration
LangChain enhances the AI layer by providing:
- **Context memory** for multi-turn financial queries  
- **Dynamic prompt chaining** for follow-up analysis  
- **Integration with Vanna AI** for Text-to-SQL translation  

**File:** `LangchainFabrics/LangChainFabrics.py`

---

## 💾 Data Insertion
Before running the models, populate the Fabric Lakehouse with synthetic data.

```bash
python CreateDataWarehouse/insertToSQL.py
```
> Ensure the connection string and drivers are configured in the script.

---

## 📂 Project Structure
```bash
Code
├─ CreateDataWarehouse
│  ├─ InsertToSQL.py
│  └─ SQL
│     ├─ create_tables.sql
│     ├─ create_views_sql.sql
│     ├─ stored_procedures.sql
│     ├─ Proc.json
│     ├─ Tables.json
│     └─ Views.json
│
├─ LangchainFabrics
│  ├─ LangChainFabrics.py
│  └─ TestConnectionFabrics.py
│
├─ RAGToSQL
│  ├─ chroma.sqlite3
│  ├─ FabricsRAG.py
│  ├─ Helper
│  │  ├─ Credentials.py
│  │  ├─ FabricsConnection.py
│  │  ├─ VannaObject.py
│  │  └─ __init__.py
│  ├─ InferenceRAG.py
│  ├─ TrainRAG.py
│  ├─ VisualizeRAG.py
│  └─ TrainingRAG-Artifact
│     ├─ Documentation.txt
│     ├─ Proc.json
│     ├─ Tables.json
│     ├─ Views.json
│     └─ training_summary.csv
│
├─ architecture_diagram.png
├─ requirements.txt
└─ Readme.md
```

---

## ⚙️ Prerequisites
- **Python 3.9**  
- **Microsoft Fabric Lakehouse access**  
- **Azure account (for Fabric)**  
- **Libraries:** `pandas`, `numpy`, `pyodbc`, `faker`, `langchain`, `openai`, `vanna-ai`

Install dependencies:
```bash
pip install -r requirements.txt
```

---

## 🧰 Environment Setup

### 🪟 Windows
```bash
cd C:\path\to\project
python -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```

### 💻 Linux / macOS
```bash
cd /path/to/project
python3.9 -m venv myenv
source myenv/bin/activate
pip install -r requirements.txt
```

If multiple Python versions exist:
```bash
py -3.9 -m venv myenv
myenv\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Execution Steps

### 1️⃣ Data Load
```bash
python CreateDataWarehouse/insertToSQL.py
```

### 2️⃣ Train Text-to-SQL Model
```bash
python RAGToSQL/TrainRAG.py
```

### 3️⃣ Run Inference on Queries
```bash
python RAGToSQL/InferenceRAG.py
```

### 4️⃣ Integrate LangChain Fabrics
```bash
python LangchainFabrics/LangChainFabrics.py
```

---

## 🧱 Architecture Diagram
![Architecture Diagram](architecture_diagram.png)

**Key Components**
1. Microsoft Fabric Lakehouse (OneLake + Warehouse)  
2. Dataflow Gen2 for data ingestion  
3. Text-to-SQL via Vanna AI  
4. LangChain for context memory & prompt reasoning  
5. Azure integration for scalable data pipelines  

---

## 🧪 Project Takeaways
- Understand Microsoft Fabric’s **Lakehouse & OneLake ecosystem**  
- Learn **RAG integration with financial datasets**  
- Implement **Text-to-SQL query generation using LLMs**  
- Connect **Python scripts to Fabric SQL endpoints**  
- Design and visualize insights with Vanna AI  
- Build end-to-end financial data pipelines for real-time decision support  

---

## 💰 Cost Breakdown (Estimates)
| Component | Description | Estimated Cost |
|------------|-------------|----------------|
| Azure Fabric Storage | 100 GB data storage – trial free (60 days) | Free / $2.30 after trial |
| Azure Compute | Pay-as-you-go (F2 SKU – 2 CUs) | ~$262 / month |
| GPT-4 API Calls (Vanna AI Text-to-SQL) | 200 K tokens | ~$1.50 per 100 queries |
| Azure SQL Storage | 50 GB | ~$5 |
| Misc. Fabric Resources | Dataflow Gen2, Lakehouse usage | Trial included |

> 💡 Use the free Microsoft Fabric trial (60 days) for exploration and testing.

---

## 🧠 Project Learnings
- Microsoft Fabric data architecture design  
- Azure OneLake warehouse management  
- LangChain contextual reasoning pipeline  
- Text-to-SQL automation with Vanna AI  
- End-to-end RAG implementation on structured financial data  

---

## 🔗 References
- [Microsoft Fabric Documentation](https://learn.microsoft.com/fabric)
- [Azure Pricing Calculator](https://azure.microsoft.com/pricing)
- [Vanna AI Text-to-SQL](https://vanna.ai/)
- [LangChain Docs](https://python.langchain.com/)
- [OpenAI Pricing](https://openai.com/pricing)
