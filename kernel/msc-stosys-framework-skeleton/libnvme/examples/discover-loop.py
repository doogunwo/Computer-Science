#!/usr/bin/python3
'''
Example script for nvme discovery

Copyright (c) 2021 Hannes Reinecke, SUSE Software Solutions
Licensed under the Apache License, Version 2.0 (the "License"); you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
'''

import libnvme
r = libnvme.nvme_root()
h = libnvme.nvme_host(r)
c = libnvme.nvme_ctrl('nqn.2014-08.org.nvmexpress.discovery','loop')
try:
    c.connect(h)
except:
    sys.exit("Failed to connect!")

print("connected to %s subsys %s" % (c.name, c.subsystem.name))
try:
    d = c.discover()
    print (d)
except:
    print("Failed to discover!")
    pass
c.disconnect()
