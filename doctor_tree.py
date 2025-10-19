from platform import node

class DoctorNode:
    def __init__(self, name):
        self.DoctorName = name
        self.LeftReport = None
        self.RightReport = None

    def SetReport(self, reporting_doctor, side):
        side = side.lower()
        
        if side == 'left':
            if self.LeftReport is not None:
                raise ValueError("Error: Left report already exists")
            else:
                self.LeftReport = DoctorNode(reporting_doctor)
        elif side == 'right':
            if self.RightReport is not None:
                raise ValueError("Error: Right report already exists")
            else:
                self.RightReport = DoctorNode(reporting_doctor)
        else:
            raise ValueError("Error: Side must be 'left' or 'right'")


    def __repr__(self):
        return f"Doctor ({self.DoctorName})"


class DoctorTree:
    def __init__(self, root_name):
        self.root = DoctorNode(root_name)

    def insert(self, doctor_name, reporting_doctor_name, reporting_side):

        doctor_node = self.find_node(self.root, doctor_name)
        if doctor_node is None:
            raise ValueError(f"Error: Doctor '{doctor_name}'not found")
        doctor_node.SetReport(reporting_doctor_name, reporting_side)

    def find_node(self, current_node, doctor_to_find):
        if current_node is None:
            return None
        if current_node.DoctorName == doctor_to_find:
            return current_node
        left_search = self.find_node(current_node.LeftReport, doctor_to_find)
        if left_search is not None:
            return left_search
        right_search = self.find_node(current_node.RightReport, doctor_to_find)
        if right_search is not None:
            return right_search
        return None

    # Root -> Left -> Right
    def preorder(self, node=None):
        if node is not None:
            print(node)
            self.preorder(node.LeftReport)
            self.preorder(node.RightReport)

    # Left -> Root -> Right
    def inorder(self, node=None):
        if node is not None:
            self.inorder(node.LeftReport)
            print(node)
            self.inorder(node.RightReport)

    # Left -> Right -> Root
    def postorder(self, node=None):
        if node is not None:
            self.postorder(node.LeftReport)
            self.postorder(node.RightReport)
            print(node)

# Test code
if __name__ == "__main__":  
    tree = DoctorTree("Dr. Croft")
    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    # Expected Error Cases
    try:
        tree.insert("Dr. Phan", "Dr. Lee", "left") 
    except ValueError as err:
        print(err)    
    try:   
        tree.insert("Dr. Invalid", "Dr. Smith", "left")
    except ValueError as err:
        print(err)    
    try:
        tree.insert("Dr. Goldsmith", "Dr. Doolittle", "invalid_side")
    except ValueError as err:
        print(err)

    print("Preorder Traversal:")
    tree.preorder(tree.root)

    print("\nInorder Traversal:")
    tree.inorder(tree.root)

    print("\nPostorder Traversal:")
    tree.postorder(tree.root)



