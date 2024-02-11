# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from firefly_iii_client.paths.v1_bills_id_transactions import Api

from firefly_iii_client.paths import PathValues

path = PathValues.V1_BILLS_ID_TRANSACTIONS