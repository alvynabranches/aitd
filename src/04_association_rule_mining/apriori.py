import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori

dataset = [
    ["Milk", "Eggs", "Bread"],
    ["Milk", "Eggs"],
    ["Milk", "Bread"],
    ["Eggs", "Apple"],
    ["Jam", "Bread"],
    ["Bread", "Butter"],
    ["Butter", "Eggs", "Bread"],
    ["Bread", "Butter"],
]

te = TransactionEncoder()
te_array = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_array, columns=te.columns_)

# print(df)
frequent_itemsets_ap = apriori(df, min_support=0.01, use_colnames=True)
print(frequent_itemsets_ap)