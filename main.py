#
# Copyright (c) 2023 Airbyte, Inc., all rights reserved.
#


import sys

from destination_bilal_connector_py import DestinationBilalConnectorPy

if __name__ == "__main__":
    DestinationBilalConnectorPy().run(sys.argv[1:])
