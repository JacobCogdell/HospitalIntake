class Patient:
    def __init__(self, name, urgency=10):
        self.PatientName = name
        self.Urgency = urgency

    def __repr__(self):
        return f"Patient ({self.PatientName}, Urgency: {self.Urgency})"
    



class MinHeap:
    def __init__(self):
        self.PatientData = []

    def heapify_up(self, index):
        if index == 0:
            # Reached the root
            return
        
        # Heaps only care about the relationship between parent and child
        # So we calculate the parent index
        parent_index = (index - 1) // 2

        if self.PatientData[index].Urgency < self.PatientData[parent_index].Urgency:
            # Swap the elements and continue heapifying up
            self.PatientData[index], self.PatientData[parent_index] = self.PatientData[parent_index], self.PatientData[index]
            self.heapify_up(parent_index)
    
    def heapify_down(self, index):
        num_patients = len(self.PatientData)
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        smallest_index = index

        if left_index < num_patients and self.PatientData[left_index].Urgency < self.PatientData[smallest_index].Urgency:
            smallest_index = left_index

        if right_index < num_patients and self.PatientData[right_index].Urgency < self.PatientData[smallest_index].Urgency:
            smallest_index = right_index

        if smallest_index != index:
            self.PatientData[index], self.PatientData[smallest_index] = self.PatientData[smallest_index], self.PatientData[index]
            self.heapify_down(smallest_index)

    def insert(self, patient):
        self.PatientData.append(patient)
        self.heapify_up(len(self.PatientData) - 1)

    def print_heap(self):
        print("Current Patient Queue (Min-Heap):")
        for patient in self.PatientData:
            print(patient)

    def extract_min(self):
      if not self.PatientData:
          return None

      self.PatientData[0], self.PatientData[-1] = self.PatientData[-1], self.PatientData[0]   

      min_patient = self.PatientData.pop()
      if self.PatientData:
        self.heapify_down(0)
      return min_patient
    
    def peek_min(self):
        if not self.PatientData:
            return None
        print(self.PatientData[0])

# Test your MinHeap class here including edge cases
if __name__ == "__main__":
    emergency_queue = MinHeap()
    emergency_queue.insert(Patient("Jordan", 3))
    emergency_queue.insert(Patient("Taylor", 1))  
    emergency_queue.insert(Patient("Avery", 5))
    emergency_queue.print_heap()  
    print("\nPeek at highest urgency patient:")
    emergency_queue.peek_min()
    next_patient = emergency_queue.extract_min()
    print(f"\nNext Patient: {next_patient}")
    print(f"\nRemaining Patients after extraction:")
    emergency_queue.print_heap()
