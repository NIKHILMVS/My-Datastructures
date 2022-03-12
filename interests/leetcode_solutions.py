class TwoSum(object):
    def __init__(self):
        self.nums=None
        self.target=None

    def my_solution(self):
        # Brute Force : O(n)**2
        for i1,i in enumerate(self.nums):
            for j1,j in enumerate(self.nums):
                if i+j==self.target and i1!=j1:
                    return [i1,j1]

    def ideal_solution(self):
        # Optimal : O(n)
        values={}
        for idx,e in enumerate(self.nums):
            if self.target-e in values:
                return [idx,values[self.target-e]]
            else:
                values[e]=idx

    def execute(self):
        self.nums=[1,3,5,7]
        self.target=8
        sol=self.my_solution()
        sol=self.ideal_solution()
        print(sol)

TwoSum().execute()
