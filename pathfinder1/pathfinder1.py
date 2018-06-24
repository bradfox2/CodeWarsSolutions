#bfs for pathfinder 1 with some commented code setting up a*

def path_finder(maze):   

    #unpack maze string into list of lists
    maze = [list(i) for i in maze.split("\n")]

    #calc the bottom right most dot (y,x)
    finish_coords = [len(maze)-1, len(maze)-1] #always square maze
    
    #one list for possible pathways remaining
    possible_paths = [[0,0]]
    
    #one set for visited nodes
    visited = set()
    
    maze_l = len(maze)
    
    #manhattan_score = set()
    #still have path options, keep trying
    while possible_paths:

        #grab the lowest cost path appended
        #frontier = heapq.heappop(possible_paths)
        #print(frontier)
        #print(frontier[0])
        #if tuple(frontier) in seen:
        #    next

        #if frontier[0] != 1: 
        #    manhattan_score.add(frontier[0])
        #else:
        #    manhattan_score.add(60)
        #frontier = frontier[1]

        #return if frontier is our goal
        #if frontier[0] > min(manhattan_score) + 15:
        #    return(False)
        
        current_node = possible_paths.pop()
                
        if current_node == finish_coords:
            return(True)        

        y = current_node[1]
        x = current_node[0]
        visited.add((x,y)) 

        #check right
        if x + 1 < maze_l and maze[y][x+1] == '.' and (x+1,y) not in visited:
            #manhattan for cardinal direction
            #h =  abs(frontier[1] - end_coords[1]) + abs(frontier[0] - end_coords[0]) 
            #heappush(possible_paths,(h,right))
            possible_paths.append([x+1,y])           
            
        #check left
        if x - 1 >= 0 and maze[y][x-1] == '.' and (x-1,y) not in visited:
            #h =  abs(frontier[1] - end_coords[1]) + abs(frontier[0] - end_coords[0]) 
            #heappush(possible_paths,(h,down))
            possible_paths.append([x-1,y])           

        #print(maze[y+1][x])    
        #check down
        if y + 1 < maze_l and maze[y+1][x] == '.' and (x, y + 1) not in visited:
            #h =  abs(frontier[1] - end_coords[1]) + abs(frontier[0] - end_coords[0]) 
            #heappush(possible_paths,(h,left))
            possible_paths.append([x,y+1])
            
        #check up
        if y - 1 >= 0 and maze[y-1][x] == '.' and (x, y-1) not in visited:

            #h =  abs(frontier[1] - end_coords[1]) + abs(frontier[0] - end_coords[0]) 
            #heappush(possible_paths,(h,up))
            possible_paths.append([x,y-1])
        
    return(False)