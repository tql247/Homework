/** Sudoku
    Input:
        args[0]: Solution file out without hole
        args[1]: Puzzle file out with hole
        args[2]: Number of hole in file Puzzle
        Example: java SudokuGenerator solution.txt puzzle.txt 50 (SudokuGenerator.java must complied before run this command)
    Output:
        File Solution contains solution of the sudoku
        File Puzzle contains puzzle of the sudoku
*/
class SudokuGenerator {
    public static void main(String [] args) throws Exception {
        SudokuSolver sdk = new SudokuSolver();

        sdk.getSquare();
        sdk.Solution(args[0]);
		sdk.diggingHole(Integer.parseInt(args[2]));
        sdk.Puzz(args[1]);
    }
}