from voluptuous import In, IsDir, Required, Schema, Url

from .validators import Hostname, LXDIdentifier


_top_level_and_containers_common_options = {
    'hostnames': [Hostname(), ],
    'image': str,
    'mode': In(['local', 'pull', ]),
    'privileged': bool,
    'protocol': In(['lxd', 'simplestreams', ]),
    'provisioning': [{
        # Common options
        'type': str,

        # Ansible specific options
        'playbook': str,
    }],
    'server': Url(),
    'shares': [{
        # The existence of the source directory will be checked!
        'source': IsDir(),
        'dest': str,
    }],
    'shell': {
        'user': str,
        'home': str,
    },
}

_container_options = {
    Required('name'): LXDIdentifier(),
}
_container_options.update(_top_level_and_containers_common_options)

_nomad_options = {
    Required('name'): LXDIdentifier(),
    'containers': [_container_options, ],
}
_nomad_options.update(_top_level_and_containers_common_options)

# The schema will be used to validate nomad files!
schema = Schema(_nomad_options)