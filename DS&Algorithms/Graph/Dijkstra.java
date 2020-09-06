/**
 * Dijkstra's
 * input: input.txt
 * Run: Use Dijkstra's method to find shorted path
 * output: Shorted Path
 */
import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Vector;
class Dijkstra {
    public static int[][] matrix_graph;
    public static int[] P;
    public static int[] D;
    public static boolean[] visit;
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
    
    public static void DijkstraAlgorithm(int start)    {
        D = new int[V + 1];
        P = new int[V];
        visit = new boolean[V];
        // Initialization
        for (int i = 0; i < V; i++) {
            D[i] = Integer.MAX_VALUE;
            P[i] = i;
            visit[i] = false;
        }

        D[start] = 0;
        
        for (int i = 0; i < V - 1; i++) {
            int u = minD();
            visit[u] = true;

            for(int v = 0; v < V; v++)
                if(!visit[v] && matrix_graph[u][v] != 0)
                    relax(u, v);
        }
    }

    public static int minD()    {
        int min = Integer.MAX_VALUE;
        int min_index = -1;
        for (int v = 0; v < V; v++) 
            if (visit[v] == false && D[v] <= min) { 
                min = D[v]; 
                min_index = v; 
            } 
        return min_index;
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
        DijkstraAlgorithm(0);
        System.out.println("Shorted Path 0->5:");
        Path(0, 5);
    }
}