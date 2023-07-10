import math 

def min_max(current_depth,node_index,scores,target_depth,maxturn):
    if(current_depth==target_depth):
        return scores[current_depth]
    if(maxturn):
        return max(min_max(current_depth+1,node_index*2,scores,target_depth,False),min_max(current_depth+1,node_index*2 +1,scores,target_depth,False))
    else:
        return min(min_max(current_depth+1,node_index*2,scores,target_depth,False),min_max(current_depth+1,node_index*2 +1,scores,target_depth,False))
    
score=[1,2,3,4,5,6,7,8]
target_depth=math.log(len(score),2)
print(f"optimal value is ")
print(min_max(0,0,score,target_depth,True))