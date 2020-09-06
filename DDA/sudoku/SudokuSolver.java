import java.io.BufferedWriter;
import java.io.FileWriter;
import java.util.Random;
import java.util.Vector;
class SudokuSolver {
    Block root;
    Vector<Block> elem = new Vector<Block>(); 
    Vector<Block> sudoku_blk = new Vector<Block>(); 
	Vector<Integer> dectect = new Vector<Integer>();
	int[][] sudoku_final;
	int len = 3;
	Random rd;

    public SudokuSolver(){}

    class Block{
        Integer [][] val = new Integer[3][3];

        public Block(){}

        public Block(Integer [][] val) {
            this.val = val;
        }

        public void Display() {
            for (int i = 0; i < 3; i++) {
                for(int j = 0; j < 3; j++)  {
                    System.out.print(val[i][j] + " ");
                }
                System.out.println();
            }
			System.out.println("-----------------------");
        }
    }

    public void getSquare()  {
        Block tmp;
		
		perm();
		
        rd = new Random();
		
		root = elem.get(rd.nextInt(11));
		
		int number;
        for (int i = 0; i < 9; i++) {
			do {
				number = rd.nextInt(11);
			} while (dectect.contains(number));
			dectect.add(number);
			sudoku_blk.add(elem.get(number));
        }
		
		sudoku_final = new int [len*len][len*len];
		
		int row = 0, col = 0;
		for (int i = 0; i < sudoku_blk.size(); i++) {
			for (int j = 0; j < len; j++) {
				for (int k = 0; k < len; k++) {
					sudoku_final[(i/3)*3 + j][(i*3 + k) % 9] = root.val[row][col]*3 + sudoku_blk.get(i).val[j][k] + 1;
				}
			}
			col += 1;
			if (col > len - 1) {
				col = 0;
				row = row + 1;
			}
		}
		
		
		// swap(2, 4);
		swap(2 - 1, 4 - 1);
		// swap(3, 7);
		swap(3 - 1, 7 - 1);
		// swap(6, 8);
		swap(6 - 1, 8 - 1);

		//done!
    }
	
	public void diggingHole(int hole) {
		int col, row;
		for (int i = 0; i < hole; i++) {
			do {
				row = rd.nextInt(9);
				col = rd.nextInt(9);
			} while (sudoku_final[row][col] == 0);
			sudoku_final[row][col] = 0;
		}
	}
	
	public void swap(int src, int dir)	{
		int [] buffer = new int[9];
		
		for (int i = 0; i < 9; i++) {
			buffer[i] = sudoku_final[src][i];
		}
		
		for (int i = 0; i < 9; i++) {
			sudoku_final[src][i] = sudoku_final[dir][i];
		}
		
		for (int i = 0; i < 9; i++) {
			sudoku_final[dir][i] = buffer[i];
		}
	}

    public void LatinSquare(int [] start)    { //with n = 3
        Integer [][] blk1 = new Integer[3][3];
        Integer [][] blk2 = new Integer[3][3];
        
		for (int i = 0; i < len; i++) {
			for (int j = 0; j < len; j++) {
				if (i == 0) {
					blk1[i][j] = start[j] - 1;
				} else {
					blk1[i][j] = blk1[i - 1][next(j, -1)];
				}
			}
		}
		
		for (int i = 0; i < len; i++) {
			for (int j = 0; j < len; j++) {
				if (i == 0) {
					blk2[i][j] = start[j] - 1;
				} else {
					blk2[i][j] = blk2[i - 1][next(j, 1)];
				}
			}
		}
		
		elem.add(new Block(blk1));
		elem.add(new Block(blk2));
    }
	
	public int next(int col, int idx) {
		if (col + idx >= len)
			return 0;
		else if (col + idx < 0)
			return len - 1;
		return col + idx;
	}
	
	public void SteinhausJohnsonTrotter (int k, int [] p, int [] pi, int [] d){
		int x, y, j;
		
		if (k > len) {
			LatinSquare(p);
		} else {
			SteinhausJohnsonTrotter(k + 1, p, pi, d);
			for (int c = 1; c <= k - 1; c++)	{
				x = pi[k];
				y = x + d[k];
				j = p[y];
				p[x] = j; pi[j] = x;
				p[y] = k; pi[k] = y;
				SteinhausJohnsonTrotter(k + 1, p, pi, d);
			}
			d[k] = -d[k];
		}
	}
	
	
	public void perm()	{
		int [] p = new int[len+1];
		int [] pi = new int[len+1];
		int [] d = new int[len+1];
		
		for (int i = 0; i < len; i++) {
			p[i] = i + 1;
			d[i] = -1;
		}
		p[len] = 0;
		d[len] = -1;
		
		for (int i = 0; i < len + 1; i++) {
			pi[p[i]] = i; 
		}
		
		SteinhausJohnsonTrotter(1, p, pi, d);
	}

    public void Solution(String fileName) throws Exception{
		BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++)	{
					writer.write(sudoku_final[i][j] + " ");
				}
				writer.write("\n");
			}
		writer.close();
	}

    public void Puzz(String fileName) throws Exception{
		BufferedWriter writer = new BufferedWriter(new FileWriter(fileName));
			for (int i = 0; i < 9; i++) {
				for (int j = 0; j < 9; j++)	{
					writer.write(sudoku_final[i][j] + " ");
				}
				writer.write("\n");
			}
		writer.close();
	}
}