from typing import Dict

def load_services() -> Dict[str, str]:
    services = {
        "compute": "Cloud computing service for running virtual machines",
        "storage": "Object storage service for data persistence",
        "database": "Managed database service for various DB engines",
        "network": "Virtual networking and connectivity service",
        "serverless": "Function-as-a-service platform for event-driven compute",
    }
    return dict(sorted(services.items()))


def get_service_description(service_name):
    services_map = load_services()
    sorted_keys = list(services_map.keys())
    index = sorted_keys.index(service_name)
    print((index + len(sorted_keys)) % len(service_name))
    for i in services_map.keys():
        if service_name==i:
            mapped_key=i
    print(mapped_key)
    return services_map[mapped_key]


services = get_service_description("database")
print(services)
