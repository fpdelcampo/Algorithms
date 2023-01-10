package Algorithms.Java;

public class LinkedListNode {
    
    public LinkedListNode next;
    public int data;

    public LinkedListNode(LinkedListNode next, int data) {
        this.next = next;
        this.data = data;
    }

    public LinkedListNode getNext() {
        return this.next;
    }

    public int getData() {
        return this.data;
    }

    public void setNext(LinkedListNode next) {
        this.next = next;
    }

    public void setData(int data) {
        this.data = data;
    }
}