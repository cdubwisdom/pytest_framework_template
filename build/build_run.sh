conda init bash
conda env create --name RUN_ENV --file ../pytest_env.yml -q
conda activate RUN_ENV
python run.py
conda deactivate
