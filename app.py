import streamlit as st
from utils.data_io import read_vms, read_hosts, read_network, export_plan
from planners.migration import migration_planner
from utils.network_graph import build_graph, visualize_graph

st.title("VM Migration Planner")

vm_file = st.file_uploader("Upload VM dataset (CSV/JSON):")
host_file = st.file_uploader("Upload Host dataset (CSV/JSON):")
net_file = st.file_uploader("Upload Network Topology (CSV/JSON):")

if vm_file and host_file and net_file:
    vms = read_vms(vm_file)
    hosts = read_hosts(host_file)
    network_df = read_network(net_file)
    plan = migration_planner(vms, hosts)
    G = build_graph(network_df, hosts, vms, plan)

    html_file = visualize_graph(G, "network_graph.html")
    with open(html_file, 'r', encoding='utf-8') as f:
      html_content = f.read()
    st.components.v1.html(html_content, height=750)


    if st.button("Export Migration Plan as CSV"):
        export_plan(plan, "migration_plan.csv")
        st.success('Migration plan exported as migration_plan.csv.')
    if st.button("Export Migration Plan as JSON"):
        export_plan(plan, "migration_plan.json")
        st.success('Migration plan exported as migration_plan.json.')

    st.write("Migration Plan Preview:", plan)
else:
    st.warning("Upload all required datasets to proceed.")
