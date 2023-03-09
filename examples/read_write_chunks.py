import hpc_datastore as ds
import numpy as np

#help(ds.Connection)
conn = ds.Connection("localhost",9080,"6f94cc3b-e206-4ee3-91f1-a117e77d6193")
print(conn.get_properties())

imgArray:np.ndarray = conn.read_block([0,0,0],0,0,0,[1,1,1],"0")

channel = 560
value = 561
# spadlo to po odeslani 558 chunku.. tzn u konce radku 15
for y in range(16,35):
    for x in range(35):
        print(f"writing channel {channel}")
        imgArray.fill(value)
        conn.write_block(imgArray, [x,y,0],[0,0,0],channel,0,0,[1,1,1],"0")

        value += 1
        channel += 1

print("done writing")