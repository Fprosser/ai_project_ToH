
# Solving Towers of Hanoi with recursion in python

#The Recursive function that prints the instructions
def TowerSolver(k, source_rod, dest_rod, aux_rod):
    #first we want to get 1, how we achieve this is by repeatedly calling it with k-1 on line 10
    if k == 1:
        print("Move disk 1 from rod",source_rod,"to rod",dest_rod)
        #once we hit this return statement we go back through the stack
        return
    TowerSolver(k-1, source_rod, aux_rod, dest_rod)
    print("Move disk",k,"from rod",source_rod,"to rod",dest_rod)
    TowerSolver(k-1, aux_rod, dest_rod, source_rod)

    #if you have an IDE where this algorithm can be stopped every execution time it is much easier to see how it works
    #rather hard to explain every step

#Driver Code
k = 4
#^^^number of disks
TowerSolver(k,'A', 'C', 'B')
