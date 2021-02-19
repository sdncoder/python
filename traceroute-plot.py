import networkx as nx
import matplotlib.pyplot as plt
data = """traceroute to xxx"""
data = data.split("\n")
data = data[1:]
cleaned_ip = [ ",".join(item.split()[1:4]) for item in data if "* * *" not in item ]
import re
pattern = r'[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+'
path_list = [re.findall(pattern,line)[0] for line in cleaned_ip]
node_node = zip(path_list,path_list[1:])
node_node
trace = nx.Graph()
[trace.add_edge(a,b) for a,b in node_node]
trace.edges()
trace.nodes()
nx.draw(trace)
plt.show()
