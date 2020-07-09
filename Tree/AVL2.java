import java.util.Vector;
import java.util.Scanner;
import java.util.Random;
import java.util.Collections;
import java.util.Vector;
import java.io.BufferedReader;
import java.io.FileReader;
class AVL {
	public Node root;
	Vector<Node> ListNode = new Vector<Node>();
	Vector<Node> Result = new Vector<Node>();
	
	public AVL()	{}
	
	//Structure
	class Node {
		Integer ID;
		String Name;
		String Birthday;
		float DTBTL;
		int STCTL;

		Node left;
		Node right;
		Node parent;
		
		public Node(Integer ID, String Name, String Birthday, float DTBTL, int STCTL)	{
			this.ID = ID;
			this.Name = Name;
			this.Birthday = Birthday;
			this.DTBTL = DTBTL;
			this.STCTL = STCTL;
		}
	}
	
	//Put
	private Node Put(Node x, Integer ID, String Name, String Birthday, float DTBTL, int STCTL, Node src)	{
		if (x == null)	{
			Node child = new Node(ID, Name, Birthday, DTBTL, STCTL);
			child.parent = src;
			return child;
		}
		int cmp = ID.compareTo(x.ID);
		if (cmp < 0)
			x.left = Put(x.left, ID, Name, Birthday, DTBTL, STCTL, x);
		else if (cmp > 0)
			x.right = Put(x.right, ID, Name, Birthday, DTBTL, STCTL, x);
		else; // This value has exist, so do nothing
		return balance(x);
	}

	public void Put(Node add) {
		root = Put(root, add.ID, add.Name, add.Birthday, add.DTBTL, add.STCTL, root);
	}
	//~~ end Put - in normal case

	//create tree none, random, deviation left, deviation right
	// create tree none - public AVL()	{} - above
	public void randomAVL()	{
		Random r = new Random();
	
		int length = r.nextInt(20) + 10;
		Integer ID;
		String name;
		int d, m, y, STCTL;
		float DTBTL;
		
		Vector<Integer> vc = new Vector<Integer>();
		Vector<Integer> month = new Vector<Integer>();
		month.add(4);
		month.add(6);
		month.add(9);
		month.add(11);
		
		for (int i = 0; i < length; i++)	{
			do {
				ID = r.nextInt(100) + 1;
			} while (vc.contains(ID));
			vc.add(ID);
			
			name = "";
			char c = (char)(r.nextInt('Z' - 'A') + 'A');
			name += String.valueOf(c);
			for (int j = 0; j < r.nextInt(5) + 5; j++)	{
				c = (char)(r.nextInt('z' - 'a') + 'a');
				name += String.valueOf(c);
			}
			
			d = r.nextInt(30) + 1;
			
			do {
				m = r.nextInt(11) + 1;
			} while ((month.contains(m) && d == 31) || (d > 29 && m == 2) );
			
			do {
				y = r.nextInt(2018 - 1990) + 1990;
			} while (m == 2 && d == 29 && !(((y % 4 == 0) && (y % 100!= 0)) || (y%400 == 0)));
			
			DTBTL = r.nextFloat()*(5) + 5;
			DTBTL = (float)Math.round(DTBTL*10)/10;
			
			STCTL = r.nextInt(100) + 50;
			
			Put(new Node(ID, name, d + "-" + "m" + "-" + "y", DTBTL, STCTL));
		}
	}
	
	//Browse LNR, LRN, NLR, RNL, NRL, RLN
	//call in here
	private void LNR (Node x)	{
		if (x != null)	{
			LNR(x.left);
			Display(x);
			LNR(x.right);
		}
	}

	private void LRN (Node x)	{
		if (x != null)	{
			LRN(x.left);
			LRN(x.right);
			Display(x);
		}
	} 

	private void NLR (Node x)	{
		if (x != null)	{
			Display(x);
			NLR(x.left);
			NLR(x.right);
		}
	}

	private void RNL (Node x)	{
		if (x != null)	{
			RNL(x.right);
			Display(x);
			RNL(x.left);
		}
	} 

	private void NRL (Node x)	{
		if (x != null)	{
			Display(x);
			NRL(x.right);
			NRL(x.left);
		}
	}

	private void RLN (Node x)	{
		if (x != null)	{
			RLN(x.right);
			RLN(x.left);
			Display(x);
		}
	} 
	//call from main	
	private void LNR ()	{	LNR(root);	}
	private void LRN ()	{	LRN(root);	}
	private void NLR ()	{	NLR(root);	}
	private void RNL ()	{	RNL(root);	}
	private void NRL ()	{	NRL(root);	}
	private void RLN ()	{	RLN(root);	}

