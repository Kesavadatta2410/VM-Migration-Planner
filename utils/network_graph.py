import networkx as nx
from pyvis.network import Network

def build_graph(network_df, hosts, vms, plan):
    G = nx.Graph()
    for idx, row in network_df.iterrows():
        G.add_edge(row['src'], row['dst'], label=row.get('label', ''))
    for host in hosts:
        G.add_node(host.id, label=f"Host: {host.id}")
    for vm in vms:
        G.add_node(vm.id, label=f"VM: {vm.id}", color='lightblue')

    # Add migration plan as arrows
    for mapping in plan:
        if mapping['host_id']:
            G.add_edge(mapping['vm_id'], mapping['host_id'], color='red', title='Migration', arrows='to')
    return G

def visualize_graph(G, output_html):
    net = Network(height="700px", width="100%", directed=True)
    net.from_nx(G)
    net.show(output_html)
    return output_html
