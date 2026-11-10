# AI Tools Usage Analytics Project

## Project files
- `AI_Tools_Usage_Dashboard_Dataset.xlsx` - original dataset.
- `Project_Proposal.md` - project proposal.
- `data_cleaning.py` - cleans the Excel data and creates `clean_dataset.csv`.
- `clean_dataset.csv` - cleaned dataset (generated).
- `Data_analysis.py` - creates statistics, correlation matrix, and summary files.
- `Data_visualisation.py` - creates PNG charts in the `charts` folder.
- `outputs/` - analysis outputs.
- `charts/` - generated charts.
- `PowerBI_Dashboard_Guide.md` - steps to create and save the PBIX file.

## Run in VS Code
1. Install Python 3 and open this folder in VS Code.
2. Open Terminal > New Terminal.
3. Run: `python -m pip install -r requirements.txt`
4. Run: `python data_cleaning.py`
5. Run: `python Data_analysis.py`
6. Run: `python Data_visualisation.py`

If the `python` command is not recognised on Windows, try `py` instead.

## Power BI file
A `.pbix` is a native Power BI Desktop project file. It must be created and saved in Power BI Desktop. Follow `PowerBI_Dashboard_Guide.md`, then save the file in this project folder as `Dashboard.pbix`.
