import requests
from flask import Blueprint

currency = Blueprint('currency', __name__)

apikey = 'e0a715edb85967dacb821d18'


@currency.route('/currency/<base_currency>/<target_currency>/<amount>', methods=['GET'])
def exchange_rate(base_currency: str, target_currency: str, amount: str) -> dict:
    """
    Method supply different currency exchange information update
    :param base_currency: Base currency to be taken for ratio and conversion#
    :param target_currency: Target currency to be taken for ratio and conversion
    :param amount: Amount to converted
    :return: expected return to provide a json dictionary with information about the ratio, latest system update,
    resul also base and target currency or error dictionary supply by 3rd part API
    """
    exchange_info = requests.get(
        'https://v6.exchangerate-api.com/v6/'
        + apikey + '/pair/' + base_currency + '/' + target_currency + '/' + amount).json()

    try:
        return {
            'Last_Update_Date': exchange_info['time_last_update_utc'],
            'Base': exchange_info['base_code'],
            'Target': exchange_info['target_code'],
            'Rate': exchange_info['conversion_rate'],
            'Result': exchange_info['conversion_result']
        }
    except KeyError:
        return {
            'Result': exchange_info['result'],
            'Error-Type': exchange_info['error-type']
        }
