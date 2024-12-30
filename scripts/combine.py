import nbformat

notebooks = ["../notebooks/01_data_collection.ipynb", "../notebooks/02_data_cleaning_processing.ipynb", "../notebooks/03_data_exploration_visualization.ipynb","../notebooks/04_insights_conclusion.ipynb"]

# Create a new notebook object
merged_notebook = nbformat.v4.new_notebook()

# Merge content from each notebook
for notebook_path in notebooks:
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = nbformat.read(f, as_version=4)
        merged_notebook.cells.extend(nb.cells)

# Save the merged notebook
with open("../notebooks/full_notebook.ipynb", 'w', encoding='utf-8') as f:
    nbformat.write(merged_notebook, f)