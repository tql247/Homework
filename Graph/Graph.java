import java.io.BufferedReader;
import java.io.FileReader;
import java.util.Vector;
import java.util.LinkedList;
import java.util.Queue;

class Graph {
    public static int[][] matrix_graph;
    public static int V;

    public Graph(String fileIn) throws Exception {
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
        System.out.print("Loaded matrix from file: \n");
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++) {
                System.out.print(matrix_graph[i][j] + " ");
            }
            System.out.println();
        }
    }

    public void BFS() {
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visit = new boolean[V];
        for(int i = 0; i < V; i++) visit[i] = false;
    
        visit[0] = true;
        queue.add(0);
        while (queue.size() != 0)   {
            int curr = queue.poll();
            System.out.print(curr + " ");
            for (int i = 0; i < V; i++) {
                if (matrix_graph[curr][i] == 1 && visit[i] == false)    {
                    visit[i] = true;
                    queue.add(i);
                }
            }
        }
    }

    public void DFS(int begin) {
        boolean[] visit = new boolean[V];
        for (int i = 0; i < V; i++)
            visit[i] = false;
        DFS(begin, visit);
    }

    public static void DFS(int begin, boolean[] visit) {
        System.out.print(begin + " ");
        visit[begin] = true;
        for (int i = 0; i < V; i++) {
            if (matrix_graph[begin][i] == 1 && visit[i] == false)
                DFS(i, visit);
        }
    }

    public static boolean Circle_Graph()    {
        int[] p = new int[V];
        for (int i = 0; i < V; i++)
            p[i] = -1;
        for (int i = 0; i < V; i++) {
            for (int j = 0; j < V; j++){
                if (matrix_graph[i][j] == 1 && p[j] == -1)
                    p[j] = p[i];
                else if (matrix_graph[i][j] == 1 && (p[j] != i && p[j] != -1))
                    return true;
            }
        }
        return false;
    }

    public static void main(String[] args) throws Exception {
        Graph g = new Graph("graph.txt");
        
        System.out.print("BFS browser: ");
        g.BFS();
        System.out.println();
        System.out.print("DFS browser: ");
        g.DFS(0);
    }
}