from hash_tables.hash_tables import Hashtable


def left_join(table_1, table_2):

    table_1_join = []

    for key in table_1:
        join_left = [key, table_1.get(key), table_2.get(key) or "NULL"]
        table_1_join.append(join_left)

    return table_1_join
