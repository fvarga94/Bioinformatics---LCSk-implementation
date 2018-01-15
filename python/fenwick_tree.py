class Fenwick_tree(object):
    #Fenwick tree for range max query implementation
    def __init__(self,size):
        # we intialize the size to +1 since the 0 node is not
        # a part of the Binary Index Tree structure (BIT)
        #size+=1
        self.f_tree=[0]*(size+1)
        self.length=size+1

    def get(self,i):
        #the get method calculates ths maximum in the [0,i] range
        #this is done in O(log n) time complexity
        result=0
        i+=1
        while(i>=0):
            result=max(result,self.f_tree[i])
            i=(i&(i+1))-1
            #we calculate the next index by remowing the most significant bit
        return result

    def update(self,i,value):
        # the update method updates the BIT to allow for max range query calculation
        #this is also done in O(log n) time complexity
        i+=1
        while(i<self.length):
            self.f_tree[i]=max(self.f_tree[i],value)
            i|=i+1

if __name__ == '__main__':
    #tests for the Fenwick tree structure
    ft=Fenwick_tree(5)
    ft.update(3,5)
    for i in range(0,5):
        print (ft.get(i))
    print ("Update")
    ft.update(2,4)
    for i in range(0,5):
        print (ft.get(i))
    print ("Update")
    ft.update(1,6)
    for i in range(0,5):
        print (ft.get(i))
