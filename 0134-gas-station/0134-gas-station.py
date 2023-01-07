class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost): 
            return -1
        tank = 0 
        index = 0 
        for x in range(len(gas)):
            tank = tank + gas[x]-cost[x] # tank+= gas[x]-cost[x]
            if tank < 0: tank, index = 0, x+1
        return index
            