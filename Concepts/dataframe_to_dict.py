import pandas as pd

header = ["u_knowledge", "assignment_group", "ticket_management", "category"]
row = [["A5", "sap marketing", "athos", "Process Issue"], ["A5", "sap marketing",
                                                           "athos", "Process Issue"], ["A5", "sap marketing", "athos", "Process Issue"]]

df = pd.DataFrame(row, columns=header)

print(df.to_dict('records'))


print(list(df['u_knowledge']))
