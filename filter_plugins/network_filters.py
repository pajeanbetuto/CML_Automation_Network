#!/usr/bin/env python3

class FilterModule(object):
    def filters(self):
        return {
            'subnet_mask': self.subnet_mask,
            'wildcard_mask': self.wildcard_mask
        }

    def subnet_mask(self, cidr):
        """Convert CIDR to subnet mask"""
        prefix = int(cidr.split('/')[1])
        mask = (0xffffffff >> (32 - prefix)) << (32 - prefix)
        return '.'.join([str((mask >> (8 * (3 - i))) & 0xff) for i in range(4)])

    def wildcard_mask(self, cidr):
        """Convert CIDR to wildcard mask"""
        prefix = int(cidr.split('/')[1])
        mask = (0xffffffff >> prefix)
        return '.'.join([str((mask >> (8 * (3 - i))) & 0xff) for i in range(4)])