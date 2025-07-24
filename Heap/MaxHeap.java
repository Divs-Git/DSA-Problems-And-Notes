import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class MaxHeap {
    List<Integer> heap;

    // T: O(1), S: O(1)
    public MaxHeap() {
        heap = new ArrayList<>();
    }

    // T: O(n), S: O(1)
    public MaxHeap(int[] nums) {
        // build max heap by given array
        heap = new ArrayList<>();

        int n = nums.length;

        for (int num : nums) {
            heap.add(num);
        }

        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(i);
        }
    }

    // T: O(1), S: O(1)
    public int peek() {
        if (heap.size() == 0) {
            return Integer.MAX_VALUE;
        }
        return heap.get(0);
    }

    // T: O(nlogn), S: O(1)
    public void heapSort() {
        for (int i = heap.size() - 1; i >= 0; i--) {
            Collections.swap(heap, 0, i);
            heapify(0, i);
        }
    }

    // T: O(logn), S: O(1)
    public void heapify(int index) {

        int size = heap.size();
        int largest = index;

        while (index < size) {

            int lci = 2 * index + 1;
            int rci = 2 * index + 2;

            if (lci < size && heap.get(lci) > heap.get(largest)) {
                largest = lci;
            }

            if (rci < size && heap.get(rci) > heap.get(largest)) {
                largest = rci;
            }

            if (largest != index) {
                Collections.swap(heap, index, largest);
                index = largest;
            } else {
                break;
            }

        }
    }

    public void heapify(int index, int size) {

        int largest = index;

        while (index < size) {

            int lci = 2 * index + 1;
            int rci = 2 * index + 2;

            if (lci < size && heap.get(lci) > heap.get(largest)) {
                largest = lci;
            }

            if (rci < size && heap.get(rci) > heap.get(largest)) {
                largest = rci;
            }

            if (largest != index) {
                Collections.swap(heap, index, largest);
                index = largest;
            } else {
                break;
            }

        }
    }

    // T: O(logn), S: O(1)
    public void insert(int val) {
        heap.add(val);

        int index = heap.size() - 1;

        while (index > 0) {
            int parentIdx = (index - 1) / 2;

            if (heap.get(parentIdx) < heap.get(index)) {
                Collections.swap(heap, index, parentIdx);
                index = parentIdx;
            } else {
                break;
            }
        }
    }

    // T: O(logn), S: O(1)
    public int pop() {
        if (heap.size() == 0) {
            return Integer.MAX_VALUE;
        }

        int pop = heap.get(0);
        int lastIdx = heap.size() - 1;
        heap.set(0, heap.get(lastIdx));
        heap.remove(lastIdx);

        heapify(0);

        return pop;
    }

    public void print() {
        for (int i = 0; i < heap.size(); i++) {
            System.out.println(heap.get(i));
        }
    }
}

class Main {
    public static void main(String[] args) {
        // MaxHeap mh = new MaxHeap();

        // System.out.println(mh.peek());

        // mh.insert(100);
        // mh.insert(200);
        // mh.insert(50);

        // System.out.println(mh.peek());

        // System.out.println(mh.pop());

        // mh.print();

        // mh.insert(250);
        // System.out.println(mh.peek());

        int[] nums = {
                20,
                10,
                17,
                30,
                40
        };

        MaxHeap mh = new MaxHeap(nums);
        mh.heapSort();
        mh.print();

    }
}