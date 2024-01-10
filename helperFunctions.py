import xrpl
from pprint import pprint 

testnet_url = "https://s.altnet.rippletest.net:51234"
client = xrpl.clients.JsonRpcClient(testnet_url)

def wallet_from_seed(seed):
    return xrpl.wallet.Wallet.from_seed(seed)

def conf_cold_settings(wallet):
    settings_tx = xrpl.models.transactions.AccountSet(
        account=wallet.address,
        transfer_rate= 0,
        tick_size=5,
        domain=bytes.hex("LBTOWA".encode("ASCII")),
        set_flag=xrpl.models.transactions.AccountSetAsfFlag.ASF_DEFAULT_RIPPLE,
    )

    # print("Sending AccountSet transaction...")
    response = xrpl.transaction.submit_and_wait(settings_tx, client, wallet)
    # pprint(response)

    return response


def conf_hot_settings(wallet):
    settings_tx = xrpl.models.transactions.AccountSet(
        account=wallet.address,
        set_flag=xrpl.models.transactions.AccountSetAsfFlag.ASF_REQUIRE_AUTH,
    )

    # print("Sending hot address AccountSet transaction...")
    response = xrpl.transaction.submit_and_wait(settings_tx, client, wallet)
    # pprint(response)

    return response

def create_trust_line(issuer_address,currency_code,reciver_seed):
    wallet = wallet_from_seed(reciver_seed)
    trust_set_tx = xrpl.models.transactions.TrustSet(
        account=wallet.address,
        limit_amount=xrpl.models.amounts.issued_currency_amount.IssuedCurrencyAmount(
            currency=currency_code,
            issuer=issuer_address,
            value="10000000000", # Large limit, arbitrarily chosen
        )
    )

    # print("Creating trust line from hot address to issuer...")
    response = xrpl.transaction.submit_and_wait(trust_set_tx, client, wallet)
    # pprint(response)

    return response

def issue_tokens(issue_quantity,currency_code,cold_wallet,hot_wallet):
    send_token_tx = xrpl.models.transactions.Payment(
        account=cold_wallet.address,
        destination=hot_wallet.address,
        amount=xrpl.models.amounts.issued_currency_amount.IssuedCurrencyAmount(
            currency=currency_code,
            issuer=cold_wallet.address,
            value=issue_quantity
        )
    )

    # print(f"Sending {issue_quantity} {currency_code} to {hot_wallet.address}...")
    response = xrpl.transaction.submit_and_wait(send_token_tx, client, cold_wallet)
    # print(response)

    return response
