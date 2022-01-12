echo "Run Date: $(date)" 2>&1 | tee ./run_logs/log_"$(date "+%d-%m-%y-%H%M")".out
conda init bash 2>&1 | tee ./run_logs/log_"$(date "+%d-%m-%y-%H%M")".out
if conda env list | grep ".*PYTEST_ENV.*" >/dev/null 2>&1; then
  echo "Updating Environment" 2>&1 | tee ./run_logs/log_"$(date "+%d-%m-%y-%H%M")".out
  conda env update --name PYTEST_ENV --file ../pytest_env.yml --prune -q 2>&1 | tee ./run_logs/log_"$(date "+%d-%m-%y-%H%M")".out
else
  echo "Creating Environment" 2>&1 | tee ./run_logs/log_"$(date "+%d-%m-%y-%H%M")".out
  conda env create --name PYTEST_ENV --file ../pytest_env.yml -q 2>&1 | tee ./run_logs/log_"$(date "+%d-%m-%y-%H%M")".out
fi
echo "Internalizing Environment" 2>&1 | tee ./run_logs/log_"$(date "+%d-%m-%y-%H%M")".out
conda activate PYTEST_ENV 2>&1 | tee ./run_logs/log_"$(date "+%d-%m-%y-%H%M")".out
echo "Set Up Complete" 2>&1 | tee ./run_logs/log_"$(date "+%d-%m-%y-%H%M")".out
python run.py 2>&1 | tee ./run_logs/log_"$(date "+%d-%m-%y-%H%M")".out
echo "Tearing Down Environment" 2>&1 | tee ./run_logs/log_"$(date "+%d-%m-%y-%H%M")".out
conda deactivate 2>&1 | tee ./run_logs/log_"$(date "+%d-%m-%y-%H%M")".out