	// Display info
	private void Display (Node x)	{
		System.out.println("ID: " + x.ID);
		System.out.println("Name: " + x.Name);
		System.out.println("Birthday: " + x.Birthday);
		System.out.println("DTBTL: " + x.DTBTL);
		System.out.println("STCTL: " + x.STCTL);
		System.out.println("------------------");
	}
	//~~~
	
	//Serch by ID, Name, Birthday, DTBTL, STCTL and min, max
	//call in here!
	private Node getElementByID(Node x, Integer ID) {
		if (x == null)
			return null;
		int cmp = ID.compareTo(x.ID);
		if (cmp < 0)
			return getElementByID(x.left, ID);
		else if (cmp > 0)
			return getElementByID(x.right, ID);
		else
			return x;
	}

	//getElementByName, getElementByBirthday, getElementByDTBTL, getElementBySTCTL return a list value store in Vector Result
	private void getElementByName(Node x, String Name) {
		if (x != null) {
			checkName(x, Name);
			getElementByName(x.left, Name);
			getElementByName(x.right, Name);
		}
	}

	private void checkName(Node x, String Name)	{
		if (Name.equalsIgnoreCase(x.Name))
			Result.add(x);
	}

	private void getElementByBirthday(Node x, String Birthday) {
		if (x != null) {
			checkBirthday(x, Birthday);
			getElementByBirthday(x.left, Birthday);
			getElementByBirthday(x.right, Birthday);
		}
	}

	private void checkBirthday(Node x, String Birthday)	{
		if (Birthday.equalsIgnoreCase(x.Birthday))
			Result.add(x);
	}

	private void getElementByDTBTL(Node x, float DTBTL) {
		if (x != null) {
			checkDTBTL(x, DTBTL);
			getElementByDTBTL(x.left, DTBTL);
			getElementByDTBTL(x.right, DTBTL);
		}
	}

	private void checkDTBTL(Node x, float DTBTL)	{
		if (DTBTL == x.DTBTL)
			Result.add(x);
	}

	private void getElementBySTCTL(Node x, Integer STCTL) {
		if (x != null) {
			checkSTCTL(x, STCTL);
			getElementBySTCTL(x.left, STCTL);
			getElementBySTCTL(x.right, STCTL);
		}
	}

	private void checkSTCTL(Node x, Integer STCTL)	{
		if (STCTL == x.STCTL)
			Result.add(x);
	}

	//Min, max
	private Node getMin(Node x)	{
		if (x.left != null)
			return getMin(x.left);
		else
			return x;
	}

	private Node getMax(Node x)	{
		if (x.right != null)
			return getMax(x.right);
		else
			return x;
	}
	//Call from main
	public Node getElementByID(Integer ID) {	return getElementByID(root, ID);	}
	public void getElementByName(String Name) {	Result.clear();	getElementByName(root, Name);	}
	public void getElementByBirthday(String Birthday) {	Result.clear();	getElementByBirthday(root, Birthday);	}
	public void getElementByDTBTL(float DTBTL) {	Result.clear(); getElementByDTBTL(root, DTBTL);	}
	public void getElementBySTCTL(Integer STCTL) {	Result.clear(); getElementBySTCTL(root, STCTL);	}
	public Node getMin()	{	return getMin(root);	}
	public Node getMax()	{	return getMax(root);	}
	//End~~~
	
	//Add node, Add list node
	//Add node is Put method above

	private void addListNode (Vector<Node> x)	{
		for (int i = 0; i < x.size(); i++)
			Put(x.get(i));
	}
	
	//Remove node, remove list node
	//call in here
	private Node removeNode (Node r, Node x) {
		if (r == null)
			return null;
		int cmp = x.ID.compareTo(r.ID);
		if (cmp < 0)
			r.left = removeNode(r.left, x);
		else if (cmp > 0)
			r.right = removeNode(r.right, x);
		else {
			if (r.left == null)
				return r.right;
			if (r.right == null)
				return r.left;
			Node t = r;
			r = getMin(t.right);
			r.right = removeNode(t.right, getMin(t.right));
			r.left = t.left;
		}
		return balance(r);
	}

	private void removeListNode (Vector<Node> x) {
		for (int i = 0; i < x.size(); i ++)
			removeNode(x.get(i));
	}
	
	//call from main
	public void removeNode(Node x)	{	root = removeNode(root, x);	}
	//Get Predecessor, Successor
	public Node getPredecessor(Node x) {
		if (x.left != null)
			return getMax(x.left);
		Node p = x.parent;
		Node T = x;
		while (p != null && T == p.left)	{
			T = p;
			p = T.parent;
		}
		return p;
	}

	public Node getSuccessor(Node x) {
		if (x.right != null)
			return getMin(x.right);
		Node p = x.parent;
		Node T = x;
		while (p != null && T == p.right)	{
			T = p;
			p = T.parent;
		}
		return p;
	}
	//~~~~~
	
