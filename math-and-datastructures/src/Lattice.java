// I wonder if there is a more efficient data structure for this. 

import java.io.*;
import java.util.*;
public class Lattice {

    Node root;
    ArrayList<ArrayList<Node>> rows;


    public Lattice(ArrayList<String> lines) {
        String first = lines.get(0);
        root = new Node(Integer.parseInt(first), 0);
        rows = new ArrayList<ArrayList<Node>>();
        root.print();

        for (int i = 1; i < lines.size(); i++){
            // Save the (i-1)th pointers with the nodes. 
            String[] composing = lines.get(i).split(" ");

        }

    }


    private static ArrayList<String> readLines(String filename){
        BufferedReader input = null;
        ArrayList<String> ret = new ArrayList<String>();
        try {
            input = new BufferedReader(new FileReader(filename));
            while(input.ready()){
                String s = input.readLine();
                ret.add(s);
            }
        } catch (Exception e) {
            System.out.println(e);
            System.exit(-1);
        }
        
        return ret;
    }

    private static void say(String s){
        System.out.println(s);
    }

    public static void main (String[] args) {
        if (args.length != 1) {
            System.err.println("Need the file name command line argument.");
            System.exit(-1);
        }

        
        ArrayList<String> lines = readLines(args[0]);

        Lattice l = new Lattice(lines);


    }


    private class Node {
        int num;
        int position;
        Node down;
        Node right; 
        Node prev; // set if&f the currNode is the preferred choice. 

        public Node(int num, int position) {
            this.num = num;
        }

        public void print(){
            String s = "";
            s += "Pointer : " + this + "\n";
            s += "Position: " + position + "\n";
            s += "Number  : " + num + "\n";
            s += "DownPos : " + down + "\n";
            s += "--> Pos : " + right + "\n";
            s += "Previous: " + prev + "\n";
            System.out.println(s);
        }


    }



}