class perm {
	static int len = 4;
	
	public static void SteinhausJohnsonTrotter (int k, int [] p, int [] pi, int [] d){
		int x, y, j;
		
		if (k > len) {
			for (int i = 0; i < len; i++)
				System.out.print(p[i] + " ");
			System.out.println();
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
	
	
	public static void main(String [] args)	{
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
}