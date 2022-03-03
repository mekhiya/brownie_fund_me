from brownie import config, FundMe, network, MockV3Aggregator, accounts, exceptions
from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
    get_account,
    deploy_mocks,
)
from scripts.deploy import deploy_fund_me
import pytest


def test_can_fund_and_withdraw():
    account = get_account()
    fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee() + 100
    print(f"Entrance_fee is {entrance_fee}")
    print(
        f"1 - fund_me.addressToAmountFunded(account.address) is {fund_me.addressToAmountFunded(account.address)}"
    )
    tx = fund_me.fund({"from": account, "value": entrance_fee})
    tx.wait(1)
    print(
        f"2 - fund_me.addressToAmountFunded(account.address) is {fund_me.addressToAmountFunded(account.address)}"
    )
    assert fund_me.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me.withdraw({"from": account})
    tx2.wait(1)
    print(
        f"3 - fund_me.addressToAmountFunded(account.address) is {fund_me.addressToAmountFunded(account.address)}"
    )
    assert fund_me.addressToAmountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("only for local testing")
    # Arrange
    account = accounts[0]
    fund_me = deploy_fund_me()

    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me.withdraw({"from": bad_actor})
    # create two accounts accounts[0] & accounts[1]
    # accounts[0] deploys contract hence becomes admin
    # NOT REALLY REQUIRED - both accounts deposit money

    # Act
    # second account tries to run withdraw

    # Assert
    # Throws Error

    # Firts accoutn calls withdraw, works fine
