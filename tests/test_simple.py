from brownie import SimpleStorage, accounts


def test_storage():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = 0
    # Act

    # Assert
    assert starting_value == simple_storage.retrieve()


def test_storage_update():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})

    expected_value = 20
    simple_storage.store(expected_value, {"from": account})

    assert expected_value == simple_storage.retrieve()

