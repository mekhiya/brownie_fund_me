from brownie import config, FundMe, network, MockV3Aggregator
from scripts.deploy import deploy_fund_me
from scripts.helpful_scripts import get_account, deploy_mocks


def fund():
    account = get_account()
    fund_me = FundMe[-1]
    # fund_me = deploy_fund_me()
    entrance_fee = fund_me.getEntranceFee()
    print(f"Entrance fee is {entrance_fee}")
    print("Funding...")
    fund_me.fund({"from": account, "value": entrance_fee})


def withdraw():
    account = get_account()
    fund_me = FundMe[-1]
    print("Withdrawing...")
    tx = fund_me.withdraw({"from": account})
    tx.wait(1)


def main():
    fund()
    withdraw()
