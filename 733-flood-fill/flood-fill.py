class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        x,y = len(image),len(image[0])
        v = image[sr][sc]
        if v == color:  
            return image
        def fill(p,q):
            if p>=x or p<0 or q>=y or q<0:
                return
            if image[p][q] != v:
                return
            image[p][q] = color
            fill(p-1,q)
            fill(p+1,q)
            fill(p,q-1)
            fill(p,q+1)  
        fill(sr, sc)     
        return image

                
                
                
                

                

                
