# pytest_framework_template

#### A simple framework to jump start web ui testing using Selenium Webdriver and the Pytest Page Object testing framework
### Includes functions to help find and use web elements, simplifying test methods.
When developing test scripts it is recommended to run test cases in an IDE that has pytest integration such as PyCharm.

### To Run Locally
Requires [Anaconda/Minconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html) to be installed and added to PATH.

Simply navigate to the project build folder and run build_run.sh
```
cd [YOUR_PATH]/project_path/build
build_run.sh
```

### Environment Setup
Miniconda3 was used to manage this suite's environment. Be free to use your preferred method.

The pytest_env.yml is optimized for conda. To initialize first install [Anaconda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html). Then from your IDE terminal run
```
conda env create --name ENV_NAME --file [FILE_PATH]/pytest_env.yml
cond activate ENV_NAME
```
Now you are ready to create and run tests.

If you install additional packages be sure to update the .yml otherwise the build script will fail. 

Simply Run in the IDE terminal
```
conda env export > pytest_env.yml
```

### Debugging Tests
To assist in debugging tests it is recommended to disable headless mode, so you can watch the code control the browser 
In conftest.py comment out ```opts.headless = True```

### Further Reading
Check out the [wiki](https://github.com/cdubwisdom/pytest_framework_template/wiki) (WIP) for a deeper dive into the various modules
Please Review the [Writer]() class before developing new test methods
