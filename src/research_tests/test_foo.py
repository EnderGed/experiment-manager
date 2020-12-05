import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

# maybe the path is not the most elegant, it can also be done with an environmental variable

import logging
import pytest

# ##########--------------  PREPARE FOR TESTING  --------------###########
# Run everything you need before running experiments
#   e.g., making sure the folder structure is correct,
#   creating some helper functions


def is_done(name, directory, appendix=''):
    return os.path.isfile('{}{}{}'.format(directory, name, appendix))


def skip_if_done(name, directory, appendix=''):
    if is_done(name, directory, appendix):
        pytest.skip('{}{}{} already exists'.format(directory, name, appendix))


dirs = {
    'data': '../data/',
    'inter': '../data/inter/',
    'results': '../data/results/'
    }
# make sure all the directories exist
for tmp_dir in dirs.values():
    if not os.path.exists(tmp_dir):
        os.makedirs(tmp_dir)


# ##########--------------  DATA PREPROCESSING  --------------###########
@pytest.mark.parametrize('name', ['Alice', 'Bob'])
@pytest.mark.parametrize('num', [1,2,3])
# make sure that the mark is defined in pytest.ini
# multiple functions can have the same mark
# one function can have multiple marks
@pytest.mark.preprocess
def test_create_some_files(name, num):
    # if the file already exists, skip this experiment
    skip_if_done('{}{}'.format(name, num), dirs['inter'], '.txt.')
    with open('{}{}{}.txt'.format(dirs['inter'], name, num), 'w') as f:
        f.write('foo\n')



# ##############--------------  EXPERIMENTS  --------------###############
@pytest.mark.parametrize('name,num,value', [
    ('Alice', 2, 'bar'),
    ('Bob', 1, 'bar'),
    ('BoB', 3, 'bar'),
])
@pytest.mark.experiments1
def test_bar(name, num, value):
    tmp = open('{}{}{}.txt'.format(dirs['inter'], name, num), 'r').readlines()
    logging.warning('This will be in the report.')
    logging.debug("This won't, because pytest-html only captures warning and above")


@pytest.mark.parametrize('arg1,arg2', [('foo', 1), ('bar', 2)])
@pytest.mark.experiments1
def test_on_gpus(arg1, arg2, gpu):
    cuda = 'cuda:{}'.format(gpu)
    # device = torch.device(cuda) # if you use pytorch
    # prints are also captured by the html reports
    print('Runnin {}_{} on gpu:{}.'.format(arg1, arg2, gpu))