	//Update
	private void Update(Integer ID)	{
		Scanner sc = new Scanner(System.in);
		
		Node x = getElementByID(ID);
		if (x == null)
			System.out.print("This tree do not contain ID: " + ID);
		else {
			System.out.print("New name: ");
			x.Name = sc.nextLine();
			System.out.print("New birthday: ");
			x.Birthday = sc.nextLine();
			System.out.print("New DTBTL: ");
			x.DTBTL = sc.nextFloat();
			System.out.print("New STCTL: ");
			x.STCTL = sc.nextInt();
			System.out.println("After update: ");
			Display(x);
		}
	}

	//My method
	public void fileToListNode(String fileIn)	throws Exception{
		String str;
		String [] value;
		
		Integer ID;
		String Name;
		String Birthday;
		float DTBTL;
		int STCTL;

		BufferedReader F = new BufferedReader(new FileReader(fileIn));
			str = F.readLine();
			while (str != null) {
				value = str.split(" ");
				
				ID = Integer.parseInt(value[0]);
				Name = value[1];
				Birthday = value[2];
				DTBTL = Float.parseFloat(value[3]);
				STCTL = Integer.parseInt(value[4]);

				ListNode.add(new Node(ID, Name, Birthday, DTBTL, STCTL));
				
				str = F.readLine();
			}
        F.close();
	}
	
	public int height(Node x)	{
		return x==null?-1:Math.max(height(x.left), height(x.right)) + 1;
	}
	
	public int checkBalance(Node x)	{
		return height(x.left) - height(x.right);
	}
	
	private Node rotateLeft(Node x) {
		Node y = x.right;
		x.right = y.left;
		y.left = x;
		return y;
	}
	
	private Node rotateRight(Node x) {
		Node y = x.left;
		x.left = y.right;
		y.right = x;
		return y;
	}
	
	private Node balance(Node x)	{
		if (checkBalance(x) < -1)	{
			if (checkBalance(x.right) > 0)
				x.right = rotateRight(x.right);
			x = rotateLeft(x);
		}
		else if (checkBalance(x) > 1) {
			if (checkBalance(x.left) < 0)
				x.left = rotateLeft(x.left);
			x = rotateRight(x);
		}
		return x;
	}
	//~~end my method

	public static void main(String [] args)	throws Exception{
		AVL avl = new AVL();
		/**
			Some method below conflict together (deviationLeft and deviationRight,...), should run each time one method to check program!
			Some input of search method may not work because it is not exist in the tree.
		*/
		
		avl.fileToListNode("input.txt");
		
		
		// avl.addListNode(avl.ListNode);
		// avl.LNR();
		
		// avl.randomAVL();
		// avl.LNR();
		
		//AVL can not contain deviationLeft and deviationRight
		
		// avl.randomAVL();
		
		// avl.LNR();
		// avl.LRN();
		// avl.RNL();
		// avl.RLN();
		// avl.NLR();
		// avl.NRL();
		
		//avl.getElementByID(10);
		
		// avl.getElementByName("DucD");
		// System.out.println(avl.Result.get(0).ID);
		
		// avl.getElementByName("Linh");
		// System.out.println(avl.Result.get(0).Birthday);
		
		// avl.getElementByBirthday("4-7-2001");
		// System.out.println(avl.Result.get(0).Name);
		
		// avl.getElementByDTBTL((float)6.5);
		// System.out.println(avl.Result.get(0).Name);
		// System.out.println(avl.Result.get(1).Name);
		
		// avl.getElementBySTCTL(100);
		// System.out.println(avl.Result.get(0).Name);
		// System.out.println(avl.Result.get(1).Name);
		// System.out.println(avl.Result.get(2).Name);
		
		// System.out.println(avl.getMin().Name);
		// System.out.println(avl.getMax().Name);
		
		// avl.addListNode(avl.ListNode);
		// avl.NLR();
		
		// avl.addListNode(avl.ListNode);
		// avl.removeNode(avl.getElementByID(9));
		// avl.NLR();
		
		// avl.addListNode(avl.ListNode);
		// avl.NLR();
		
		// Vector<Node> removeList = new Vector<Node>();
		// avl.getElementBySTCTL(100);
		// removeList.add(avl.Result.get(0));
		// removeList.add(avl.Result.get(1));
		// removeList.add(avl.Result.get(2));
		// avl.removeListNode(removeList);
		// avl.NLR();
		
		// System.out.print(avl.getSuccessor(avl.getElementByID(59)).ID);
		// System.out.print(avl.getPredecessor(avl.getElementByID(59)).ID);
		
		// System.out.println("Update with ID: " + 10);
		// avl.Update(10);
		// System.out.println("Afer update");
		// avl.Display(avl.getElementByID(10));
		// avl.NLR();
	}
}