import canopen
import time

network = canopen.Network()
network.connect(channel='vcan0', bustype='socketcan')

network.scanner.search()
time.sleep(0.05)

for node_id in network.scanner.nodes:
    print("Found node %d!" % node_id)
    if node_id == 2:
        node = network.add_node(node_id)
        for i in range(0x1000, 0x7000):
            for j in range(10):
                try:
                    byte = node.sdo.upload(i, j)
                    list_byte = list(byte)
                    listTestByteAsHex = [hex(x)[2:] for x in list_byte]

                    print(f"Index: {i}, Subindex: {j}, Value: {listTestByteAsHex}")
                except canopen.sdo.exceptions.SdoAbortedError:
                    pass





    # node = network[node_id] 

# network.disconnect()
