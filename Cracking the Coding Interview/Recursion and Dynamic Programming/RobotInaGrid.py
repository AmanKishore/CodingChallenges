'''
Robot In a Grid:
    Determine if threre is a path for the robot if it can only move down and right.
'''

def getPath(maze):
    if not maze or len(maze) == 0:
        return None
    path = []
    failedPoints = []
    if isPath(maze, len(maze)-1, len(maze[0])-1, path, failedPoints):
        return path
    return None

def isPath(maze, row, col, path, failedPoints):
    if col < 0 or row < 0 or not maze[row][col]: # Checks if out of bounds or false
        return False
    
    point = (row, col)

    if point in failedPoints: # Checks if visited
        return False

    isAtOrigin = (row == 0) and (col == 0)

    # If there's a path from start to my current location, add my location
    if isAtOrigin or isPath(maze, row, col-1, path, failedPoints) or isPath(maze, row-1, col, path, failedPoints):
        path.append(point)
        return True

    failedPoints.append(point) 
    return False