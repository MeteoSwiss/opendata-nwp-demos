import logging
import sys
from pathlib import Path
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError
import nbformat

logger = logging.getLogger(__name__)

KERNEL_NAME = "notebooks-nwp-env"
ROOT_DIR = Path(__file__).resolve().parent
NOTEBOOK_DIRS = [ROOT_DIR, ROOT_DIR / "developer_notebooks"]


def run_notebook(notebook_path: Path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)

    # configure the notebook execution mode
    ep = ExecutePreprocessor(timeout=600, kernel_name=KERNEL_NAME)

    try:
        # run the notebook
        ep.preprocess(nb, {'metadata': {'path': notebook_path.parent}})
        logger.info(f"Notebook ran successfully: {notebook_path}")
    except CellExecutionError as e:
        logger.exception(f"Error in notebook: {notebook_path}")
        raise

def main():
    had_errors = False
    failed_notebooks = []

    for directory in NOTEBOOK_DIRS:
        for nb_path in directory.glob("*.ipynb"):
            try:
                run_notebook(nb_path)
            except Exception:
                had_errors = True
                failed_notebooks.append(nb_path)

    if had_errors:
        failed_notebooks_str = "\n".join(f"  - {nb_path}" for nb_path in failed_notebooks)
        logger.error(f"The following notebooks failed:\n{failed_notebooks_str}")
        sys.exit(1)
    else:
        logger.info("All notebooks ran successfully.")

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

    main()

