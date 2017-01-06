class Solution {
public:
    int row = 0; 
    int col  = 0;
    int visit(vector<vector<int>>& grid , int **visited, int r , int c , int p){
        
        if (visited[r][c] == 1) return p;
        visited[r][c] = 1;
        
        if (grid[r][c] == 1){
            
            // cout << visited[r][c] << endl;
            
            if ( c == 0 || grid[r][c-1] == 0) p++ ; // left
            
            if ( c == col -1 || grid[r][c+1] == 0) p++ ; // right
            
            if ( r == 0 ||  grid[r-1][c] == 0) p++ ; // up
            
            if ( r == row-1|| grid[r+1][c] == 0) p++ ; // down
            
            // cout << r << ":" << c << " -> " << p << endl;
            
            if (c-1 > -1 && grid[r][c-1] == 1)
                p = visit(grid, visited, r, c-1, p);
            
            if ( c+1 < col && grid[r][c+1] == 1)
                p = visit(grid, visited, r, c+1, p);
            
            if ( r-1 > -1 &&  grid[r-1][c] == 1)
                p = visit(grid, visited, r-1, c, p);
            
            if ( r+1 < row && grid[r+1][c] == 1)
                p = visit(grid, visited, r+1, c, p);
        }
        return p;
        
    }
    int islandPerimeter(vector<vector<int>>& grid) {
        row = grid.size();
        col = grid[0].size();
        int p = 0 , r = 0,c =0 ;
        
        int **visited = new int*[row];
        for (int i = 0;i<row ; i++)
            visited[i] = new int[col];
        for ( r = 0 ; r < row ; r++)
            for (c = 0; c < col ; c++)
                    visited[r][c] = 0;
        r = 0;
        c = 0;
        for (int r = 0 ; r < row ; r++)
            for (int c = 0 ; c < col ; c++)
                if (grid[r][c] == 1){ 
                    p = visit(grid, visited, r, c, p);
                    break;
                }
        return p;
    }
};