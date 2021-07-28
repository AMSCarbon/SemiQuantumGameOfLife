#Benchmarking

100 * 100 = 10000 cells
Display.update: 0.004604
ClassicModel.__create_empty_matrix: 0.008089
ClassicModel.get_neighbours: 0.000005
ClassicCell.get_next_state: 0.000001
ClassicModel.update: 0.116575

200*200 = 40000
Display.update: 0.018389
ClassicModel.__create_empty_matrix: 0.059397
ClassicModel.get_neighbours: 0.000005
ClassicCell.get_next_state: 0.000002
ClassicModel.update: 0.519843


ClassicModel.get_neighbours+ ClassicModel.get_next_state * cell_count = 0.28
+ClassicModel.__create_empty_matrix: 0.059397 = 0.34

0.18 seconds unaccounted for?
    
The functions individually don't take very long, it's mainly the fact we're looping over all of them.
Want to reduce the number of cells to consider during a loop.

Observation:  
There's wide areas of "dead" cells we don't really need to bother considering. Change only happens around live cells.

Create a list of live cells. For each of these cells, get the neighbours. 

Create a dictionary with the key as the cell's index and the value the number of times it appeared.
the new state is then determined by the number times the cell was a neighbour.

This way we can update the values directly too, rather than creating a new grid.

New benchmarking:

200 * 200 = 40000
ClassicModel.__create_empty_matrix: 0.038110
Display.update: 0.005692
ClassicModel.get_neighbours: 0.000004
ClassicCell.get_next_state: 0.000001
ClassicModel.update: 0.022168

awyyiiissssss