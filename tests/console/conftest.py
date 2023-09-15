import pytest


# Target 1 and their permutations
@pytest.fixture(scope="module")
def valid_yaml_target1_1():
    return """
    target:
        cmd:
            python script1.py
    """


# Target 2
@pytest.fixture(scope="module")
def valid_yaml_target2_1():
    return """
    target:
        var:
            basic:
                - var1
                - var2
                - var3
                - var4
        cmd:
            python script1.py
    """


# Target 3
@pytest.fixture(scope="module")
def valid_yaml_target3_1():
    return """
    target:
        var:
            basic: var1
        cmd:
            python script1.py
    """


# Target 4
@pytest.fixture(scope="module")
def valid_yaml_target4_1():
    return """
    target:
        var:
            option:
                all: "-a"
        cmd:
            python script1.py
    """


# Target 5
@pytest.fixture(scope="module")
def valid_yaml_target5_1():
    return """
    target:
        var:
            sequence:
                list1
        cmd:
            python script1.py
    """


# Target 6
@pytest.fixture(scope="module")
def valid_yaml_target6_1():
    return """
    target:
        var:
            sequence:
                list1: [1,2,3]
        cmd:
            python script1.py
    """


# Target 7
@pytest.fixture(scope="module")
def valid_yaml_target7_1():
    return """
    target:
        var:
            basic:
                var1: 1
                var2: 2
                var3: null
            sequence:
                list1: [1,2,3]
        cmd:
            python script1.py
    """


# Target 8
@pytest.fixture(scope="module")
def valid_yaml_target8_1():
    return """
    target:
        var:
            basic:
                var1: null
                var2: 2
                var3: null
            sequence:
                list1: null
        cmd:
            python script1.py
    """


# Target 9
@pytest.fixture(scope="module")
def valid_yaml_target9_1():
    return """
    target:
        var:
            basic:
                var1: null
                var2: 2
                var3: null
            option:
                all: "-all"
                quiet: "-quiet"
            sequence:
                list1: null
                list2: null
        cmd:
            python script1.py
    """


# Target 10
@pytest.fixture(scope="module")
def valid_yaml_target10_1():
    return """
    target:
        var:
            basic:
                var1: 10
                var2: 2
                var3: 14
            option:
                all: "-all"
                quiet: "-quiet"
            sequence:
                list1: null
                list2: null
        env:
            env1: $(var1)
            env2: $(var2)
        cmd:
            - python script1.py
            - python script2.py
    """


# Test 11
@pytest.fixture(scope="module")
def valid_yaml_target11_1():
    return """
    target:
        var:
            basic: var1
            sequence: list1

        cmd:
            - python script1.py
            - python script2.py
    """


# Test 12
@pytest.fixture(scope="module")
def valid_yaml_target12_1():
    return """
    target:
        var:
            basic:
                var1: 1
                var2: 2
                var3: 3
            sequence:
                list1: [1, 2, 3]
                list2: [4, 5, 6]
            option:
                all: "-a"
        env:
            ENV1: $(var1)
            ENV2: $(var2)
        cmd:
            - ls $(all)
            - python script1.py $(list1)
            - python script2.py --var3 $(var3) $(list2)
    """


# Test 13
@pytest.fixture(scope="module")
def valid_yaml_target13_1():
    return """
    target:
        var:
            sequence:
                list1: 1
                list2: [1, 2, 3]
                list3: null

        cmd:
            - echo Hello
    """
