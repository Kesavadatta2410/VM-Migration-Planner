def migration_planner(vms, hosts):
    plan = []
    hosts_map = {host.id: host for host in hosts}
    for vm in vms:
        for host in hosts:
            if host.can_host(vm):
                host.add_vm(vm)
                plan.append({'vm_id': vm.id, 'host_id': host.id})
                break
        else:
            plan.append({'vm_id': vm.id, 'host_id': None})
    return plan
