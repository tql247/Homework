/**
 * BellmanFord
 * input: input.txt
 * Run: Use Bellman Ford method to find shorted path
 * output: Shorted Path
 */
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Vector;
class BellmanFord {
    public static int[][] matrix_graph;
    public static int[] P;
    public static int[] D;
    public static int V;

    public static void fileToGraph (String fileIn) throws Exception {
        Vector<String> Vc = new Vector<String>();
        String str = "";

        BufferedReader F = new BufferedReader(new FileReader(fileIn));
        while (str != null) {
            if (str != "")
                Vc.add(str);
            str = F.readLine();
        }
        F.close();

        matrix_graph = new int[Vc.size()][Vc.size()];
        V = Vc.size();

        String[] value;

        for (int i = 0; i < V; i++) {
            value = Vc.get(i).split(" ");
            for (int j = 0; j < V; j++) {
                matrix_graph[i][j] = Integer.parseInt(value[j]);
            }
        }

        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                System.out.print(matrix_graph[i][j] + " ");
            }
            System.out.println();
        }
    }
    
    public static void Bellman(int start)    {
        D = new int[V];
        P = new int[V];
        //initialization
        for(int i = 0; i < V; i++)  {
            if (i == start) {
                D[i] = 0;
                P[i] = i;
            }
            else
                D[i] = 1000;
        }

        //Add Vertical
        for (int i = 0; i < V; i++) {
            for (int j = i; j < V; j++) {
                if (matrix_graph[i][j] != 0)
                    relax(i, j);
            }
        }
    }

    public static void relax(int i, int j) {
        if (D[j] > D[i] + matrix_graph[i][j])   {
            D[j] = D[i] + matrix_graph[i][j];
            P[j] = i;
        }
    }

    public static void Path(int start, int finish)   {
        for (int i = finish; i != start;i = P[i])
            System.out.print(i + "<---");
        System.out.print(start);
    }

    public static void main(String [] args) throws Exception{
        System.out.println("From input: ");
        fileToGraph("input.txt");
        Bellman(0);
        System.out.println("Shorted Path 0->5:");
        Path(0, 5);
    }
}