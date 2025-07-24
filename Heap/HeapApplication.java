import java.util.Arrays;
import java.util.Collections;
import java.util.PriorityQueue;

public class HeapApplication {
    public static void main(String[] args) {
        // [20,10,17,30,40]
        // Creating the min heap and max heap
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(); // empty min heap
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder()); // empty max Heap

        // Adding elements to min Heap and max Heap
        maxHeap.add(20);
        maxHeap.add(10);
        maxHeap.add(17);
        maxHeap.add(30);
        maxHeap.add(40);

        minHeap.add(20);
        minHeap.add(10);
        minHeap.add(17);
        minHeap.add(30);
        minHeap.add(40);

        // peek element
        System.out.println("Min Heap: MIN: " + minHeap.peek());
        System.out.println("Max Heap: MAX: " + maxHeap.peek());

        // removing element
        minHeap.poll();
        maxHeap.poll();

        System.out.println("Min Heap: MIN: " + minHeap.peek());
        System.out.println("Max Heap: MAX: " + maxHeap.peek());

        // size
        System.out.println(minHeap.size());
        System.out.println(maxHeap.size());

        // empty
        System.out.println(minHeap.isEmpty());

        // creating min heap using heapify

        PriorityQueue<Integer> minHeapUsingHeapify = new PriorityQueue<>(Arrays.asList(20, 10, 17, 30, 40));
        System.out.println(minHeapUsingHeapify.peek());

    }
}
