class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_tank = 0
        current_tank = 0
        start = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            current_tank += diff
            
            # If we can't reach next station
            if current_tank < 0:
                start = i + 1
                current_tank = 0
        
        # If total gas is enough, return start index
        return start if total_tank >= 0 else -1