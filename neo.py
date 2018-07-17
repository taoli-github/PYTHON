"""
with driver.session() as session:
    with session.begin_transaction() as tx:
        tx.run(sql)
"""

from neo4j.v1 import GraphDatabase, basic_auth


query = "match p=(n)-[:is_symptom_of]->(d:Disease) " \
        "return p "
insert_sql = "merge(s:Symptom{name:'胸痛'}) " \
            "merge(d:Disease{name:'胸膜炎'})" \
            "merge(s)-[:is_symptom_of]->(d) "

driver = GraphDatabase.driver("bolt://10.68.4.55:7687", auth=basic_auth("neo4j", "neo4j55"))

# 1. 常规调用
# session = driver.session()
# results = session.run(query)
#
# for res in results:
#     print(res["p"])
#
# session.close()


# 2 事务
# 2.1 自动提交
with driver.session() as sess:
    sess.run(query)


# 2.2 显示提交
with driver.session() as sess:
    tx = sess.begin_transaction()
    tx.run(query)
    tx.commit()


# 2.3 函数提交 推荐
def find_symps(tx, name):
    result_list = tx.run(insert_sql)
    for item in result_list:
        print(item["p"])


with driver.session() as sess:
    """ read_transaction  write_transaction """
    sess.read_transaction(find_symps, 'name')

# driver.close()
