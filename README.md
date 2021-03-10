# ExperimentManager

A basic pytest setup for experiments management

Pytest gives you parallelization and worker managment with pytest-xdist and html reports with pytest-html.
To get a specific order of execution of batches of experiments we just run pytest couple of times with different markers (each marking a different batch).
There is also a fixture to assign a gpu number to each worker, you just need to make sure that the number of workers is smaller or equal that number of gpus specified (as a command argument of *src/main.sh*).

How to use:
1. Put all your experiments in *src/research_tests/*, each experiment function needs to start with 'test_'
1. Define your markers in *src/research_tests/pytest.ini*
1. Modify *src/main.sh* with your markers an number of workers for each batch.
1. Use *src/main.sh* to execute your experiments.

General project setup on MacOS:
1. git clone git@github.com:EnderGed/experiment-manager.git
1. cd experiment-manager
1. pyenv install 3.7.5 # of course any version of python will work
1. Create a virtualenv:
* pip3 install virtualenv
* virtualenv -p ~/.pyenv/versions/3.7.5/bin/python venv
* source venv/bin/activate
* pip3 install -r requirements.txt
* deactivate

Working on project (in venv):
* source venv/bin/activate
* ... your work ...
* deactivate

Managing pip requirements
* pip3 freeze >requirements.txt # saving new requirements
* pip3 install -r requirements.txt # updating requirements

Running experiments
* cd src
* ./main.sh # maybe you need to chmod o+x main.sh first
* you see all the workers spawning and doing the work
* checkout the neat html reports in ../results/
