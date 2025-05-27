Requirement Document: Hackathon Use Case

Project Title:
AI-Powered Automation of Peer Bank Analysis for Quarterly Reporting
Team Owner:
Barclays – Credit Risk or Finance Insights Team
Point of Contact: [Email]
Objective:
To automate the manual end-to-end process of collecting, extracting, calculating, and presenting key peer bank metrics and commentary using publicly available earnings documents and transcripts. The goal is to streamline peer analysis, reduce manual effort, improve accuracy, and enhance insight extraction for senior stakeholders.
Scope:
Banks Covered (Initial Scope):
• JPMorgan Chase
• Bank of America
• Citibank
• Wells Fargo
• Capital One
• Synchrony
• American Express
Process Summary (Current Manual Workflow):
1. Data Collection:
  - Manually visit investor relations websites
  - Download press releases, presentations, supplement PDFs, earnings call transcripts
2. Data Extraction:
  - Extract balances, reserves, delinquency rates, NCL rates
  - Perform custom calculations, especially for Citi
3. Commentary Analysis:
  - Skim transcripts to summarize macro trends
  - Extract CEO/CFO verbatim quotes
4. Reporting & Presentation:
  - Input into Excel workbook
  - Generate charts and populate PowerPoint peer deck
Pain Points:
• Time-intensive manual download and copy-paste
• Inconsistent report formats across banks
• Derived metrics require custom formulas
• Transcripts require manual tagging of quotes
• Repetitive slide formatting
Desired Outcome (What to Automate):
• Auto-download earnings documents from IR sites
• Extract financial tables from PDFs/slides
• Automate custom metrics and calculations
• Auto-generate charts and populate Excel
• Use NLP to extract quotes and summaries from transcripts
• Generate full peer comparison tables
• Populate peer deck automatically
Suggested Technologies:
• Python for scripting
• OCR + PDF parsers (e.g., PyMuPDF, PDFPlumber)
• NLP (e.g., SpaCy, GPT-4)
• Excel/PPT automation (openpyxl, python-pptx)
• Browser automation (e.g., Selenium)
Deliverables:
• Prototype of document parsing, metric extraction, and commentary tagging
• Sample auto-populated Excel and deck
• Technical documentation
• Use case summary deck
Evaluation Metrics:
• Time saved per quarter
• Accuracy of extracted metrics
• Commentary quality
• Usability of peer deck