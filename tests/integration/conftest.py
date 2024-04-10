import pytest

def pytest_addoption(parser):
    """
    This function is called by pytest to add custom command line options.
    
    parameters
    ----------
    parser: object
        The parser object that will be used to add the custom command line options.
        
    prints
    -------
    scoreurl: str
        The url of the ml web service.
        
    scorekey: str
        The key of the ml web service.
    """
    parser.addoption("--scoreurl", action="store",
        help="the score url of the ml web service")
    parser.addoption("--scorekey", action="store",
        help="the score key of the ml web service")

@pytest.fixture
def scoreurl(request):
    return request.config.getoption("--scoreurl")

@pytest.fixture
def scorekey(request):
    return request.config.getoption("--scorekey")
