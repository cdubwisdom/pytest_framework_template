{
  echo "Run Date: $(date)"
  conda init bash
  if conda env list | grep ".*PYTEST_ENV.*" >/dev/null 2>&1; then
    echo "Updating Environment"
    conda env update --name PYTEST_ENV --file ../pytest_env.yml --prune -q
  else
    echo "Creating Environment"
    conda env create --name PYTEST_ENV --file ../pytest_env.yml -q
  fi
  echo "Internalizing Environment"
  conda activate PYTEST_ENV
  echo "Set Up Complete"
  python run.py
  echo "Tearing Down Environment"
  conda deactivate
  taskkill /F /IM chromedriver.exe
}  2>&1 | tee -a ./run_logs/log_"$(date "+%d-%m-%y-%H%M")".out
