from concurrent.futures import ProcessPoolExecutor

from db.models.operation import Operation
from sqlalchemy.exc import DataError, OperationalError
from db.settings.base import Session
from logic.math_logic import figure_out_operation, allowed_operations

session = Session()

executor = ProcessPoolExecutor(max_workers=10)


def add_to_db(operator: str, n1: str, n2: str) -> str:
    future_obj = executor.submit(add_to_db_without_multi_proc, operator, n1, n2)
    return future_obj.result()


def add_to_db_without_multi_proc(operator: str, n1: str, n2: str) -> str:
    res = figure_out_operation(operator, n1, n2)
    session.add(Operation(operator, n1, n2, res))
    try:
        session.commit()
    except DataError:
        res = ''
    except OperationalError:
        res += '\tThe results are not put into the database.!'
    finally:
        session.close()
    return res


def get_filter(props: dict, oper: str):
    limit, offset = '', ''
    if 'limit' in props.keys():
        limit = props['limit']
    if 'offset' in props.keys():
        offset = props['offset']
    if not offset:
        offset = 0

    if not oper in allowed_operations:
        return {}

    if limit:
        return query_to_dict(session.query(Operation).filter(Operation.operator == oper) \
                             .offset(offset).limit(limit))
    else:
        return query_to_dict(session.query(Operation).filter(Operation.operator == oper) \
                             .offset(offset))


def get_all():
    return query_to_dict(session.query(Operation).all())


def query_to_dict(operations) -> dict:
    res = {}
    i = 0
    for oper in operations:
        res[i] = f'{str(oper.operator)}: ' \
                 f'{str(oper.number1)} {str(oper.number2)}, ' \
                 f'result: {str(oper.result)}'
        i += 1
    return res
