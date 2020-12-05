import pytest


# ##########------------  GPU ASSIGNMENT FIXTURE  -------------###########
# add the pytest argument --gpus
def pytest_addoption(parser):
    parser.addoption("--gpus", type=str, help="comma seperated list of available gpus", required=True)


def pytest_generate_tests(metafunc):
    if "gpus" in metafunc.fixturenames:
        metafunc.parametrize("gpus", [metafunc.config.getoption("gpus")])

# any test with an argument 'gpu' will get a gpu from this fixture
@pytest.fixture()
def gpu(worker_id, gpus):
    gpus_list = gpus.split(',')
    worker_num = int(worker_id[2:])
    try:
        return gpus_list[worker_num]
    except IndexError:
        raise Exception('Number of workers needs to be smaller or equal to number of gpus available. No gpu for '
                        'worker {}.'.format(worker_id))
