import math

def alpha_beta(depth,nodeindex,maxplayer,values,alpha,beta,):
    if(depth==3):
        return values[nodeindex]
    if(maxplayer):
        best=-1000
        for i in range (0,2):
            val=alpha_beta(depth+1,nodeindex*i,False,values,alpha,beta)
            best=max(best,val)
            alpha=max(best,alpha)
            if beta<=alpha:
                break
        return best
    else:
        best=1000
        for i in range(0,2):
            val=alpha_beta(depth+1,nodeindex*i,True,values,alpha,beta)
            best=min(best,val)
            beta=min(beta,best)
            if beta<=alpha:
                break;
        return best
    
if __name__ == "__main__":
    values=[2,4,6,7,1,9,3]
    print(values)
    print(f"optimal value is ",alpha_beta(0,0,True,values,1000,-1000))
